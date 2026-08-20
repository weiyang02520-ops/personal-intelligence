from __future__ import annotations

import json

from fastapi.testclient import TestClient


def test_public_events_are_projected_and_replayable(app):
    client = TestClient(app)
    research_id = client.post("/research", json={}).json()["id"]
    with client.stream("GET", f"/research/{research_id}/events?after_sequence=0") as response:
        body = "".join(response.iter_text())
    assert response.status_code == 200
    assert "event: public" in body
    assert "research.created" in body
    assert "research.completed" in body
    ids = [int(line.removeprefix("id: ")) for line in body.splitlines() if line.startswith("id: ")]
    assert ids == sorted(ids)
    assert len(ids) >= 2
    parsed = [json.loads(line.removeprefix("data: ")) for line in body.splitlines() if line.startswith("data: ")]
    assert all("type" in item and "data" in item for item in parsed)
