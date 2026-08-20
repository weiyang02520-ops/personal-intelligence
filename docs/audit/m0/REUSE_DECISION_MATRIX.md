# M0 Reuse Decision Matrix

Source tasks: TASK-M0-011, TASK-M0-013  
Status: DECISION CANDIDATES ONLY — no ADR accepted, no Architecture Freeze

## Matrix

| Capability | Candidate | Evidence | Decision Classification | Plan Reuse Mode | Verified existing capability | PI custom design / open gap | ADR update proposal |
|---|---|---|---|---|---|---|---|
| Runtime | DeerFlow | L1/L2 partial | UNKNOWN | ADAPTER | API/extension surface reviewed | Pin source contract; adopted version not frozen | Update ADR-002 with contract evidence rule |
| Runtime | Pi | L1, L2/L3 partial | ADAPT | ADAPTER | Sessions/tools likely; permission absent | Adapter, cancel/resume/state mapping, sandbox | Update ADR-002/003 with alternate-runtime comparison |
| Search gateway | SearXNG | L1/L2 candidate | ADAPT | ADAPTER | HTTP metasearch boundary candidate | Operator/health/provenance normalization | Update ADR-004 with provider contract evidence |
| Search provider | Brave/Exa/Tavily | L2 docs candidate | UNKNOWN | ADAPTER | Hosted APIs exist | Credentials, costs, terms, rate limits, live shape | Record provider selection as later architecture task |
| GitHub vertical | GitHub REST Search | L2 official docs | ADAPT | ADAPTER | API boundary candidate | Auth, rate limit, provenance and query semantics | Add vertical provider evidence to ADR-004 |
| Fetch/Crawl | Direct HTTP | L1 | REFERENCE | REJECT | Common-case fetch concept | SSRF, parser, provenance, trust | Define boundary in crawler PoC task |
| Crawl | Crawl4AI/Firecrawl | L1/L2 candidate | UNKNOWN | ADAPTER | Candidate crawl interfaces | License, isolation, hosting and failure behavior | Compare in PoC, no dependency yet |
| Browser fallback | Browser Use | L1/L2 candidate | REFERENCE | UI_REFERENCE | Browser automation pattern | Permission/isolation/nondeterminism | Security/PoC decision input |
| Research loop | ODR/GPT Researcher/Deep Searcher | L1/L2 partial | REFERENCE | ALGORITHM_REFERENCE | Patterns and codebases exist | PI-owned evidence/citation semantics | Add algorithm reference note, no fork |
| Discovery strategy | STORM/MindSearch/Alibaba family | L1/L2 partial | REFERENCE | ALGORITHM_REFERENCE | Strategy candidates | Ownership, stop thresholds, benchmark | M1 strategy ADR proposal |
| Community connectors | SurfSense/REST/MCP | L1/L2 partial | UNKNOWN | ADAPTER | Connector patterns | Auth, terms, schema/security | Adapter contract review |
| Queue/workflow | DB queue / Arq / RQ / Celery / Temporal-like | L1/L2 candidate | UNKNOWN | INFRASTRUCTURE_OPTION | Capability categories | Final Python stack, DB, durability, ops | Update ADR-001/005/006 after PoC |
| Security | External sandbox + permission layer | L1/L2 partial | UNKNOWN | ADAPTER | Need is verified | Trust boundary and enforcement unproven | Update ADR-003 with security acceptance tests |
| UI primitives | Morphic/Vane/DeerFlow/CC Switch | L0-L2 partial | REFERENCE | UI_REFERENCE | Patterns only | PI-owned UI and API boundary | M4 design/reference review |

## Cross-project comparison

| Axis | Strongest evidence | Weakest evidence | Current implication |
|---|---|---|---|
| Runtime | Pi local source snapshot | DeerFlow external contract | Do not select runtime yet |
| Research algorithms | Several public references | PI behavior/benchmark fit | Borrow strategy ideas, keep PI semantics |
| Search | Official provider APIs | Cost/terms/live behavior | Build capability comparison before M1 choice |
| Crawl | Multiple mature candidates | security/legal/isolation | Use escalation ladder, defer dependency |
| UI | Reference patterns | license/component mapping | Reference only |
| Queue/security | Capability families identified | final stack and proof | PoC/ADR required |

## Explicit labels

`Verified existing capability` means only the evidence in the referenced audit row, not production readiness. `PI custom design` includes domain ownership, evidence/memory semantics, state machines, public contracts and any gap not verified in an external project.

## Unknown gaps / PoC blockers

- Exact DeerFlow commit, license and callable runtime contract.
- Pi permission/sandbox integration and cancel/resume mapping.
- Provider live response, rate/cost/terms and provenance normalization.
- Crawler license, SSRF/network isolation and browser fallback behavior.
- Queue choice after final Python/DB architecture.
- Security enforcement and secret redaction evidence.

No row is an accepted ADR. M0-GATE-001 must remain non-PASS.

## Queue/workflow source audit

| Candidate | Repository / reviewed commit | License | Relevant source anchors | Capability candidate | Classification | Evidence gap |
|---|---|---|---|---|---|---|
| Arq | https://github.com/python-arq/arq @ `5ee4b48cf6faf4dc181f1ccb76dfb1bc1fedf9bf` | MIT | `arq/`, `docs/`, `tests/` | Redis-backed async jobs, retry/scheduling candidate | INFRASTRUCTURE_OPTION | DB/outbox fit, heartbeat/cancel/recovery semantics not mapped |
| RQ | https://github.com/rq/rq @ `f51f9746de5caacc88c91a7c09656bf50616b735` | `NOASSERTION` metadata; inspect `LICENSE` before use | `rq/`, `docs/`, `tests/` | Redis queue and worker candidate | INFRASTRUCTURE_OPTION / UNKNOWN | License confirmation, durable workflow semantics and PI state mapping |
| Celery | https://github.com/celery/celery @ `2c42237d375718a84f01f3a7b4eb12a85e061e37` | `NOASSERTION` metadata; inspect `LICENSE` before use | `celery/`, `docs/`, `t/` | distributed task/retry/scheduling candidate | INFRASTRUCTURE_OPTION / UNKNOWN | operational complexity, cancel/recovery semantics and stack fit |
| Temporal Python SDK | https://github.com/temporalio/sdk-python @ `1c30f89b1f7fd50117f138bed2f4e96d93cd2b0b` | MIT | `temporalio/`, `tests/`, `README.md` | durable workflow/retry/timer candidate | INFRASTRUCTURE_OPTION | external Temporal service, operational footprint and contract fit |

These rows are decision input only. No queue or database choice is accepted by M0.
