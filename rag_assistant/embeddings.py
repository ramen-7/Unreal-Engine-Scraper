from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from typing import Iterable, List

import numpy as np
from sentence_transformers import SentenceTransformer


@dataclass(frozen=True)
class EmbeddingConfig:
    # Immutable config: prevents accidental changes to embedding model selection at runtime.
    # If the config changes, you typically rebuild the vectorstore/index.
    #
    # Small + fast embedding model for local RAG.
    model_name: str = "sentence-transformers/all-MiniLM-L6-v2"


@lru_cache(maxsize=1)
def _get_model(model_name: str) -> SentenceTransformer:
    # Cache the (heavy) SentenceTransformer model in-process.
    # This avoids re-downloading/re-instantiating on every request.
    return SentenceTransformer(model_name)


class LocalEmbeddings:
    def __init__(self, config: EmbeddingConfig | None = None):
        # Keep embedding model choice centralized via EmbeddingConfig.
        self.config = config or EmbeddingConfig()
        self.model = _get_model(self.config.model_name)

    def embed_documents(self, texts: Iterable[str]) -> np.ndarray:
        # normalize_embeddings=True + later FAISS inner product gives cosine similarity.
        vecs = self.model.encode(
            list(texts),
            normalize_embeddings=True,
            convert_to_numpy=True,
            show_progress_bar=True,
        )
        return vecs.astype("float32", copy=False)

    def embed_query(self, text: str) -> np.ndarray:
        vec = self.model.encode(
            [text],
            normalize_embeddings=True,
            convert_to_numpy=True,
            show_progress_bar=False,
        )[0]
        return vec.astype("float32", copy=False)

    def cosine_similarity(self, a: np.ndarray, b: np.ndarray) -> float:
        # With normalized embeddings, dot product == cosine similarity.
        return float(np.dot(a, b))

