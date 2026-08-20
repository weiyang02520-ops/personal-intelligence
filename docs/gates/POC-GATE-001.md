# POC-GATE-001 — Physical Architecture PoC External Review Packet

Status: READY_WITH_KNOWN_GAPS — EXTERNAL REVIEW REQUIRED  
Gate owner: External Review  
Architecture Freeze: NO  
M1 authorization: NO

## Gate purpose

Review whether the physical architecture candidate has enough evidence to proceed to a separately authorized Architecture Freeze discussion. This packet is not a self-approval and does not authorize M1.

## Baseline and scope

- Prior accepted baseline: `bd12271c6e2cdc3a2e3e8fef440c47aaf86cfe82`
- Prior gate verdict: `M0-GATE-001 PASS_WITH_NOTES`
- PoC scope: `TASK-POC-001` through `TASK-POC-012`
- No M1/M2/M3/M4 business feature implementation is included.

## Evidence register

| Task | Evidence | Verification | Result |
|---|---|---|---|
| POC-001 | `apps/core/`, import-rule test, `pyproject.toml` | automated | PASS |
| POC-002 | FastAPI lifecycle, FakeRuntime, SQLite tests, isolated PostgreSQL integration | automated + integration | PASS |
| POC-003 | PI-owned public event rows and SSE replay tests | automated | PASS |
| POC-004 | transaction rollback, outbox row, duplicate consumer idempotency tests | automated | PASS |
| POC-005 | DB-backed enqueue/claim/retry/heartbeat/stale recovery tests | automated | PASS |
| POC-006 | `IF-SEARCH-001` implementation, fake transport contract tests, optional live adapter path | automated + optional live | PASS_WITH_LIMITATION |
| POC-007 | SSRF, redirect revalidation, timeout/size-bounded FetchGateway tests | automated | PASS |
| POC-008 | `docs/audit/poc/DEERFLOW_CONTRACT.md`, pinned source inspection, thin adapter tests | source + automated | PASS_WITH_CONTRACT_GAP |
| POC-009 | allowlisted SearchToolBridge and credential isolation tests | automated | PASS |
| POC-010 | `apps/web/` minimal Next.js build and frontend boundary test | build + automated | PASS |
| POC-011 | in-memory SecretStore and leakage boundary tests | automated + source scan | PASS_WITH_LIMITATION |
| POC-012 | this packet and external-review request | document | READY_FOR_EXTERNAL_REVIEW |

## Candidate architectural observations

1. Candidate A (Python/FastAPI + PostgreSQL) is physically viable for the PoC lifecycle and persistence slice.
2. PostgreSQL-backed state/outbox atomicity is demonstrated; no broker or workflow engine was added.
3. PI-owned SearchGateway and FetchGateway boundaries are implementable without exposing provider credentials to the runtime.
4. SSE replay works from PI-owned public event sequence numbers.
5. DeerFlow can be wrapped for stream/capability inspection, but cancel and resume are explicit contract gaps. Runtime version remains NOT FROZEN.

## Known gaps requiring External Review decision

- No credentialed end-to-end DeerFlow run was claimed.
- Job retry policy is a minimal PoC policy and has no production backoff/dead-letter semantics.
- The in-memory SecretStore is only a boundary proof, not durable secret management.
- The GitHub adapter proves one real provider shape; it does not select the final Search provider.
- UI is a thin PI API client and not a Product UI.

## Review outcomes allowed by the gate

External Review may record `PASS`, `PASS_WITH_NOTES`, or `NOT_READY`. Until that review is recorded, the repository remains in Physical Architecture PoC, Architecture Freeze remains NO, and M1 remains NOT AUTHORIZED.
