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
        fits = buf_len + len(p) + 2 <= chunk_size
        if fits:
            buf.append(p)
            buf_len += len(p) + 2
            i += 1
            continue
        if buf:
            flush()
            if overlap > 0:
                tail = paragraphs[max(0, i - 3) : i]
                for t in tail:
                    if buf_len + len(t) + 2 > overlap:
                        break
                    buf.append(t)
                    buf_len += len(t) + 2
            if buf_len + len(p) + 2 <= chunk_size:
                continue
            flush()
        for start in range(0, len(p), chunk_size):
            chunks.append(p[start : start + chunk_size])
        i += 1

    flush()
    return [c for c in chunks if len(c.strip()) >= 80]


def _clean_markdown(text: str) -> str:
    if "<" in text and ">" in text:
        soup = BeautifulSoup(text, "html.parser")
        return soup.get_text("\n").strip()
    return text.strip()


@dataclass(frozen=True)
class VectorStoreConfig:
    vector_dir: Path
    markdown_root: Path
    specifiers_jsonl: Path
    unreal_specifiers_root: Path
    include_unreal_specifiers_dir: bool = True

    chunk_size: int = 1400
    chunk_overlap: int = 200

    top_k: int = 6

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
            if self.index_path.exists() and self.meta_path.exists():
                return
        self.cfg.vector_dir.mkdir(parents=True, exist_ok=True)

        index: faiss.Index | None = None
        dim: int | None = None
        chunk_count = 0
        batch_size = 16

        with open(self.meta_path, "w", encoding="utf-8") as meta_f:
            batch: List[Chunk] = []

            def flush_batch() -> None:
                nonlocal index, dim, chunk_count, batch
                if not batch:
                    return
                texts = [c.text for c in batch]
                vecs = self.embeddings.embed_documents(texts).astype("float32", copy=False)
                faiss.normalize_L2(vecs)
                if index is None:
                    dim = int(vecs.shape[1])
                    index = faiss.IndexFlatIP(dim)
                index.add(vecs)
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
