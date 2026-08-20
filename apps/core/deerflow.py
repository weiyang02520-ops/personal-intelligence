from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Iterable, Protocol

import httpx

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
    status: str = "pending"
    location: str | None = None


class DeerFlowRuntimeAdapter:
    """PI adapter for the reviewed DeerFlow Gateway HTTP/SSE boundary."""

    def __init__(self, client: httpx.Client):
        self.client = client

    def _request(self, method: str, path: str, **kwargs: Any) -> httpx.Response:
        try:
            response = self.client.request(method, path, **kwargs)
        except httpx.TimeoutException as exc:
            raise PocError("RUNTIME_TIMEOUT", "DeerFlow Gateway request timed out", 504) from exc
        except httpx.HTTPError as exc:
            raise PocError("RUNTIME_UNAVAILABLE", "DeerFlow Gateway transport failed", 502) from exc
        if response.status_code >= 400:
            raise PocError("RUNTIME_GATEWAY_ERROR", f"DeerFlow Gateway returned {response.status_code}", response.status_code)
        return response

    @staticmethod
    def _run_path(thread_id: str, run_id: str) -> str:
        return f"/api/threads/{thread_id}/runs/{run_id}"

    def start(self, message: str, *, thread_id: str) -> RuntimeStart:
        response = self._request(
            "POST",
            f"/api/threads/{thread_id}/runs",
            json={"input": {"messages": [{"role": "user", "content": message}]}},
        )
        payload = response.json()
        run_id = str(payload.get("run_id") or "")
        if not run_id:
            raise PocError("RUNTIME_INVALID_RESPONSE", "Gateway start response has no run_id", 502)
        return RuntimeStart(run_id, str(payload.get("thread_id") or thread_id), str(payload.get("status") or "pending"), response.headers.get("content-location"))

    def status(self, handle: RuntimeStart) -> dict[str, Any]:
        payload = self._request("GET", self._run_path(handle.thread_id, handle.run_id)).json()
        return {"run_id": str(payload.get("run_id") or handle.run_id), "thread_id": str(payload.get("thread_id") or handle.thread_id), "status": str(payload.get("status") or "unknown")}

    def events(self, handle: RuntimeStart) -> Iterable[RuntimeEvent]:
        response = self._request("GET", f"{self._run_path(handle.thread_id, handle.run_id)}/join")
        event_name = "message"
        data_lines: list[str] = []
        for line in response.iter_lines():
            if not line:
                if data_lines:
                    raw = "\n".join(data_lines)
                    try:
                        data = json.loads(raw)
                    except json.JSONDecodeError:
                        data = {"value": raw}
                    yield RuntimeEvent(event_name, data if isinstance(data, dict) else {"value": data})
                    data_lines = []
                event_name = "message"
                continue
            if line.startswith("event:"):
                event_name = line.split(":", 1)[1].strip() or "message"
            elif line.startswith("data:"):
                data_lines.append(line.split(":", 1)[1].lstrip())
        if data_lines:
            raw = "\n".join(data_lines)
            try:
                data = json.loads(raw)
            except json.JSONDecodeError:
                data = {"value": raw}
            yield RuntimeEvent(event_name, data if isinstance(data, dict) else {"value": data})

    def result(self, handle: RuntimeStart) -> dict[str, Any]:
        payload = self._request("GET", f"{self._run_path(handle.thread_id, handle.run_id)}/messages").json()
        return {"run_id": handle.run_id, "messages": payload.get("data", []) if isinstance(payload, dict) else []}

    def cancel(self, handle: RuntimeStart, *, action: str = "interrupt") -> bool:
        response = self._request("POST", f"{self._run_path(handle.thread_id, handle.run_id)}/cancel", params={"action": action})
        return response.status_code in {202, 204}

    def capabilities(self) -> dict[str, bool]:
        health = self._request("GET", "/health").json()
        self._request("GET", "/api/models")
        self._request("GET", "/api/skills")
        return {
            "gateway": True,
            "healthy": health.get("status") == "healthy",
            "start": True,
            "events": True,
            "result": True,
            "cancel": True,
            "models": True,
            "skills": True,
            "resume": False,
        }


class EmbeddedDeerFlowRuntimeAdapter:
    """Embedded-client fixture retained to document the rejected boundary."""

    def __init__(self, client: DeerFlowClientProtocol):
        self.client = client

    def start(self, message: str, *, thread_id: str) -> Iterable[RuntimeEvent]:
        try:
            for event in self.client.stream(message, thread_id=thread_id):
                event_type = getattr(event, "type", None) or (event.get("type") if isinstance(event, dict) else "custom")
                data = getattr(event, "data", None) or (event.get("data", {}) if isinstance(event, dict) else {})
                yield RuntimeEvent(event_type=str(event_type), data=dict(data))
        except Exception as exc:
            raise PocError("RUNTIME_UPSTREAM_ERROR", "DeerFlow embedded stream failed", 502) from exc

    def cancel(self, _: str) -> bool:
        raise PocError("RUNTIME_CONTRACT_GAP", "reviewed embedded DeerFlowClient has no stable cancel method", 501)

    def capabilities(self) -> dict[str, bool]:
        return {
            "gateway": False,
            "start": callable(getattr(self.client, "stream", None)),
            "events": callable(getattr(self.client, "stream", None)),
            "result": callable(getattr(self.client, "stream", None)),
            "cancel": False,
            "models": callable(getattr(self.client, "list_models", None)),
            "skills": callable(getattr(self.client, "list_skills", None)),
            "resume": False,
        }
