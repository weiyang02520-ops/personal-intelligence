from __future__ import annotations

from .errors import SecretNotFound


class InMemorySecretStore:
    """Reversible PoC store; values never enter API models, events or database rows."""

    def __init__(self):
        self._values: dict[str, str] = {}

    def put(self, name: str, value: str) -> None:
        self._values[name] = value

    def get(self, name: str) -> str:
        try:
            return self._values[name]
        except KeyError as exc:
            raise SecretNotFound(name) from exc

    def has(self, name: str) -> bool:
        return name in self._values

    def redact(self, text: str) -> str:
        for value in self._values.values():
            text = text.replace(value, "[REDACTED]")
        return text
