from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

try:
    import faiss  # type: ignore
except ModuleNotFoundError:  # local dev may not have faiss installed
    faiss = None  # type: ignore
import numpy as np
from bs4 import BeautifulSoup

from .embeddings import LocalEmbeddings


@dataclass(frozen=True)
class Chunk:
    # Immutable chunk + metadata:
    # - makes it harder to accidentally mutate the text used for indexing
    # - allows safe reuse when building/storing metadata
    chunk_id: int
    text: str
    metadata: Dict[str, Any]


def _iter_markdown_files(root: Path) -> Iterable[Path]:
    for p in root.rglob("*.md"):
        if p.is_file():
            yield p


def _read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace")


def _chunk_text_by_paragraphs(text: str, *, chunk_size: int, overlap: int) -> List[str]:
    # chunk_size/overlap are in characters (approx). This keeps the implementation simple
    # while still respecting doc structure via paragraph boundaries.
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks: List[str] = []
    buf: List[str] = []
    buf_len = 0

    def flush() -> None:
        nonlocal buf, buf_len
        if not buf:
            return
        chunk = "\n\n".join(buf).strip()
        if chunk:
            chunks.append(chunk)
        buf = []
        buf_len = 0

    i = 0
    while i < len(paragraphs):
        p = paragraphs[i]
        if buf_len + len(p) + 2 > chunk_size and buf:
            flush()
            # Overlap: we keep a small tail of previous paragraphs to preserve context.
            # (Heuristic: “last few paras” works well for documentation text.)
            if overlap > 0:
                tail = paragraphs[max(0, i - 3) : i]  # heuristic: keep last few paras
                buf = []
                buf_len = 0
                for t in tail:
                    if buf_len + len(t) + 2 > overlap:
                        break
                    buf.append(t)
                    buf_len += len(t) + 2
            continue
        buf.append(p)
        buf_len += len(p) + 2
        i += 1

    flush()
    # final merge guard: avoid many tiny chunks
    return [c for c in chunks if len(c.strip()) >= 80]


def _clean_markdown(text: str) -> str:
    # If markdown contains HTML fragments, strip them lightly.
    # This avoids feeding raw HTML tags into embeddings/prompt context.
    if "<" in text and ">" in text:
        soup = BeautifulSoup(text, "html.parser")
        return soup.get_text("\n").strip()
    return text.strip()


@dataclass(frozen=True)
class VectorStoreConfig:
    # Immutable config for the index:
    # - changing chunking/top_k/etc should trigger rebuilds
    # - freezing avoids accidental runtime drift
    vector_dir: Path
    # Source roots:
    markdown_root: Path
    specifiers_jsonl: Path
    unreal_specifiers_root: Path
    # Source switch:
    # - include both `scraped_data/content/unreal_specifiers.jsonl` AND the
    #   `unreal_specifiers/` markdown tree (useful if you want redundancy or more granularity).
    include_unreal_specifiers_dir: bool = True

    # Chunking / indexing:
    chunk_size: int = 1400
    chunk_overlap: int = 200

    # Retrieval:
    top_k: int = 6

    # Safety limit:
    # Embedding all chunks can OOM in free Docker / small RAM environments.
    # When set, vectorstore build stops after embedding this many chunks total.
    max_chunks: int | None = None


