from __future__ import annotations

import httpx
import pytest

from apps.core.deerflow import DeerFlowRuntimeAdapter, EmbeddedDeerFlowRuntimeAdapter
from apps.core.errors import PocError


def test_gateway_adapter_maps_start_status_events_result_cancel_and_capabilities():
    calls = []

    def handler(request: httpx.Request):
        calls.append((request.method, request.url.path))
        if request.method == "POST" and request.url.path.endswith("/runs"):
            assert request.read().find(b"research") >= 0
            return httpx.Response(200, headers={"Content-Location": "/api/threads/thread-1/runs/run-1"}, json={"run_id": "run-1", "thread_id": "thread-1", "status": "pending"}, request=request)
        if request.method == "GET" and request.url.path.endswith("/run-1"):
            return httpx.Response(200, json={"run_id": "run-1", "thread_id": "thread-1", "status": "completed"}, request=request)
        if request.method == "GET" and request.url.path.endswith("/run-1/join"):
            body = b'event: messages-tuple\ndata: {"text":"hello"}\n\nevent: end\ndata: {"status":"completed"}\n\n'
            return httpx.Response(200, headers={"content-type": "text/event-stream"}, content=body, request=request)
        if request.method == "GET" and request.url.path.endswith("/run-1/messages"):
            return httpx.Response(200, json={"data": [{"type": "result", "content": "done"}], "has_more": False}, request=request)
        if request.method == "POST" and request.url.path.endswith("/run-1/cancel"):
            return httpx.Response(202, request=request)
        if request.method == "GET" and request.url.path == "/health":
            return httpx.Response(200, json={"status": "healthy", "service": "deer-flow-gateway"}, request=request)
        if request.method == "GET" and request.url.path in {"/api/models", "/api/skills"}:
            return httpx.Response(200, json={"data": []}, request=request)
        return httpx.Response(404, request=request)

    http_client = httpx.Client(transport=httpx.MockTransport(handler), base_url="https://deerflow.test")
    adapter = DeerFlowRuntimeAdapter(http_client)
    handle = adapter.start("research", thread_id="thread-1")
    assert handle.run_id == "run-1" and handle.thread_id == "thread-1"
    assert adapter.status(handle)["status"] == "completed"
    events = list(adapter.events(handle))
    assert [event.event_type for event in events] == ["messages-tuple", "end"]
    assert events[0].data == {"text": "hello"}
    assert adapter.result(handle)["messages"][0]["type"] == "result"
    assert adapter.cancel(handle) is True
    capabilities = adapter.capabilities()
    assert capabilities["gateway"] is True and capabilities["cancel"] is True and capabilities["resume"] is False
    assert ("POST", "/api/threads/thread-1/runs/run-1/cancel") in calls


class FixtureClient:
    def stream(self, message, *, thread_id=None, **kwargs):
        assert message == "research"
        assert thread_id == "thread-1"
        yield {"type": "text", "data": {"text": "hello"}}
        yield {"type": "result", "data": {"status": "completed"}}

    def list_models(self):
        return {"models": ["fixture"]}

    def list_skills(self, enabled_only=False):
        return {"skills": [], "enabled_only": enabled_only}


def test_embedded_client_is_retained_only_as_rejected_boundary():
    adapter = EmbeddedDeerFlowRuntimeAdapter(FixtureClient())
    events = list(adapter.start("research", thread_id="thread-1"))
    assert [event.event_type for event in events] == ["text", "result"]
    assert adapter.capabilities()["cancel"] is False
    with pytest.raises(PocError) as error:
        adapter.cancel("run-1")
    assert error.value.code == "RUNTIME_CONTRACT_GAP"


class BrokenClient(FixtureClient):
    def stream(self, message, *, thread_id=None, **kwargs):
        raise RuntimeError("upstream down")
        yield  # pragma: no cover


def test_embedded_upstream_failure_is_translated():
    with pytest.raises(PocError) as error:
        list(EmbeddedDeerFlowRuntimeAdapter(BrokenClient()).start("research", thread_id="thread-1"))
    assert error.value.code == "RUNTIME_UPSTREAM_ERROR"
