# Personal Intelligence — M0 Implementation Map

Status: `CURRENT COVERAGE: M0 SLICE`  
Blueprint: [`docs/plan(4).md`](plan(4).md)  
Architecture: NOT FROZEN  
This map intentionally uses architecture/governance IDs where the Blueprint does not provide a closed Product Requirement trace. It does not invent Product REQ IDs.

## Current coverage: M0 slice

| Requirement / control | M0 Task | Required evidence | Artifact | Gate condition |
|---|---|---|---|---|
| `GOV-M0-001` Task packet completeness from PART 16.2 | M0-001..014 | Required fields, dependencies, stop rules, result sections | `docs/tasks/m0/TASK-M0-*.md` | All M0 tasks independently reviewable |
| `GOV-M0-002` canonical reuse artifacts from PART 16.5 | M0-001, M0-013 | Canonical path and legacy alias rule | `docs/audit/m0/OPEN_SOURCE_AUDIT.md` + canonical files | Artifact contract is unambiguous |
| `ARCH-M0-001` runtime adapter feasibility | M0-002..004, M0-012 | Runtime capability, extension, permission and failure evidence | `RUNTIME_AUDIT.md` | Runtime path is evidence-backed or explicitly blocked |
| `ARCH-M0-002` search/crawl/connector capability evidence | M0-007..009 | Provider, escalation and connector matrix | `SEARCH_PROVIDER_AUDIT.md` | Minimal combination remains a candidate, not an unproven choice |
| `ARCH-M0-003` algorithm/reference reuse evidence | M0-005..006 | Capability map and strategy cards | `ALGORITHM_REUSE_AUDIT.md`, `STRATEGY_REGISTRY.md` | No duplicate self-build claim without audit |
| `NFR-M0-001` evidence/reproducibility | M0-001..013 | URL, version/commit, license, evidence level, limitations | All M0 audit artifacts | Claims are reproducible and uncertainty visible |
| `NFR-M0-002` security boundary preservation | M0-008, M0-012 | Trust, permission, network/file isolation evidence | `RUNTIME_AUDIT.md`, `SEARCH_PROVIDER_AUDIT.md` | No unisolated execution is authorized |
| `GOV-M0-003` recommendation vs ADR acceptance | M0-013, M0-014 | ADR update proposals, no ACCEPTED decisions | `REUSE_DECISION_MATRIX.md`, `M0-GATE-001.md` | External reviewer owns Gate decision |
| `GOV-M0-004` stop before PoC/M1 | M0-014 | Gate candidate result and review request | `docs/gates/M0-GATE-001.md` | `READY_FOR_EXTERNAL_REVIEW` or `BLOCKED`, never self-PASS |

## Future coverage

Product `REQ-*` → Use Case → Module → Component → Function → Test → Task traceability remains open and must be built incrementally for PoC/M1/M2/M3/M4 after architecture review. The known gaps are recorded in `docs/audit/BLUEPRINT_AUDIT.md`, `SPEC_CONFLICTS.md` and `OPEN_TBDS.md`; this M0 slice does not silently close them.

## Traceability rule

Every later implementation task must link back to a Requirement or explicit `ARCH-*`/`NFR-*`/`GOV-*` control, its Function/Interface and Test IDs, then a Gate condition. M0 audit tasks produce evidence documents only and do not create Product Core implementation mappings.

## Current coverage: Physical Architecture PoC slice

| Requirement / control | PoC Task | Interface / Contract | Required Test | Evidence | POC-GATE-001 condition |
|---|---|---|---|---|---|
| `ARCH-POC-001` Runtime boundary | POC-001, POC-008 | `IF-RUNTIME-001`, `DeerFlowRuntimeAdapter` | Import boundary + adapter contract | Skeleton/import report + runtime audit | PI Core is runtime-agnostic |
| `ARCH-POC-002` Search boundary | POC-006 | `IF-SEARCH-001`, `SearchGateway` | Normal/timeout/429/auth/no-result/cancel | Search contract report | Real provider adapter normalized |
| `ARCH-POC-003` Public API boundary | POC-002, POC-010 | `POST/GET /research` | API lifecycle contract | API test report | Web uses PI API only |
| `ARCH-POC-004` SSE/event boundary | POC-003 | PI PublicEvent + SSE | Disconnect/reconnect sequence test | SSE replay report | Runtime SSE not exposed |
| `ARCH-POC-005` Persistence transaction/outbox | POC-004 | state + outbox transaction | commit failure/idempotent consumer | Outbox fault report | Atomicity is evidenced |
| `ARCH-POC-006` Job/recovery | POC-005 | enqueue/worker/lease/recovery | worker kill/restart | Job recovery report | Simplest candidate recovers |
| `NFR-POC-001` Fetch security | POC-007 | `FetchGateway` | SSRF/private/metadata/redirect tests | Fetch security report | Required targets blocked |
| `NFR-POC-002` Secret boundary | POC-011 | `SecretStore` | API/SSE/DB/log/HTTP/Git canary scan | SecretStore report | Canary never leaks |
| `NFR-POC-003` Runtime tool bridge | POC-009 | bounded PI search tool | allow/deny/key non-exposure | Tool bridge report | Runtime receives no provider key |
| `GOV-POC-001` External gate discipline | POC-012 | POC-GATE-001 evidence schema | coverage + non-self-PASS scan | Gate packet | External review required |

Future Product Requirement mappings remain out of scope for this PoC slice.
