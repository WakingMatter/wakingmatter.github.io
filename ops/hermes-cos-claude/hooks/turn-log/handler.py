"""Append redacted turn lines under this profile only."""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

_SECRET = re.compile(
    r"(xox[bapre]-[A-Za-z0-9-]+|sk-ant-[A-Za-z0-9_-]+|gh[pousr]_[A-Za-z0-9_]+|"
    r"github_pat_[A-Za-z0-9_]+|Bearer\s+\S+|(?:api[_-]?key|token|secret|password)\s*[=:]\s*\S+)",
    re.IGNORECASE,
)


def _home() -> Path:
    return Path(__file__).resolve().parents[2]


def _redact(value):
    if isinstance(value, str):
        return _SECRET.sub("[REDACTED]", value)
    if isinstance(value, dict):
        return {str(key): _redact(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_redact(item) for item in value]
    if value is None or isinstance(value, (int, float, bool)):
        return value
    return _SECRET.sub("[REDACTED]", str(value))


async def handle(event_type: str, context: dict):
    line = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event": event_type,
        "context": _redact(context if isinstance(context, dict) else {}),
    }
    path = _home() / "logs" / "turns.jsonl"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(line, ensure_ascii=False) + "\n")
