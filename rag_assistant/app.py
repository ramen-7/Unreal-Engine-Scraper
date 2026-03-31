from __future__ import annotations

import os
import uuid
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import gradio as gr

from .chat_storage import ChatStore
from .embeddings import EmbeddingConfig
from .rag_backend import RAGService


def _stored_to_chatbot(messages: List[Dict[str, Any]]) -> List[Dict[str, str]]:
    out: List[Dict[str, str]] = []
    for m in messages:
        role = m.get("role", "user")
        content = m.get("content", "")
        if role in ("user", "assistant") and content:
            out.append({"role": role, "content": content})
    return out


def _compute_topic_id(chat_store: ChatStore, session_id: str, topic_new: bool) -> str:
    msgs = chat_store.get_messages(session_id)
    if topic_new:
        return uuid.uuid4().hex
    for m in reversed(msgs):
        tid = m.get("topic_id")
        if tid:
            return tid
    return uuid.uuid4().hex


def build_app() -> gr.Blocks:
    repo_root = Path(".").resolve()

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
    include_unreal_specifiers_dir = os.getenv("INCLUDE_UNREAL_SPECIFIERS_DIR", "0") == "1"
    chunk_size = int(os.getenv("VSTORE_CHUNK_SIZE", "2200"))
    chunk_overlap = int(os.getenv("VSTORE_CHUNK_OVERLAP", "200"))
    max_chunks_env = os.getenv("VSTORE_MAX_CHUNKS", "none").strip()
    max_chunks = None if max_chunks_env.lower() in ("", "none", "null", "0") else int(max_chunks_env)

    shard_strategy = os.getenv("VSTORE_SHARD_STRATEGY", "sharded_by_path_level_1")
    shard_top_n = int(os.getenv("VSTORE_SHARD_TOP_N", "5"))
    shard_level_index = int(os.getenv("VSTORE_SHARD_LEVEL_INDEX", "1"))

    rag = RAGService(
        vector_dir=vector_dir,
        markdown_root=markdown_root,
        specifiers_jsonl=specifiers_jsonl,
        unreal_specifiers_root=unreal_specifiers_root,
        include_unreal_specifiers_dir=include_unreal_specifiers_dir,
        embedding_config=embedding_cfg,
        force_rebuild_vectorstore=False,
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
        chat_history: List[Dict[str, str]],
        request: gr.Request,
    ) -> Tuple[List[Dict[str, str]], str, str]:
        if chat_history is None:
            chat_history = []

        session_id = getattr(request, "session_hash", None) or getattr(request, "client_hash", None) or uuid.uuid4().hex

        stored_messages = chat_store.get_messages(session_id)
        if not chat_history and stored_messages:
            chat_history = _stored_to_chatbot(stored_messages)

        result = rag.answer(
            question=message,
            session_id=session_id,
            chat_store=chat_store,
            topic_threshold=topic_threshold,
            top_k=top_k,
        )

        topic_id = _compute_topic_id(chat_store, session_id, topic_new=result.topic_new)

        chat_store.append(session_id, role="user", content=message, topic_id=topic_id)
        chat_store.append(session_id, role="assistant", content=result.answer_text, topic_id=topic_id)

        chat_history = chat_history + [
            {"role": "user", "content": message},
            {"role": "assistant", "content": result.answer_text},
        ]

        model_line = f"**{result.provider_display}** | Topic new: {result.topic_new} (sim={result.topic_similarity:.3f})"

        sources_parts: List[str] = []
        for r in result.retrieved:
            title = r.get("title") or "document"
            path = r.get("path") or ""
            score = r.get("score")
            snippet = (r.get("snippet") or "")[:300]
            score_str = f" ({score:.3f})" if score is not None else ""
            sources_parts.append(
                f"### {title}{score_str}\n"
                f"`{path}`\n\n"
                f"{snippet}{'...' if len(r.get('snippet', '')) > 300 else ''}"
            )

        sources_md = "\n\n---\n\n".join(sources_parts) if sources_parts else "*No documents retrieved*"

        return chat_history, model_line, sources_md

    css = """
    .source-panel { max-height: 70vh; overflow-y: auto; }
    """

    with gr.Blocks(title="Unreal Engine RAG Assistant", css=css) as demo:
        gr.Markdown("# Unreal Engine RAG Assistant")
        model_label = gr.Markdown("")

        with gr.Row(equal_height=True):
            with gr.Column(scale=1):
                chatbot = gr.Chatbot(label="Chat", height=500)
                with gr.Row():
                    msg = gr.Textbox(
                        label="Ask a question",
                        placeholder="e.g. How do I use MeshWarp for deformations?",
                        scale=4,
                    )
                    send = gr.Button("Send", scale=1, variant="primary")

            with gr.Column(scale=1):
                sources_box = gr.Markdown(
                    value="*Ask a question to see retrieved documents here.*",
                    label="Retrieved Documents",
                    elem_classes=["source-panel"],
                )

        def on_send(message, chat_history, request: gr.Request):
            history, model_md, sources_md = respond(message, chat_history, request)
            return history, model_md, sources_md, ""

        msg.submit(on_send, inputs=[msg, chatbot], outputs=[chatbot, model_label, sources_box, msg])
        send.click(on_send, inputs=[msg, chatbot], outputs=[chatbot, model_label, sources_box, msg])

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
    demo.queue().launch(
        server_name="0.0.0.0",
        server_port=int(os.getenv("PORT", "7860")),
        share=False,
    )
