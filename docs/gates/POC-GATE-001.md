# POC-GATE-001 — Physical Architecture PoC External Review Packet

Status: READY_WITH_KNOWN_GAPS — EXTERNAL REVIEW REQUIRED  
Gate owner: External Review  
Architecture Freeze: NO  
M1 authorization: NO

## Gate purpose

Review whether the physical architecture candidate has enough evidence to proceed to a separately authorized Architecture Freeze discussion. This packet is not a self-approval and does not authorize M1.

## Baseline and scope

- Prior accepted baseline: `bd12271c6e2cdc3a2e3e8fef440c47aaf86cfe82`
- Closure batch starting baseline: `e7f6d5c97a62b35cacfbabf713daa81f55aea001`
- Prior gate verdict: `M0-GATE-001 PASS_WITH_NOTES`
- External Review delta: `POC-GATE-001 CHANGES_REQUESTED`; this packet records the focused closure evidence.
- PoC scope: `TASK-POC-001` through `TASK-POC-012`
- No M1/M2/M3/M4 business feature implementation is included.

## Evidence register

| Task | Evidence | Verification | Result |
|---|---|---|---|
| POC-001 | `apps/core/`, import-rule test, `pyproject.toml` | automated | PASS |
| POC-002 | FastAPI lifecycle, FakeRuntime, SQLite tests, isolated PostgreSQL integration | automated + integration | PASS |
| POC-003 | `apps/core/api.py` public stream and real disconnect → continue → reconnect test | automated endpoint harness | PASS |
| POC-004 | PostgreSQL rollback row-count proof and PostgreSQL duplicate consumer/event proof; SQLite fast tests retained | isolated PostgreSQL + automated | PASS |
| POC-005 | PostgreSQL enqueue/claim/heartbeat/retry/stale recovery/complete across separate service instances | isolated PostgreSQL + automated | PASS |
| POC-006 | SearchGateway contract tests plus canonical Search cancellation conflict report | automated + spec audit | PARTIAL |
| POC-007 | SSRF, redirect revalidation, timeout/size-bounded FetchGateway tests | automated | PASS |
| POC-008 | Gateway HTTP/SSE adapter, exact pinned route anchors, embedded rejection fixture, controlled transport tests | source + automated | PASS_WITH_LIMITATION |
| POC-009 | allowlisted SearchToolBridge and credential isolation tests | automated | PASS |
| POC-010 | `apps/web/` minimal Next.js build and frontend boundary test | build + automated | PASS |
| POC-011 | runtime-generated canary across API/SSE/DB/log/HTTP/Git plus typed missing-secret test | automated + source scan | PASS |
| POC-012 | this packet and external-review request | document | READY_FOR_EXTERNAL_REVIEW |

## Candidate architectural observations

1. Candidate A (Python/FastAPI + PostgreSQL) is physically viable for the PoC lifecycle and persistence slice.
2. PostgreSQL-backed state/outbox atomicity is demonstrated; no broker or workflow engine was added.
3. PI-owned SearchGateway and FetchGateway boundaries are implementable without exposing provider credentials to the runtime. Search cancellation remains a canonical-contract conflict and is not claimed as implemented.
4. SSE replay works from PI-owned public event sequence numbers.
5. The DeerFlow Gateway HTTP/SSE boundary is preferred over the embedded client for process isolation, replaceability, failure isolation and cancel lifecycle. Gateway cancel is contract-verified; resume and runtime version remain NOT FROZEN.

## Closure Batch explicit answers

| Question | Answer | Evidence |
|---|---|---|
| SSE reconnect proven? | YES | `tests/poc/test_sse.py` consumes first endpoint frame, abandons connection, waits for completion, reconnects with cursor and checks only missing sequences |
| PostgreSQL transaction rollback proven? | YES | `tests/poc/test_postgres_integration.py` |
| PostgreSQL idempotency proven? | YES | `tests/poc/test_postgres_integration.py` |
| PostgreSQL job recovery proven? | YES | `tests/poc/test_jobs.py` integration case with separate service instances |
| Search cancellation proven? | NO — SPEC CONFLICT | `docs/audit/poc/SEARCH_CANCELLATION_CONFLICT.md`; canonical Blueprint does not define Search cancellation |
| Secret multi-surface non-leakage proven? | YES | `tests/poc/test_secrets.py`; output is `CANARY_LEAK_TEST: PASS` |
| DeerFlow external Runtime boundary identified? | YES | `docs/audit/poc/DEERFLOW_CONTRACT.md` and pinned Gateway route inspection |
| DeerFlow cancel contract satisfied? | YES | Gateway `POST /api/threads/{thread_id}/runs/{run_id}/cancel` controlled transport test |
| Real credentialed DeerFlow run? | NOT VERIFIED — CREDENTIAL REQUIRED | No real credential used or committed |

## Known gaps requiring External Review decision

- No credentialed end-to-end DeerFlow run was claimed.
- `TASK-POC-006` remains PARTIAL until a Spec owner resolves the Search cancellation conflict.
- Job retry policy is a minimal PoC policy and has no production backoff/dead-letter semantics.
- The in-memory SecretStore is only a boundary proof, not durable secret management.
- The GitHub adapter proves one real provider shape; it does not select the final Search provider.
- UI is a thin PI API client and not a Product UI.

## Review outcomes allowed by the gate

External Review may record `PASS`, `PASS_WITH_NOTES`, or `NOT_READY`. Closure candidate remains `READY_WITH_KNOWN_GAPS` because Search cancellation is unresolved and real model execution is not verified. Until review is recorded, the repository remains in Physical Architecture PoC, Architecture Freeze remains NO, and M1 remains NOT AUTHORIZED.
