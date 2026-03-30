from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Tuple


@dataclass(frozen=True)
class StoredMessage:
    # This dataclass currently serves as a typed schema for messages.
    # frozen=True keeps it immutable and prevents accidental edits after creation.
    role: str  # "user" | "assistant" | maybe system
    content: str
    ts: float
    topic_id: str | None = None


class ChatStore:
    def __init__(self, base_dir: Path):
        # Persistent-on-disk storage:
        # - simple JSON per session_id
        # - good enough for free-tier hosting and local development
        self.base_dir = base_dir
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def _path(self, session_id: str) -> Path:
        # Ensure we never allow path traversal:
        # we keep only alnum + "-" "_" and cap length.
        safe = "".join(ch for ch in session_id if ch.isalnum() or ch in ("-", "_"))[:120]
        return self.base_dir / f"{safe}.json"

    def load(self, session_id: str) -> Dict[str, Any]:
        p = self._path(session_id)
        if not p.exists():
            return {"session_id": session_id, "messages": []}
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            return {"session_id": session_id, "messages": []}

    def append(
        self,
        session_id: str,
        *,
        role: str,
        content: str,
        topic_id: str | None,
    ) -> None:
        # Append by reloading and rewriting the full JSON file.
        # For small chat histories this is simplest and reliable.
        data = self.load(session_id)
        data.setdefault("messages", [])
        data["messages"].append(
            {
                "role": role,
                "content": content,
                "ts": time.time(),
                "topic_id": topic_id,
            }
        )
        p = self._path(session_id)
        p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    def get_messages(self, session_id: str) -> List[Dict[str, Any]]:
        return self.load(session_id).get("messages", [])

