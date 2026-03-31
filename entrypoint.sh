#!/usr/bin/env bash
set -e

if [[ "${FORCE_REBUILD_VECTORSTORE:-0}" == "1" ]] || [[ ! -f data/vectorstore/router.faiss.index ]]; then
    echo "=== Building vectorstore (lean process) ==="
    python -m rag_assistant.build
    echo "=== Vectorstore build finished ==="
fi

echo "=== Starting Gradio app ==="
exec python -m rag_assistant.app
