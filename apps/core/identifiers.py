from __future__ import annotations

from uuid import UUID, uuid4


def new_id() -> str:
    return str(uuid4())


def require_id(value: str) -> str:
    try:
        return str(UUID(value))
    except (ValueError, AttributeError, TypeError) as exc:
        raise ValueError("invalid identifier") from exc
