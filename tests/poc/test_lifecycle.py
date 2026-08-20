from __future__ import annotations

import time

from fastapi.testclient import TestClient


def test_research_lifecycle_is_async_and_persistent(app):
    client = TestClient(app)
    response = client.post("/research", json={})
    assert response.status_code == 202
    research_id = response.json()["id"]
    assert response.json()["status"] == "CREATED"

    deadline = time.monotonic() + 2
    while time.monotonic() < deadline:
        result = client.get(f"/research/{research_id}")
        if result.json()["status"] == "COMPLETED":
            break
        time.sleep(0.02)
    assert result.json()["status"] == "COMPLETED"

    fresh_client = TestClient(app)
    assert fresh_client.get(f"/research/{research_id}").json()["id"] == research_id


def test_missing_research_uses_error_envelope(app):
    response = TestClient(app).get("/research/not-found")
    assert response.status_code == 404
    assert response.json()["error"]["code"] == "NOT_FOUND"
