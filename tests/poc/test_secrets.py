from __future__ import annotations

from apps.core.secrets import InMemorySecretStore


def test_secret_store_retrieves_without_persisting_plaintext():
    store = InMemorySecretStore()
    store.put("github", "secret-token")
    assert store.get("github") == "secret-token"
    assert store.has("github") is True
    assert store.redact("Authorization: secret-token") == "Authorization: [REDACTED]"
