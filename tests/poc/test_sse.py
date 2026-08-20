from __future__ import annotations

import asyncio
import json
import time

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


def _events_endpoint(app):
    return next(route.endpoint for route in app.routes if getattr(route, "path", "").endswith("/events"))


async def _read_one(iterator):
    return await iterator.__anext__()


async def _read_all(iterator):
    chunks = []
    async for chunk in iterator:
        chunks.append(chunk.decode() if isinstance(chunk, bytes) else chunk)
    return "".join(chunks)


def test_sse_disconnect_continue_and_reconnect_replays_only_missing_events(app):
    client = TestClient(app)
    research_id = client.post("/research", json={}).json()["id"]
    endpoint = _events_endpoint(app)

    # This calls the real PI SSE route and consumes only its first response
    # frame. Abandoning the iterator is the deterministic in-process equivalent
    # of a client disconnect; the runtime thread is not owned by this iterator.
    first_connection = endpoint(research_id, after_sequence=0)
    first_chunk = asyncio.run(_read_one(first_connection.body_iterator))
    if isinstance(first_chunk, bytes):
        first_chunk = first_chunk.decode()
    first_data = next(json.loads(line.removeprefix("data: ")) for line in first_chunk.splitlines() if line.startswith("data: "))
    cursor = int(first_data["sequence"])
    assert first_data["type"] == "research.created"

    deadline = time.monotonic() + 2
    while time.monotonic() < deadline and client.get(f"/research/{research_id}").json()["status"] != "COMPLETED":
        time.sleep(0.02)
    assert client.get(f"/research/{research_id}").json()["status"] == "COMPLETED"

    # Reconnect through the same PI endpoint with the sequence cursor.
    second_connection = endpoint(research_id, after_sequence=cursor)
    replay = asyncio.run(_read_all(second_connection.body_iterator))
    replayed = [json.loads(line.removeprefix("data: ")) for line in replay.splitlines() if line.startswith("data: ")]
    sequences = [item["sequence"] for item in replayed]
    assert sequences == sorted(sequences) and all(sequence > cursor for sequence in sequences)
    assert [item["type"] for item in replayed] == ["research.running", "research.completed"]
    assert all(not {"DeerFlow", "LangGraph", "RuntimeEvent"}.intersection(item["data"]) for item in replayed)
