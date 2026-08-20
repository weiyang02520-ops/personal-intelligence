# TASK-POC-002 — Core API research lifecycle spike

Task ID: TASK-POC-002  
Title: Core API research lifecycle spike  
Milestone: PoC  
Priority: P0  
Status: READY  
Depends On: TASK-POC-001  
Blocks: TASK-POC-003..005, TASK-POC-010

## Objective

验证最小 `POST /research`、`GET /research/{id}`、FakeRuntime 异步执行和 PostgreSQL Candidate A 持久化。

## Scope

PoC lifecycle semantics: `CREATED`, internal RUNNING-like, `COMPLETED`; process-boundary persistence and worker execution.

## Out of Scope

不冻结最终 Research status/stage，不实现 Discovery、Runtime production adapter、full Domain 或 M1。

## Allowed Files

`apps/core/`, `apps/web/`, `tests/`, `benchmarks/`, PoC config and docs.

## New Files Allowed

Minimal FastAPI/Core lifecycle, persistence models, FakeRuntime, tests and local test runner.

## Forbidden Files

M1 Domain/Discovery、final API registry、production migrations、real credentials、unapproved DB decision.

## Required Interfaces

PoC HTTP API `POST /research`, `GET /research/{id}`; FakeRuntime adapter boundary.

## Required Functions

Create research, read research, enqueue/execute FakeRuntime, persist state.

## Required Behavior

POST returns ID; worker completes asynchronously; GET eventually reads completed state after process boundary where configured.

## Required Errors

Not found, invalid request, persistence failure via PoC error envelope.

## Required Events

Internal lifecycle event only; PublicEvent projection is POC-003.

## Required Tests

API contract, async completion, PostgreSQL persistence, process-boundary read, failure response.

## Commands To Run

`python -m pytest -q tests/poc`; isolated PostgreSQL runner; `git diff --check`.

## Acceptance Criteria

All required lifecycle behavior passes without Discovery code; state names are clearly marked PoC-only.

## Evidence Required

API/test output, database URL mode, observed lifecycle, limitations, candidate DB conclusion and discovered delta.

## Architecture Constraints

PostgreSQL is Candidate A, not accepted production database. Do not let FakeRuntime types leak into Product Core.

## Stop Conditions

Need to resolve final state semantics, database ADR, or production migration policy.

## Execution Result

Status: PENDING  
Evidence: —  
Artifacts Changed: —  
Acceptance Result: —  
Verification: —  
Known Limitations: —  
Discovered Delta: —
