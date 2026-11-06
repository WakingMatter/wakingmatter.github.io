"""Profile-local guards for the cos-claude Hermes home.

Not a native Hermes knob. Counts bot messages per Slack thread, caps this
profile's posts, and halts on an exact ``CoS stop`` from Aditya. State stays
under this profile directory. It never calls ``hermes pause`` on the default
home.
"""

from __future__ import annotations

import json
import os
import time
from pathlib import Path

ADITYA = "U0C6D8NTGNL"
STOP_TEXT = "CoS stop"
UNAVAILABLE = "CoS unavailable"
MAX_BOT_STREAK = 6
MAX_POSTS_PER_HOUR = 20
PING = "<@U0C6D8NTGNL> CoS paused this thread after 6 bot messages without you."
FAILURE_MARKERS = (
    "Claude Code is installed but not logged in",
    "Claude Code is installed but has no usable login",
    "Claude Code is not installed",
    "Something went wrong and I couldn't finish this reply",
    "The AI model service kept failing",
    "I couldn't connect to the AI model service",
    "Sign-in to the AI model service failed",
    "The AI model service isn't reachable",
    "Hermes could not reach the AI model service",
    "The connection to the AI model service was interrupted",
    "The AI model service is rate-limiting",
    "The AI model service rejected this request",
)


def _home() -> Path:
    return Path(__file__).resolve().parents[2]


def _state_path() -> Path:
    return _home() / "cos-guard-state.json"


def _load() -> dict:
    path = _state_path()
    if not path.exists():
        return {"threads": {}, "posts": []}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {"threads": {}, "posts": []}
    if not isinstance(data, dict):
        return {"threads": {}, "posts": []}
    data.setdefault("threads", {})
    data.setdefault("posts", [])
    return data


def _save(data: dict) -> None:
    path = _state_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(data), encoding="utf-8")
    os.replace(tmp, path)


def _halted() -> bool:
    return (_home() / "COS_HALT").exists()


def _engage_halt() -> None:
    home = _home()
    home.mkdir(parents=True, exist_ok=True)
    (home / "COS_HALT").write_text("CoS stop\n", encoding="utf-8")
    payload = {"engaged_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "reason": "CoS stop"}
    (home / "ESTOP").write_text(json.dumps(payload) + "\n", encoding="utf-8")


def _source(obj):
    if obj is None:
        return None
    source = getattr(obj, "source", None)
    return source if source is not None else obj


def _field(source, name: str, default: str = "") -> str:
    if source is None:
        return default
    if isinstance(source, dict):
        value = source.get(name, default)
    else:
        value = getattr(source, name, default)
    return default if value is None else str(value)


def _is_bot(source) -> bool:
    if source is None:
        return False
    if isinstance(source, dict):
        return bool(source.get("is_bot"))
    return bool(getattr(source, "is_bot", False))


def _thread_key(source) -> str:
    chat = _field(source, "chat_id", "unknown")
    thread = _field(source, "thread_id", "")
    return f"{chat}:{thread or 'root'}"


def _recent_posts(data: dict, now: float) -> list:
    posts = [float(item) for item in data.get("posts", []) if now - float(item) < 3600]
    data["posts"] = posts
    return posts


def _thread(data: dict, key: str) -> dict:
    threads = data.setdefault("threads", {})
    row = threads.get(key)
    if not isinstance(row, dict):
        row = {"streak": 0, "quiet": False}
        threads[key] = row
    row.setdefault("streak", 0)
    row.setdefault("quiet", False)
    return row


def _text_of(event, text: str | None = None) -> str:
    if text is not None:
        return str(text).strip()
    return str(getattr(event, "text", "") or "").strip()


def on_pre(event=None, **kwargs):
    del kwargs
    if _halted():
        return {"action": "skip", "reason": "cos-halt"}
    source = _source(event)
    text = _text_of(event)
    user = _field(source, "user_id")
    if text == STOP_TEXT and user == ADITYA and not _is_bot(source):
        _engage_halt()
        return {"action": "skip", "reason": "cos-stop"}
    data = _load()
    now = time.time()
    key = _thread_key(source)
    row = _thread(data, key)
    if user == ADITYA and not _is_bot(source):
        row["streak"] = 0
        row["quiet"] = False
        data["active_thread"] = key
        _save(data)
        return None
    if row.get("quiet"):
        _save(data)
        return {"action": "skip", "reason": "cos-quiet"}
    if len(_recent_posts(data, now)) >= MAX_POSTS_PER_HOUR:
        _save(data)
        return {"action": "skip", "reason": "cos-hourly-cap"}
    if _is_bot(source):
        row["streak"] = int(row.get("streak") or 0) + 1
    data["active_thread"] = key
    _save(data)
    return None


def on_post(text=None, source=None, **kwargs):
    del kwargs
    if _halted():
        return {"action": "handled"}
    body = _text_of(None, text)
    user = _field(source, "user_id")
    if body == STOP_TEXT and user == ADITYA and not _is_bot(source):
        _engage_halt()
        return {"action": "handled"}
    data = _load()
    now = time.time()
    key = _thread_key(source)
    row = _thread(data, key)
    if row.get("quiet"):
        _save(data)
        return {"action": "handled"}
    posts = _recent_posts(data, now)
    if len(posts) >= MAX_POSTS_PER_HOUR:
        _save(data)
        return {"action": "handled"}
    if int(row.get("streak") or 0) >= MAX_BOT_STREAK and _is_bot(source):
        row["quiet"] = True
        posts.append(now)
        _save(data)
        return {"action": "handled", "reply": PING}
    _save(data)
    return None


def on_output(response_text: str = "", **kwargs):
    del kwargs
    text = str(response_text or "")
    if any(marker in text for marker in FAILURE_MARKERS):
        text = UNAVAILABLE
    if not text.strip() or text.strip() in {"[SILENT]", "NO_REPLY", "SILENT"}:
        return UNAVAILABLE if text == UNAVAILABLE else None
    data = _load()
    now = time.time()
    posts = _recent_posts(data, now)
    if len(posts) >= MAX_POSTS_PER_HOUR:
        _save(data)
        return "[SILENT]"
    posts.append(now)
    key = data.get("active_thread")
    row = _thread(data, key) if isinstance(key, str) and key else None
    if row is not None and not row.get("quiet"):
        row["streak"] = int(row.get("streak") or 0) + 1
    _save(data)
    if text == UNAVAILABLE:
        return UNAVAILABLE
    return None


def register(ctx):
    ctx.register_hook("pre_gateway_dispatch", on_pre)
    ctx.register_hook("post_gateway_admission", on_post)
    ctx.register_hook("transform_llm_output", on_output)
