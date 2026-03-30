from __future__ import annotations

import os
import time
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from .chat_storage import ChatStore
from .embeddings import EmbeddingConfig, LocalEmbeddings
from .providers import LLMClient, ProviderRouter
from .vectorstore import VectorStore, VectorStoreConfig
from .sharded_vectorstore import ShardedVectorStore, ShardedVectorStoreConfig


DEFAULT_SYSTEM_PROMPT = (
    "You are an expert Unreal Engine software engineer helping out a fellow collegaue. "
    "Answer the user's question using ONLY the provided retrieved context. "
    "If the answer is not in the context, say you don't know. "
    "Be concise and accurate. Include short citations as (source) using the provided source paths."
)


def _build_chat_history_for_prompt(messages: List[Dict[str, Any]], *, max_turns: int = 6) -> str:
    # Keep formatting stable for the LLM: alternating roles.
    relevant = messages[-max_turns * 2 :]
    lines: List[str] = []
    for m in relevant:
        role = m.get("role", "user")
        content = m.get("content", "")
        if not content:
            continue
        lines.append(f"{role.upper()}: {content}")
    return "\n".join(lines).strip()


@dataclass(frozen=True)
class RetrievalResult:
    # Immutable result:
    # - stable response metadata for the Gradio UI
    # - safe to pass between functions without accidental mutation
    answer_text: str
    provider_display: str
    provider_model: str
    retrieved: List[Dict[str, Any]]
    topic_new: bool
    topic_similarity: float


class RAGService:
    def __init__(
        self,
        *,
        vector_dir: Path,
        markdown_root: Path,
        specifiers_jsonl: Path,
        unreal_specifiers_root: Path,
        include_unreal_specifiers_dir: bool = True,
        embedding_config: EmbeddingConfig | None = None,
        force_rebuild_vectorstore: bool = False,
        chunk_size: int = 1400,
        chunk_overlap: int = 200,
        max_chunks: int | None = None,
        shard_strategy: str = "none",
        shard_top_n: int = 3,
        shard_level_index: int = 1,
    ):
        self.embeddings = LocalEmbeddings(embedding_config)

        # Vectorstore strategy:
        # - none: single monolithic FAISS index (fast to query but can OOM while building)
        # - sharded_by_path_level_*: build a router + shard FAISS indexes and only search top shards
        if shard_strategy.startswith("sharded"):
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
            self.vectorstore = ShardedVectorStore(cfg, embeddings=self.embeddings)
            self.vectorstore.load_or_build(force_rebuild=force_rebuild_vectorstore)  # type: ignore[attr-defined]
        else:
            self.vectorstore = VectorStore(
                VectorStoreConfig(
                    vector_dir=vector_dir,
                    markdown_root=markdown_root,
                    specifiers_jsonl=specifiers_jsonl,
                    unreal_specifiers_root=unreal_specifiers_root,
                    include_unreal_specifiers_dir=include_unreal_specifiers_dir,
                    chunk_size=chunk_size,
                    chunk_overlap=chunk_overlap,
                    max_chunks=max_chunks,
                ),
                embeddings=self.embeddings,
            )
            self.vectorstore.load_or_build(force=force_rebuild_vectorstore)

        state_path = Path("data") / "provider_state.json"
        self.router = ProviderRouter(state_path)
        self.llm = LLMClient(self.router)

    def _is_new_topic(
        self,
        *,
        question: str,
        stored_messages: List[Dict[str, Any]],
        recent_n_messages: int = 4,
        threshold: float = 0.4,
    ) -> Tuple[bool, float]:
        # “New topic” heuristic:
        # Compare the embedding of the new question to the embedding of recent
        # chat context; low cosine similarity => reset context for prompt.
        if len(stored_messages) < 2:
            return False, 1.0

        recent = stored_messages[-recent_n_messages:]
        recent_text = " ".join(m.get("content", "") for m in recent if m.get("content"))
        if not recent_text.strip():
            return False, 1.0

        q_emb = self.embeddings.embed_query(question)
        ctx_emb = self.embeddings.embed_query(recent_text)

        # Embeddings are normalized, so cosine_similarity is stable.
        sim = float(cosine_similarity([q_emb], [ctx_emb])[0][0])
        return sim < threshold, sim

    def answer(
        self,
        *,
        question: str,
        session_id: str,
        chat_store: ChatStore,
        max_context_turns: int = 4,
        topic_recent_n_messages: int = 4,
        topic_threshold: float = 0.4,
        top_k: int = 6,
        system_prompt: str = DEFAULT_SYSTEM_PROMPT,
    ) -> RetrievalResult:
        # Main RAG pipeline:
        # 1) load persisted chat history
        # 2) detect new topic (embedding similarity)
        # 3) retrieve top-k chunks from vector store
        # 4) build a prompt that forces the model to answer from retrieved context
        # 5) call the LLM provider router (Gemini->OpenAI failover)
        stored = chat_store.get_messages(session_id)

        topic_new, sim = self._is_new_topic(
            question=question,
            stored_messages=stored,
            recent_n_messages=topic_recent_n_messages,
            threshold=topic_threshold,
        )

        prompt_messages = [] if topic_new else stored[-max_context_turns * 2 :]
        # We only include chat history when the question is still on the same topic.
        prompt_history = _build_chat_history_for_prompt(prompt_messages, max_turns=max_context_turns)

        q_emb = self.embeddings.embed_query(question)
        retrieved = self.vectorstore.search(q_emb, top_k=top_k)

        # Assemble a prompt with retrieved context + citations.
        context_blocks: List[str] = []
        for i, r in enumerate(retrieved, start=1):
            # Context blocks are enumerated so the LLM can refer to “(1)”, “(2)”, etc.
            title = r.get("title") or r.get("path") or "document"
            path = r.get("path") or ""
            text = (r.get("text") or "").strip()
            text = text[:1800]
            context_blocks.append(f"[{i}] {title} ({path})\n{text}")

        retrieved_preview = [
            {
                "rank": idx + 1,
                "title": r.get("title"),
                "path": r.get("path"),
                "snippet": (r.get("text") or "")[:500],
                "score": r.get("score"),
            }
            for idx, r in enumerate(retrieved)
        ]

        user_prompt = (
            f"USER QUESTION:\n{question}\n\n"
            f"RETRIEVED CONTEXT:\n\n" + "\n\n".join(context_blocks) + "\n\n"
            f"CHAT HISTORY (only when same topic):\n{prompt_history if prompt_history else '[none]'}\n\n"
            "Answer now."
        )

        answer_text, sel = self.llm.generate(system_prompt=system_prompt, user_prompt=user_prompt)
        # Provider router returns the model actually used; UI displays it.

        provider_model = sel.model
        provider_display = sel.display_name

        return RetrievalResult(
            answer_text=answer_text.strip(),
            provider_display=provider_display,
            provider_model=provider_model,
            retrieved=retrieved_preview,
            topic_new=topic_new,
            topic_similarity=sim,
        )

