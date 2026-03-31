"""Standalone vectorstore build script.

Imports only embeddings + faiss + sharded vectorstore -- avoids loading
Gradio, OpenAI, Google AI, sklearn, etc. which saves ~2-3GB of RAM.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path


def main() -> None:
    repo_root = Path(".").resolve()

    vector_dir = repo_root / "data" / "vectorstore"
    markdown_root = repo_root / "scraped_data" / "markdown_by_path"
    specifiers_jsonl = repo_root / "scraped_data" / "content" / "unreal_specifiers.jsonl"
    unreal_specifiers_root = repo_root / "unreal_specifiers"

    from .embeddings import EmbeddingConfig, LocalEmbeddings
    from .sharded_vectorstore import ShardedVectorStore, ShardedVectorStoreConfig

    embedding_cfg = EmbeddingConfig(
        model_name=os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
    )
    include_unreal_specifiers_dir = os.getenv("INCLUDE_UNREAL_SPECIFIERS_DIR", "0") == "1"
    chunk_size = int(os.getenv("VSTORE_CHUNK_SIZE", "2200"))
    chunk_overlap = int(os.getenv("VSTORE_CHUNK_OVERLAP", "200"))
    max_chunks_env = os.getenv("VSTORE_MAX_CHUNKS", "none").strip()
    max_chunks = None if max_chunks_env.lower() in ("", "none", "null", "0") else int(max_chunks_env)
    shard_top_n = int(os.getenv("VSTORE_SHARD_TOP_N", "5"))
    shard_level_index = int(os.getenv("VSTORE_SHARD_LEVEL_INDEX", "1"))
    force_rebuild = os.getenv("FORCE_REBUILD_VECTORSTORE", "0") == "1"

    print(f"[build] vector_dir={vector_dir}", flush=True)
    print(f"[build] markdown_root={markdown_root} (exists={markdown_root.exists()})", flush=True)
    print(f"[build] force_rebuild={force_rebuild}, max_chunks={max_chunks}", flush=True)

    embeddings = LocalEmbeddings(embedding_cfg)

    cfg = ShardedVectorStoreConfig(
        vector_dir=vector_dir,
        markdown_root=markdown_root,
        specifiers_jsonl=specifiers_jsonl,
        unreal_specifiers_root=unreal_specifiers_root,
        include_unreal_specifiers_dir=include_unreal_specifiers_dir,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        shard_level_index=shard_level_index,
        shard_top_n=shard_top_n,
        max_chunks=max_chunks,
    )
    store = ShardedVectorStore(cfg, embeddings=embeddings)
    store.load_or_build(force_rebuild=force_rebuild)
    print("[build] Vectorstore build complete.", flush=True)


if __name__ == "__main__":
    main()
