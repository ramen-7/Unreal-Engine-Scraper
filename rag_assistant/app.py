from __future__ import annotations

import os
import time
import uuid
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import gradio as gr

from .chat_storage import ChatStore
from .embeddings import EmbeddingConfig
from .rag_backend import RAGService


def _messages_to_chatbot_pairs(messages: List[Dict[str, Any]]) -> List[List[str]]:
    pairs: List[List[str]] = []
    last_user: Optional[str] = None
    for m in messages:
        role = m.get("role")
        content = m.get("content", "")
        if role == "user":
            last_user = content
        elif role == "assistant" and last_user is not None:
            pairs.append([last_user, content])
            last_user = None
    return pairs


def _compute_topic_id(chat_store: ChatStore, session_id: str, topic_new: bool) -> str:
    msgs = chat_store.get_messages(session_id)
    if topic_new:
        return uuid.uuid4().hex
    # Continue the latest topic id if present.
    for m in reversed(msgs):
        tid = m.get("topic_id")
        if tid:
            return tid
    return uuid.uuid4().hex


def _ensure_chat_loaded(chat_store: ChatStore, session_id: str) -> List[List[str]]:
    stored_messages = chat_store.get_messages(session_id)
    return _messages_to_chatbot_pairs(stored_messages)


def build_app() -> gr.Blocks:
    repo_root = Path(".").resolve()

    # Data roots are fixed: the assistant is tightly coupled to your scraped corpus.
    vector_dir = repo_root / "data" / "vectorstore"
    markdown_root = repo_root / "scraped_data" / "markdown_by_path"
    specifiers_jsonl = repo_root / "scraped_data" / "content" / "unreal_specifiers.jsonl"
    unreal_specifiers_root = repo_root / "unreal_specifiers"

    missing = []
    if not markdown_root.exists():
        missing.append(str(markdown_root))
    if not specifiers_jsonl.exists():
        missing.append(str(specifiers_jsonl))
    if not unreal_specifiers_root.exists():
        missing.append(str(unreal_specifiers_root))
    if missing:
        raise FileNotFoundError(
            "Missing required data in container working directory. "
            "Make sure `scraped_data/` and `unreal_specifiers/` exist under /app. "
            "Missing: " + ", ".join(missing)
        )

    embedding_cfg = EmbeddingConfig(
        model_name=os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
    )
    # Vectorstore rebuild is expensive, so keep it opt-in for deployment.
    force_rebuild = os.getenv("FORCE_REBUILD_VECTORSTORE", "0") == "1"

    # Memory safety defaults:
    # If the full vectorstore index build OOMs inside Docker, reduce chunk count.
    include_unreal_specifiers_dir = os.getenv("INCLUDE_UNREAL_SPECIFIERS_DIR", "0") == "1"
    chunk_size = int(os.getenv("VSTORE_CHUNK_SIZE", "2200"))
    chunk_overlap = int(os.getenv("VSTORE_CHUNK_OVERLAP", "200"))
    max_chunks_env = os.getenv("VSTORE_MAX_CHUNKS", "6000").strip()
    max_chunks = None if max_chunks_env.lower() in ("", "none", "null", "0") else int(max_chunks_env)

    # Sharded vectorstore (recommended for Docker/free-tier):
    # shard_strategy="sharded_by_path_level_1" => shard_key = rel.parts[1] (skip the constant top folder)
    shard_strategy = os.getenv("VSTORE_SHARD_STRATEGY", "sharded_by_path_level_1")
    shard_top_n = int(os.getenv("VSTORE_SHARD_TOP_N", "3"))
    shard_level_index = int(os.getenv("VSTORE_SHARD_LEVEL_INDEX", "1"))

    # RAG service load/build:
    rag = RAGService(
        vector_dir=vector_dir,
        markdown_root=markdown_root,
        specifiers_jsonl=specifiers_jsonl,
        unreal_specifiers_root=unreal_specifiers_root,
        include_unreal_specifiers_dir=include_unreal_specifiers_dir,
        embedding_config=embedding_cfg,
        force_rebuild_vectorstore=force_rebuild,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        max_chunks=max_chunks,
        shard_strategy=shard_strategy,
        shard_top_n=shard_top_n,
        shard_level_index=shard_level_index,
    )

    chat_store = ChatStore(repo_root / "data" / "chats")

    topic_threshold = float(os.getenv("TOPIC_SIM_THRESHOLD", "0.4"))
    top_k = int(os.getenv("RAG_TOP_K", "6"))

    def respond(
        message: str,
        chat_history: List[List[str]],
        request: gr.Request,
    ) -> Tuple[List[List[str]], str, str]:
        if chat_history is None:
            chat_history = []
        # Session id for persistence:
        # Gradio provides stable identifiers; if not present, we generate a UUID.
        session_id = getattr(request, "session_hash", None) or getattr(request, "client_hash", None) or uuid.uuid4().hex

        # Load stored history for prompt accuracy.
        stored_messages = chat_store.get_messages(session_id)
        if not chat_history and stored_messages:
            chat_history = _messages_to_chatbot_pairs(stored_messages)

        result = rag.answer(
            question=message,
            session_id=session_id,
            chat_store=chat_store,
            topic_threshold=topic_threshold,
            top_k=top_k,
        )

        # We compute a topic id so the chat store can keep “topic boundaries”
        # aligned with our embedding-based topic switching heuristic.
        topic_id = _compute_topic_id(chat_store, session_id, topic_new=result.topic_new)

        chat_store.append(session_id, role="user", content=message, topic_id=topic_id)
        chat_store.append(session_id, role="assistant", content=result.answer_text, topic_id=topic_id)

        updated_chat_history = chat_history + [[message, result.answer_text]]

        # UI requirement: show which provider/model was used for this answer.
        model_used = f"Model used: {result.provider_display}"
        topic_line = f"Topic new: {result.topic_new} (similarity={result.topic_similarity:.3f})"

        sources_lines: List[str] = []
        for r in result.retrieved:
            title = r.get("title") or "document"
            path = r.get("path") or ""
            snippet = r.get("snippet") or ""
            sources_lines.append(f"- {title} ({path})\n\n  {snippet}".rstrip())

        sources_md = (
            f"**{model_used}**\n\n"
            f"{topic_line}\n\n"
            f"**Retrieved context:**\n" + "\n".join(sources_lines)
        )

        return updated_chat_history, model_used, sources_md

    with gr.Blocks(title="Unreal Engine RAG Assistant") as demo:
        gr.Markdown("## Unreal Engine RAG Assistant")
        model_label = gr.Markdown("")
        sources_box = gr.Markdown("")

        chatbot = gr.Chatbot(label="Chat", show_copy_button=True)
        msg = gr.Textbox(label="Ask a question", placeholder="Example: How do I use MeshWarp for deformations?")
        send = gr.Button("Send")

        def on_send(message, chat_history, request: gr.Request):
            return respond(message, chat_history, request)

        # Hook submit + button.
        msg.submit(on_send, inputs=[msg, chatbot], outputs=[chatbot, model_label, sources_box], show_progress=True)
        send.click(on_send, inputs=[msg, chatbot], outputs=[chatbot, model_label, sources_box], show_progress=True)

        gr.Examples(
            examples=[
                "What is CLASS_ConfigDoNotCheckDefaults?",
                "How do I use Dataflow node MergeConvexHulls?",
                "How do I set up a Blueprint to handle replicated events?",
            ],
            inputs=msg,
        )

    return demo


if __name__ == "__main__":
    demo = build_app()
    # Public sharing off by default; only local container access.
    demo.queue().launch(
        server_name="0.0.0.0",
        server_port=int(os.getenv("PORT", "7860")),
        share=False,
    )

