from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional, Tuple


class ProviderError(RuntimeError):
    pass


@dataclass(frozen=True)
class ProviderSelection:
    # Immutable selection object:
    # - ensures the “which provider/model did we use” metadata stays consistent
    # - safe to store alongside chat logs/retrieval results
    provider: str  # "gemini" | "openai"
    model: str
    display_name: str


def _is_quota_or_block_error(msg: str) -> bool:
    # Provider failover heuristic:
    # We treat quota/rate-limit-like errors as “Gemini free tier exhausted”, then
    # permanently switch to OpenAI.
    m = msg.lower()
    return any(
        k in m
        for k in [
            "quota",
            "rate limit",
            "429",
            "too many requests",
            "insufficient",
            "not authorized",
            "forbidden",
            "blocked",
            "temporarily unavailable",
            "daily limit",
        ]
    )


class ProviderRouter:
    def __init__(
        self,
        state_path: Path,
        *,
        gemini_free_hours: float = 24.0,
        openai_model: str = "gpt-4o-mini",
        gemini_model: str = "gemini-1.5-flash",
    ):
        self.state_path = state_path
        self.gemini_free_hours = gemini_free_hours
        self.openai_model = openai_model
        self.gemini_model = gemini_model

        self.state_path.parent.mkdir(parents=True, exist_ok=True)

    def _load_state(self) -> Dict[str, Any]:
        if not self.state_path.exists():
            return {}
        try:
            return json.loads(self.state_path.read_text(encoding="utf-8"))
        except Exception:
            return {}

    def _save_state(self, st: Dict[str, Any]) -> None:
        self.state_path.write_text(json.dumps(st, ensure_ascii=False, indent=2), encoding="utf-8")

    def select(self) -> ProviderSelection:
        # Time-based window:
        # Gemini is used for a fixed time budget, then we switch to OpenAI.
        # (This is “free-tier for a day” behavior.)
        st = self._load_state()
        now = time.time()

        # Initialize gemini window.
        if "gemini_until_ts" not in st and st.get("provider") != "openai":
            st["gemini_until_ts"] = now + self.gemini_free_hours * 3600.0
            st["provider"] = "gemini"
            st["created_ts"] = now
            self._save_state(st)

        if st.get("provider") == "openai":
            return ProviderSelection(
                provider="openai",
                model=self.openai_model,
                display_name=f"OpenAI ({self.openai_model})",
            )

        # Use Gemini until time window ends.
        if st.get("provider") == "gemini":
            until = float(st.get("gemini_until_ts", 0.0))
            if now <= until:
                return ProviderSelection(
                    provider="gemini",
                    model=self.gemini_model,
                    display_name=f"Gemini ({self.gemini_model})",
                )

            st["provider"] = "openai"
            st["switched_ts"] = now
            self._save_state(st)

        return ProviderSelection(
            provider="openai",
            model=self.openai_model,
            display_name=f"OpenAI ({self.openai_model})",
        )

    def mark_gemini_exhausted(self, reason: str) -> None:
        # If Gemini errors out due to quota/rate limiting, mark it exhausted.
        # Next calls will route directly to OpenAI.
        st = self._load_state()
        st["provider"] = "openai"
        st["gemini_exhausted_ts"] = time.time()
        st["gemini_exhausted_reason"] = reason
        self._save_state(st)


class LLMClient:
    def __init__(self, router: ProviderRouter):
        self.router = router

        self._gemini = None
        self._openai = None

    def _gemini_client(self):
        # Lazy client init so imports/auth only happen when needed.
        if self._gemini is not None:
            return self._gemini
        import google.generativeai as genai

        api_key = os.getenv("GEMINI_API_KEY") or ""
        if not api_key:
            raise ProviderError("Missing GEMINI_API_KEY env var.")

        genai.configure(api_key=api_key)
        self._gemini = genai
        return self._gemini

    def _openai_client(self):
        # Lazy client init so we don't require OPENAI_API_KEY unless needed.
        if self._openai is not None:
            return self._openai
        from openai import OpenAI

        api_key = os.getenv("OPENAI_API_KEY") or ""
        if not api_key:
            raise ProviderError("Missing OPENAI_API_KEY env var.")

        self._openai = OpenAI(api_key=api_key)
        return self._openai

    def generate(self, *, system_prompt: str, user_prompt: str) -> Tuple[str, ProviderSelection]:
        # “Single entry point” for all model calls:
        # - route to Gemini/OpenAI
        # - format prompt including system instructions
        # - return both answer and provider metadata
        sel = self.router.select()

        if sel.provider == "gemini":
            try:
                genai = self._gemini_client()
                model = genai.GenerativeModel(sel.model)
                # Gemini supports a single combined prompt; we include system instructions explicitly.
                full_prompt = f"{system_prompt}\n\n{user_prompt}"
                resp = model.generate_content(full_prompt)
                txt = getattr(resp, "text", None) or str(resp)
                return txt, sel
            except Exception as e:
                msg = str(e)
                if _is_quota_or_block_error(msg):
                    self.router.mark_gemini_exhausted(msg)
                raise

        # OpenAI
        try:
            client = self._openai_client()
            resp = client.chat.completions.create(
                model=sel.model,
                temperature=0.2,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
            )
            txt = resp.choices[0].message.content or ""
            return txt, sel
        except Exception as e:
            raise ProviderError(str(e)) from e

