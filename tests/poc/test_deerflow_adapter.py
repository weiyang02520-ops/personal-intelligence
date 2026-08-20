from __future__ import annotations

import pytest

from apps.core.deerflow import DeerFlowRuntimeAdapter
from apps.core.errors import PocError


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


def test_adapter_projects_upstream_events_and_capabilities():
    adapter = DeerFlowRuntimeAdapter(FixtureClient())
    events = list(adapter.start("research", thread_id="thread-1"))
    assert [event.event_type for event in events] == ["text", "result"]
    assert events[0].data == {"text": "hello"}
    capabilities = adapter.capabilities()
    assert capabilities["start"] is True and capabilities["events"] is True
    assert capabilities["cancel"] is False and capabilities["resume"] is False


def test_cancel_is_explicit_contract_gap():
    with pytest.raises(PocError) as error:
        DeerFlowRuntimeAdapter(FixtureClient()).cancel("run-1")
    assert error.value.code == "RUNTIME_CONTRACT_GAP"


class BrokenClient(FixtureClient):
    def stream(self, message, *, thread_id=None, **kwargs):
        raise RuntimeError("upstream down")
        yield  # pragma: no cover


def test_upstream_failure_is_translated():
    with pytest.raises(PocError) as error:
        list(DeerFlowRuntimeAdapter(BrokenClient()).start("research", thread_id="thread-1"))
    assert error.value.code == "RUNTIME_UPSTREAM_ERROR"
