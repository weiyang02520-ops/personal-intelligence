# PoC Security and Boundary Matrix

| Boundary | Test/evidence | Result | Known limitation |
|---|---|---|---|
| FetchGateway → network | `tests/poc/test_fetch.py` | PASS: only HTTP/HTTPS, DNS result checked, private/loopback/link-local/reserved/metadata blocked, redirects revalidated, size bounded | DNS rebinding and egress policy need a production network design |
| SearchGateway → provider | `tests/poc/test_search.py` | PASS: normalized response, timeout/auth/rate-limit/unavailable mapping, credentials read from environment only | GitHub is a PoC real adapter, not final general-web provider |
| Runtime → tool bridge | `tests/poc/test_search.py` | PASS: only `search` allowlisted; provider credential stays in PI-side provider | No production policy engine or per-run grants yet |
| Runtime → public API | `tests/poc/test_frontend_boundary.py`, SSE tests | PASS: UI references PI `/research` and `/events` only; no upstream runtime endpoint/types | Frontend is a minimal build proof, not an M1 UI |
| SecretStore → API/SSE/DB/log/HTTP/Git | `tests/poc/test_secrets.py`; runtime-generated canary | PASS: `CANARY_LEAK_TEST: PASS` across all required surfaces; typed missing-secret error | In-memory store is deliberately non-production |
| Job service → PostgreSQL | `tests/poc/test_jobs.py`, `tests/poc/test_postgres_integration.py` | PASS: separate service lifecycles recover stale lease and complete once logically | Retry backoff/dead-letter policy remains PoC-only |
| Outbox/public event | `tests/poc/test_outbox.py`, `test_sse.py` | PASS: state and outbox commit together; duplicate consumer delivery is idempotent; public events replay by sequence | No production broker selected |