class VectorStore:
    def __init__(
        self,
        cfg: VectorStoreConfig,
        embeddings: LocalEmbeddings,
    ):
        self.cfg = cfg
        self.embeddings = embeddings

        self.index_path = cfg.vector_dir / "faiss.index"
        self.meta_path = cfg.vector_dir / "metadata.jsonl"
        self.state_path = cfg.vector_dir / "state.json"

        self._index: faiss.Index | None = None
        self._meta: List[Dict[str, Any]] = []

    def _load_meta(self) -> None:
        meta: List[Dict[str, Any]] = []
        with open(self.meta_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                meta.append(json.loads(line))
        self._meta = meta

    def _load_index(self) -> None:
        if faiss is None:
            raise ModuleNotFoundError(
                "faiss is not installed. Install faiss-cpu to load/build the vector index."
            )
        idx = faiss.read_index(str(self.index_path))
        self._index = idx

    def load(self) -> bool:
        if not self.index_path.exists() or not self.meta_path.exists():
            return False
        self._load_meta()
        self._load_index()
        return True

    def _source_chunks(self) -> Iterable[Chunk]:
        chunk_id = 0

        # 1) scraped_data/markdown_by_path/**/*.md
        if self.cfg.markdown_root.exists():
            for p in _iter_markdown_files(self.cfg.markdown_root):
                rel = p.relative_to(self.cfg.markdown_root)
                title = rel.parts[-1].rsplit(".", 1)[0]
                raw = _read_text(p)
                raw = _clean_markdown(raw)
                chunks = _chunk_text_by_paragraphs(
                    raw, chunk_size=self.cfg.chunk_size, overlap=self.cfg.chunk_overlap
                )
                for i, c in enumerate(chunks):
                    if self.cfg.max_chunks is not None and chunk_id >= self.cfg.max_chunks:
                        return
                    yield Chunk(
                        chunk_id=chunk_id,
                        text=c,
                        metadata={
                            "source_type": "markdown",
                            "path": str(rel),
                            "title": title,
                            "chunk_index": i,
                        },
                    )
                    chunk_id += 1

        # 2) scraped_data/content/unreal_specifiers.jsonl
        if self.cfg.specifiers_jsonl.exists():
            with open(self.cfg.specifiers_jsonl, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    obj = json.loads(line)
                    text = obj.get("content") or ""
                    text = _clean_markdown(text)
                    if len(text) < 80:
                        continue
                    rel_path = obj.get("path") or obj.get("title") or "unreal_specifiers"
                    title = obj.get("title") or rel_path
                    chunks = _chunk_text_by_paragraphs(
                        text, chunk_size=self.cfg.chunk_size // 2, overlap=120
                    )
                    if not chunks:
                        chunks = [text]
                    for i, c in enumerate(chunks):
                        if self.cfg.max_chunks is not None and chunk_id >= self.cfg.max_chunks:
                            return
                        yield Chunk(
                            chunk_id=chunk_id,
                            text=c,
                            metadata={
                                "source_type": "specifier",
                                "path": str(rel_path),
                                "title": title,
                                "chunk_index": i,
                                "category": obj.get("category") or "",
                                "source": obj.get("source") or "UnrealSpecifiers",
                            },
                        )
                        chunk_id += 1

        # 3) unreal_specifiers/ (directory of markdown)
        if self.cfg.include_unreal_specifiers_dir and self.cfg.unreal_specifiers_root.exists():
            for p in _iter_markdown_files(self.cfg.unreal_specifiers_root):
                rel = p.relative_to(self.cfg.unreal_specifiers_root)
                title = rel.parts[-1].rsplit(".", 1)[0]
                raw = _read_text(p)
                raw = _clean_markdown(raw)
                if len(raw) < 80:
                    continue
                chunks = _chunk_text_by_paragraphs(
                    raw, chunk_size=self.cfg.chunk_size // 2, overlap=120
                )
                for i, c in enumerate(chunks):
                    if self.cfg.max_chunks is not None and chunk_id >= self.cfg.max_chunks:
                        return
                    yield Chunk(
                        chunk_id=chunk_id,
                        text=c,
                        metadata={
                            "source_type": "unreal_specifiers_dir",
                            "path": str(rel),
                            "title": title,
                            "chunk_index": i,
                        },
                    )
                    chunk_id += 1

    def build(self, *, force: bool = False) -> None:
        if faiss is None:
            raise ModuleNotFoundError(
                "faiss is not installed. Install faiss-cpu to build the vector index."
            )
        if self.cfg.vector_dir.exists() and not force:
            # If partial index exists, we’ll rebuild.
            if self.index_path.exists() and self.meta_path.exists():
                return
        self.cfg.vector_dir.mkdir(parents=True, exist_ok=True)

        # Stream build to avoid holding every chunk in memory.
        index: faiss.Index | None = None
        dim: int | None = None
        chunk_count = 0
        # Small batch keeps memory bounded and makes embedding batching efficient.
        batch_size = 16

        with open(self.meta_path, "w", encoding="utf-8") as meta_f:
            batch: List[Chunk] = []

            def flush_batch() -> None:
                nonlocal index, dim, chunk_count, batch
                if not batch:
                    return
                texts = [c.text for c in batch]
                # Sentences are L2-normalized so inner product == cosine similarity.
                vecs = self.embeddings.embed_documents(texts).astype("float32", copy=False)
                faiss.normalize_L2(vecs)
                if index is None:
                    dim = int(vecs.shape[1])
                    # IndexFlatIP + normalized vectors => cosine similarity retrieval.
                    index = faiss.IndexFlatIP(dim)
                index.add(vecs)
                # Persist metadata + short snippet only:
                # - keeps disk/memory lower
                # - good enough for “retrieved context snippets” in chat responses
                for c in batch:
                    snippet = c.text[:1200] if len(c.text) > 1200 else c.text
                    meta_f.write(
                        json.dumps(
                            {"chunk_id": c.chunk_id, "text": snippet, **c.metadata},
                            ensure_ascii=False,
                        )
                        + "\n"
                    )
                    chunk_count += 1
                batch = []

            for c in self._source_chunks():
                batch.append(c)
                if len(batch) >= batch_size:
                    flush_batch()

            flush_batch()

        if index is None or dim is None or chunk_count == 0:
            raise RuntimeError("No chunks embedded; vector store build failed.")

        faiss.write_index(index, str(self.index_path))

        with open(self.state_path, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "dim": dim,
                    "embedding_model": self.embeddings.config.model_name,
                    "chunk_size": self.cfg.chunk_size,
                    "chunk_overlap": self.cfg.chunk_overlap,
                    "chunks": chunk_count,
                },
                f,
                ensure_ascii=False,
                indent=2,
            )

        self._index = index
        self._meta = []
        self._load_meta()

    def load_or_build(self, *, force: bool = False) -> None:
        if not self.load() or force:
            self.build(force=force)

    def search(self, query_embedding: np.ndarray, top_k: int | None = None) -> List[Dict[str, Any]]:
        if self._index is None:
            raise RuntimeError("VectorStore is not loaded.")
        if top_k is None:
            top_k = self.cfg.top_k

        q = query_embedding.astype("float32", copy=False)
        # Normalize query embedding so IndexFlatIP behaves like cosine similarity.
        faiss.normalize_L2(q.reshape(1, -1))

        scores, ids = self._index.search(q.reshape(1, -1), top_k)
        results: List[Dict[str, Any]] = []
        for score, chunk_id in zip(scores[0], ids[0]):
            if chunk_id < 0:
                continue
            meta = self._meta[chunk_id]
            meta_out = dict(meta)
            meta_out["score"] = float(score)
            results.append(meta_out)
        return results

