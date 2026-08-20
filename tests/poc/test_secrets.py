from __future__ import annotations

import json
import logging
import subprocess
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient

from apps.core.models import Base
from apps.core.search import GitHubSearchProvider
from apps.core.secrets import InMemorySecretStore
from apps.core.errors import SecretNotFound


def test_secret_store_retrieves_and_reports_missing_secret_without_plaintext():
    store = InMemorySecretStore()
    store.put("github", "secret-token")
    assert store.get("github") == "secret-token"
    assert store.has("github") is True
    assert store.redact("Authorization: secret-token") == "Authorization: [REDACTED]"
    with pytest.raises(SecretNotFound) as error:
        store.get("missing")
    assert error.value.code == "SECRET_NOT_FOUND"


def test_unique_secret_canary_has_no_api_sse_db_log_http_or_git_leak(app, caplog):
    canary = f"poc-canary-{uuid4().hex}"
    store = app.state.secret_store
    store.put("provider", canary)

    # The adapter may retrieve the value internally; it is never placed in a
    # PI DTO, event, database row, or public response.
    provider = GitHubSearchProvider(token=store.get("provider"))
    assert provider.token == canary

    client = TestClient(app)
    with caplog.at_level(logging.INFO, logger="poc.canary"):
        logging.getLogger("poc.canary").info("provider=%s", store.redact(store.get("provider")))
        api_response = client.post("/research", json={})
        research_id = api_response.json()["id"]
        with client.stream("GET", f"/research/{research_id}/events?after_sequence=0") as sse_response:
            sse_body = "".join(sse_response.iter_text())

    assert canary not in api_response.text
    assert canary not in sse_body
    assert canary not in "\n".join(f"{key}: {value}" for key, value in api_response.headers.items())
    assert canary not in caplog.text

    with app.state.database.session() as session:
        for table in Base.metadata.sorted_tables:
            rows = session.execute(table.select()).mappings()
            for row in rows:
                assert canary not in json.dumps(dict(row), default=str)

    tracked = subprocess.run(["git", "ls-files"], cwd=__import__("pathlib").Path(__file__).parents[2], capture_output=True, text=True, check=True).stdout.splitlines()
    assert all(canary not in __import__("pathlib").Path(__file__).parents[2].joinpath(path).read_text(encoding="utf-8", errors="ignore") for path in tracked)
    print("CANARY_LEAK_TEST: PASS")
