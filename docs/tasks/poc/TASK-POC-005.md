# TASK-POC-005 — Job execution/recovery spike

Task ID: TASK-POC-005  
Title: Job execution/recovery spike  
Milestone: PoC  
Priority: P0  
Status: READY  
Depends On: TASK-POC-002, TASK-POC-004  
Blocks: TASK-POC-012

## Objective

验证最小 PostgreSQL-backed Job mechanism 的 enqueue、worker、retry、heartbeat、restart recovery。

## Scope

Isolated job table, worker lease/heartbeat, retry, worker kill/restart recovery.

## Out of Scope

不引入 Celery、Temporal、Redis，除非简单候选无法证明 contract；不实现 Radar Scheduler。

## Allowed Files

`apps/core/`, `tests/`, local scripts and PoC docs.

## New Files Allowed

Minimal job repository/worker/recovery harness and tests.

## Forbidden Files

External queue infrastructure by default, production scheduler, Radar, M1 jobs.

## Required Interfaces

Job enqueue/worker/recovery boundary.

## Required Functions

Enqueue, claim, heartbeat, retry, complete/fail, recover stale job.

## Required Behavior

Kill worker during execution; restart worker; job eventually reaches correct final state.

## Required Errors

Lease expired, retryable failure, terminal failure, duplicate claim.

## Required Events

PoC job state events sufficient for evidence.

## Required Tests

Worker kill/restart integration test with isolated database.

## Commands To Run

`python -m pytest -q tests/poc/test_jobs.py`; isolated worker harness; `git diff --check`.

## Acceptance Criteria

Simple candidate proves required semantics or records evidence for next candidate; no fashionable infrastructure added without evidence.

## Evidence Required

Recovery timeline, DB rows, test output, complexity observation, known limitations and candidate outcome.

## Architecture Constraints

No queue selection accepted; job state remains PoC semantics.

## Stop Conditions

Need Redis/Temporal/Celery without a failed simpler candidate or need to change Job state contract.

## Execution Result

Status: PENDING  
Evidence: —  
Artifacts Changed: —  
Acceptance Result: —  
Verification: —  
Known Limitations: —  
Discovered Delta: —
