from __future__ import annotations

import gc
import json
import logging
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional, Tuple

import numpy as np
from bs4 import BeautifulSoup

try:
    import faiss  # type: ignore
except ModuleNotFoundError:  # local dev without faiss
    faiss = None  # type: ignore

from .embeddings import LocalEmbeddings

log = logging.getLogger(__name__)


@dataclass(frozen=True)
class ShardedVectorStoreConfig:
    vector_dir: Path
    markdown_root: Path
    specifiers_jsonl: Path
    unreal_specifiers_root: Path
    include_unreal_specifiers_dir: bool = False

    # Chunking / indexing
    chunk_size: int = 2200
    chunk_overlap: int = 200

    # Sharding strategy for markdown tree:
    # shard_key = rel.parts[shard_level_index] if it exists, else rel.parts[0]
    # Using level_index=1 avoids the top constant folder like
    # "Unreal Engine 5.7 Documentation".
    shard_level_index: int = 1

    # How many shards to search per query.
    shard_top_n: int = 3

    # Optional safety limit:
    # If set, only embed/build up to this many total chunks across all shards.
    max_chunks: int | None = None


@dataclass(frozen=True)
class ShardCandidate:
    shard_key: str
    score: float


class ShardedVectorStore:
    """
    Sharded FAISS index that avoids OOM:
    - router index: 1 vector per shard (mean embedding)
    - shard indexes: chunk-level FAISS per shard, built sequentially
    - at query time: load only top-N shards and search inside them
    """

    def __init__(
        self,
        cfg: ShardedVectorStoreConfig,
        embeddings: LocalEmbeddings,
        *,
        shard_cache_size: int = 2,
    ):
        if faiss is None:
            raise ModuleNotFoundError(
                "faiss is not installed. Install faiss-cpu to use ShardedVectorStore."
            )

        self.cfg = cfg
        self.embeddings = embeddings

        self.router_index_path = cfg.vector_dir / "router.faiss.index"
        self.router_meta_path = cfg.vector_dir / "router_metadata.jsonl"

        self.shards_root = cfg.vector_dir / "shards"
        self.shards_root.mkdir(parents=True, exist_ok=True)

        self._router_index: faiss.Index | None = None
        self._router_meta: List[Dict[str, Any]] = []

        # Simple LRU-ish cache: {shard_key: shard_index_and_meta}
        self._shard_cache: Dict[str, Tuple[faiss.Index, List[Dict[str, Any]]]] = {}
        self._shard_cache_order: List[str] = []
        self._shard_cache_size = shard_cache_size

    def _read_text(self, p: Path) -> str:
        return p.read_text(encoding="utf-8", errors="replace")

    def _clean_markdown(self, text: str) -> str:
        if "<" in text and ">" in text:
            soup = BeautifulSoup(text, "html.parser")
            return soup.get_text("\n").strip()
        return text.strip()

    def _chunk_text_by_paragraphs(self, text: str) -> List[str]:
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
        chunk_size = self.cfg.chunk_size
        overlap = self.cfg.chunk_overlap
        while i < len(paragraphs):
            p = paragraphs[i]
            if buf_len + len(p) + 2 > chunk_size and buf:
                flush()
                if overlap > 0:
                    # Keep a small tail of previous paragraphs (heuristic).
                    tail = paragraphs[max(0, i - 3) : i]
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
        return [c for c in chunks if len(c.strip()) >= 80]

    def _iter_markdown_files_by_top_segment(self) -> Iterator[Tuple[str, Path]]:
        # Top segment is the first directory under markdown_root.
        # Example: markdown_by_path/Unreal Engine 5.7 Documentation/What's New/Beta Features.md
        # => shard_key = "Unreal Engine 5.7 Documentation"
        for p in self.cfg.markdown_root.rglob("*.md"):
            if not p.is_file():
                continue
            rel = p.relative_to(self.cfg.markdown_root)
            if not rel.parts:
                continue
            if len(rel.parts) > self.cfg.shard_level_index:
                shard_key = rel.parts[self.cfg.shard_level_index]
            else:
                shard_key = rel.parts[0]
            yield shard_key, p

    def _iter_unreal_specifiers_by_shard(self) -> Iterator[Tuple[str, Path]]:
        # Shard by top folder under unreal_specifiers_root.
        root = self.cfg.unreal_specifiers_root
        if not root.exists():
            return
        for p in root.rglob("*.md"):
            if not p.is_file():
                continue
            rel = p.relative_to(root)
            if not rel.parts:
                continue
            shard_key = rel.parts[0]
            yield shard_key, p

    def _iter_specifiers_jsonl_by_shard(self) -> Iterator[Tuple[str, Dict[str, Any]]]:
        # Shard by `category` (fallback: "Unknown").
        if not self.cfg.specifiers_jsonl.exists():
            return
        with open(self.cfg.specifiers_jsonl, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                obj = json.loads(line)
                shard_key = obj.get("category") or obj.get("source") or "Unknown"
                yield shard_key, obj

    def _load_router(self) -> bool:
        if not self.router_index_path.exists() or not self.router_meta_path.exists():
            return False
        idx = faiss.read_index(str(self.router_index_path))
        self._router_index = idx
        meta: List[Dict[str, Any]] = []
        with open(self.router_meta_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                meta.append(json.loads(line))
        self._router_meta = meta
        return True

    def _load_shard(self, shard_key: str) -> Tuple[faiss.Index, List[Dict[str, Any]]]:
        # Cache lookup
        if shard_key in self._shard_cache:
            # Refresh order (simple LRU)
            self._shard_cache_order.remove(shard_key)
            self._shard_cache_order.append(shard_key)
            return self._shard_cache[shard_key]

        shard_dir = self.shards_root / shard_key
        index_path = shard_dir / "faiss.index"
        meta_path = shard_dir / "metadata.jsonl"
        idx = faiss.read_index(str(index_path))
        meta: List[Dict[str, Any]] = []
        with open(meta_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                meta.append(json.loads(line))

        self._shard_cache[shard_key] = (idx, meta)
        self._shard_cache_order.append(shard_key)
        if len(self._shard_cache_order) > self._shard_cache_size:
            old = self._shard_cache_order.pop(0)
            self._shard_cache.pop(old, None)
        return idx, meta

    def load_or_build(self, *, force_rebuild: bool = False) -> None:
        if not force_rebuild and self._load_router():
            return
        self.build(force_rebuild=force_rebuild)

    def build(self, *, force_rebuild: bool = False) -> None:
        vector_dir = self.cfg.vector_dir
        vector_dir.mkdir(parents=True, exist_ok=True)
        self.shards_root.mkdir(parents=True, exist_ok=True)

        if force_rebuild:
            if vector_dir.exists():
                for p in vector_dir.glob("router.*"):
                    p.unlink(missing_ok=True)
            if self.shards_root.exists():
                for p in self.shards_root.glob("*"):
                    if p.is_dir():
                        for fp in p.rglob("*"):
                            if fp.is_file():
                                fp.unlink(missing_ok=True)
                        p.rmdir()

        router_index: faiss.Index | None = None
        router_meta: List[Dict[str, Any]] = []

        markdown_files = list(self._iter_markdown_files_by_top_segment())
        shard_keys = sorted({k for k, _ in markdown_files})

        if self.cfg.include_unreal_specifiers_dir:
            shard_keys += [k for k, _ in self._iter_unreal_specifiers_by_shard()]
            shard_keys = sorted(set(shard_keys))

        spec_shards = set()
        for k, _obj in self._iter_specifiers_jsonl_by_shard():
            spec_shards.add(k)
        shard_keys = sorted(set(shard_keys) | spec_shards)

        total_shards = len(shard_keys)
        log.info("Discovered %d shard keys to build", total_shards)

        total_embedded = 0
        batch_size = 32

        for shard_idx, shard_key in enumerate(shard_keys):
            if self.cfg.max_chunks is not None and total_embedded >= self.cfg.max_chunks:
                log.info("Reached max_chunks=%d, stopping build", self.cfg.max_chunks)
                break

            log.info(
                "[%d/%d] Building shard '%s' (total chunks so far: %d)",
                shard_idx + 1, total_shards, shard_key, total_embedded,
            )

            try:
                mean_vec, shard_meta_rows, chunks_in_shard = self._build_one_shard(
                    shard_key, markdown_files, batch_size, total_embedded,
                )
            except MemoryError:
                log.error(
                    "MemoryError while building shard '%s' (embedded %d chunks so far). "
                    "Saving partial router and exiting with code 137.",
                    shard_key, total_embedded,
                )
                self._save_router(router_index, router_meta)
                sys.exit(137)

            total_embedded += chunks_in_shard

            if mean_vec is None or chunks_in_shard == 0:
                log.info("  Shard '%s' produced 0 chunks, skipping", shard_key)
                continue

            if router_index is None:
                dim = int(mean_vec.shape[1])
                router_index = faiss.IndexFlatIP(dim)

            router_index.add(mean_vec)
            router_meta.append({"shard_key": shard_key})
            log.info("  Shard '%s' done: %d chunks", shard_key, chunks_in_shard)

            gc.collect()

        if router_index is None:
            raise RuntimeError("ShardedVectorStore build produced no router index (no chunks embedded).")

        self._save_router(router_index, router_meta)
        self._router_index = router_index
        self._router_meta = router_meta

        log.info(
            "Build complete: %d shards, %d total chunks",
            len(router_meta), total_embedded,
        )

    def _save_router(
        self,
        router_index: Optional[faiss.Index],
        router_meta: List[Dict[str, Any]],
    ) -> None:
        if router_index is None:
            return
        faiss.write_index(router_index, str(self.router_index_path))
        with open(self.router_meta_path, "w", encoding="utf-8") as f:
            for row in router_meta:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")

    def _build_one_shard(
        self,
        shard_key: str,
        markdown_files: List[Tuple[str, Path]],
        batch_size: int,
        total_embedded_before: int,
    ) -> Tuple[Optional[np.ndarray], List[Dict[str, Any]], int]:
        """Build a single shard's FAISS index and metadata. Returns (mean_vec, meta_rows, chunk_count)."""
        shard_dir = self.shards_root / shard_key
        shard_dir.mkdir(parents=True, exist_ok=True)
        shard_index_path = shard_dir / "faiss.index"
        shard_meta_path = shard_dir / "metadata.jsonl"

        shard_index: faiss.Index | None = None
        shard_dim: int | None = None
        shard_meta: List[Dict[str, Any]] = []
        sum_vec: np.ndarray | None = None
        count: int = 0
        total_embedded = total_embedded_before

        def add_batch(vecs: np.ndarray, chunk_rows: List[Dict[str, Any]]) -> None:
            nonlocal shard_index, shard_dim, shard_meta, sum_vec, count, total_embedded
            if shard_index is None:
                shard_dim = int(vecs.shape[1])
                shard_index = faiss.IndexFlatIP(shard_dim)
            shard_index.add(vecs)
            shard_meta.extend(chunk_rows)
            if sum_vec is None:
                sum_vec = vecs.sum(axis=0).astype("float32", copy=False)
            else:
                sum_vec += vecs.sum(axis=0).astype("float32", copy=False)
            count += vecs.shape[0]
            total_embedded += vecs.shape[0]

        texts_batch: List[str] = []
        rows_batch: List[Dict[str, Any]] = []

        def flush_batch() -> None:
            nonlocal texts_batch, rows_batch
            if not texts_batch:
                return
            vecs = self.embeddings.embed_documents(texts_batch)
            vecs = vecs.astype("float32", copy=False)
            faiss.normalize_L2(vecs)
            add_batch(vecs, rows_batch)
            texts_batch = []
            rows_batch = []

        max_chunks = self.cfg.max_chunks

        for key, p in markdown_files:
            if key != shard_key:
                continue
            rel = p.relative_to(self.cfg.markdown_root)
            title = rel.parts[-1].rsplit(".", 1)[0]
            raw = self._clean_markdown(self._read_text(p))
            if len(raw) < 80:
                continue
            chunks = self._chunk_text_by_paragraphs(raw)
            for i, c in enumerate(chunks):
                if max_chunks is not None and total_embedded >= max_chunks:
                    break
                texts_batch.append(c)
                rows_batch.append({
                    "source_type": "markdown",
                    "path": str(rel),
                    "title": title,
                    "chunk_index": i,
                    "text": c[:1200],
                })
                if len(texts_batch) >= batch_size:
                    flush_batch()
            if max_chunks is not None and total_embedded >= max_chunks:
                break

        if total_embedded < (max_chunks or 10**18):
            for key, obj in self._iter_specifiers_jsonl_by_shard():
                if key != shard_key:
                    continue
                text = self._clean_markdown(obj.get("content") or "")
                if len(text) < 80:
                    continue
                chunks = self._chunk_text_by_paragraphs(text)[:40]
                if not chunks:
                    chunks = [text]
                for i, c in enumerate(chunks):
                    if max_chunks is not None and total_embedded >= max_chunks:
                        break
                    texts_batch.append(c)
                    rows_batch.append({
                        "source_type": "specifier",
                        "path": str(obj.get("path") or obj.get("title") or "unreal_specifiers"),
                        "title": obj.get("title") or "",
                        "chunk_index": i,
                        "category": obj.get("category") or "",
                        "source": obj.get("source") or "UnrealSpecifiers",
                        "text": c[:1200],
                    })
                    if len(texts_batch) >= batch_size:
                        flush_batch()
                if max_chunks is not None and total_embedded >= max_chunks:
                    break

        if self.cfg.include_unreal_specifiers_dir and total_embedded < (max_chunks or 10**18):
            for key, p in self._iter_unreal_specifiers_by_shard():
                if key != shard_key:
                    continue
                rel = p.relative_to(self.cfg.unreal_specifiers_root)
                title = rel.parts[-1].rsplit(".", 1)[0]
                raw = self._clean_markdown(self._read_text(p))
                if len(raw) < 80:
                    continue
                chunks = self._chunk_text_by_paragraphs(raw)
                for i, c in enumerate(chunks):
                    if max_chunks is not None and total_embedded >= max_chunks:
                        break
                    texts_batch.append(c)
                    rows_batch.append({
                        "source_type": "unreal_specifiers_dir",
                        "path": str(rel),
                        "title": title,
                        "chunk_index": i,
                        "text": c[:1200],
                    })
                    if len(texts_batch) >= batch_size:
                        flush_batch()
                if max_chunks is not None and total_embedded >= max_chunks:
                    break

        flush_batch()

        chunks_in_shard = count

        if shard_index is None or not shard_meta:
            return None, [], 0

        faiss.write_index(shard_index, str(shard_index_path))
        with open(shard_meta_path, "w", encoding="utf-8") as f:
            for row in shard_meta:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")

        mean_vec = (sum_vec / float(count)).astype("float32", copy=False).reshape(1, -1)
        faiss.normalize_L2(mean_vec)

        del shard_index, shard_meta, texts_batch, rows_batch
        gc.collect()

        return mean_vec, [], chunks_in_shard

    def _top_shards(self, q_emb: np.ndarray) -> List[ShardCandidate]:
        if self._router_index is None:
            ok = self._load_router()
            if not ok:
                raise RuntimeError("Router index not found; build the sharded vectorstore first.")
        idx = self._router_index
        assert idx is not None

        # Normalize for cosine similarity.
        q = q_emb.astype("float32", copy=False).reshape(1, -1)
        faiss.normalize_L2(q)

        top_n = max(1, self.cfg.shard_top_n)
        k = min(top_n, len(self._router_meta))
        scores, ids = idx.search(q, k)

        out: List[ShardCandidate] = []
        for score, shard_local_id in zip(scores[0], ids[0]):
            if shard_local_id < 0:
                continue
            shard_key = self._router_meta[int(shard_local_id)]["shard_key"]
            out.append(ShardCandidate(shard_key=shard_key, score=float(score)))
        return out

    def search(self, query_embedding: np.ndarray, top_k: int = 6) -> List[Dict[str, Any]]:
        candidates = self._top_shards(query_embedding)
        if not candidates:
            return []

        # Distribute retrieval across shards (simple merge).
        per_shard = max(1, int(np.ceil(top_k / float(len(candidates)))))
        merged: List[Dict[str, Any]] = []

        # Normalize query embedding once.
        q = query_embedding.astype("float32", copy=False).reshape(1, -1)
        faiss.normalize_L2(q)

        for c in candidates:
            shard_index, shard_meta = self._load_shard(c.shard_key)
            scores, ids = shard_index.search(q, per_shard)
            for score, local_id in zip(scores[0], ids[0]):
                if local_id < 0:
                    continue
                meta = dict(shard_meta[int(local_id)])
                meta["score"] = float(score)
                meta["shard_score"] = c.score
                merged.append(meta)

        # Sort by chunk score.
        merged.sort(key=lambda x: x.get("score", -1e9), reverse=True)
        return merged[:top_k]

