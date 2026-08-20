from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable, Protocol

from .contracts import RuntimeEvent
from .errors import PocError


class DeerFlowClientProtocol(Protocol):
    def stream(self, message: str, *, thread_id: str | None = None, **kwargs: Any) -> Iterable[Any]: ...

    def list_models(self) -> dict[str, Any]: ...

    def list_skills(self, enabled_only: bool = False) -> dict[str, Any]: ...


@dataclass(frozen=True)
class RuntimeStart:
    run_id: str
    thread_id: str


class DeerFlowRuntimeAdapter:
    """Thin adapter around reviewed DeerFlowClient surface.

    The embedded client exposes streaming and capability inspection, but no
    stable cancel method in the reviewed source. Cancel is therefore an
    explicit contract gap until the Gateway run API is used in a later PoC.
    """

    def __init__(self, client: DeerFlowClientProtocol):
        self.client = client

    def start(self, message: str, *, thread_id: str) -> Iterable[RuntimeEvent]:
        try:
            for event in self.client.stream(message, thread_id=thread_id):
                event_type = getattr(event, "type", None) or (event.get("type") if isinstance(event, dict) else "custom")
                data = getattr(event, "data", None) or (event.get("data", {}) if isinstance(event, dict) else {})
                yield RuntimeEvent(event_type=str(event_type), data=dict(data))
        except Exception as exc:
            raise PocError("RUNTIME_UPSTREAM_ERROR", "DeerFlow stream failed", 502) from exc

    def cancel(self, _: str) -> bool:
        raise PocError("RUNTIME_CONTRACT_GAP", "reviewed embedded DeerFlowClient has no stable cancel method", 501)

    def capabilities(self) -> dict[str, bool]:
        return {
            "start": callable(getattr(self.client, "stream", None)),
            "events": callable(getattr(self.client, "stream", None)),
            "result": callable(getattr(self.client, "stream", None)),
            "cancel": False,
            "models": callable(getattr(self.client, "list_models", None)),
            "skills": callable(getattr(self.client, "list_skills", None)),
            "resume": False,
        }
