# TASK-POC-004 — PostgreSQL transaction + outbox spike

Task ID: TASK-POC-004  
Title: PostgreSQL transaction + outbox spike  
Milestone: PoC  
Priority: P0  
Status: COMPLETE
Depends On: TASK-POC-002  
Blocks: TASK-POC-012

## Objective

证明 Research state write 与 DomainEvent/outbox write 的原子性及消费幂等。

## Scope

PostgreSQL transaction, outbox row, commit failure isolation, duplicate publisher delivery and idempotent consumer effect.

## Out of Scope

不建立生产 migration 历史，不接受 PostgreSQL/Outbox ADR，不实现完整 event platform。

## Allowed Files

`apps/core/`, `tests/`, local PoC database scripts and docs.

## New Files Allowed

Minimal schema/bootstrap, transaction service, outbox publisher/consumer and fault tests.

## Forbidden Files

Production migration framework, external queue, final event registry, real data.

## Required Interfaces

Transaction + outbox boundary; idempotent consumer boundary.

## Required Functions

Atomic state/event write, publish once-or-more, idempotent consume.

## Required Behavior

Commit failure leaves neither orphan event nor partial state; duplicate delivery has one consumer effect.

## Required Errors

Commit failure, duplicate event, serialization/database error.

## Required Events

PoC outbox lifecycle event with stable event ID.

## Required Tests

Atomicity fault test and duplicate publisher/consumer idempotency test against isolated PostgreSQL.

## Commands To Run

`python -m pytest -q tests/poc/test_outbox.py`; isolated DB setup; `git diff --check`.

## Acceptance Criteria

Required faults are observed and documented; PostgreSQL remains only Candidate A result.

## Evidence Required

SQL/test output, transaction observations, idempotency proof, limitations and candidate decision input.

## Architecture Constraints

No final persistence choice or migration policy.

## Stop Conditions

Need to change Domain event semantics or accept database architecture.

## Execution Result

Status: COMPLETE
Evidence: `apps/core/events.py`, transaction rollback and idempotency tests
Artifacts Changed: Research/outbox atomic write path and processed-event uniqueness
Acceptance Result: PASS
Verification: `python -m pytest -q tests/poc/test_outbox.py` plus PostgreSQL integration run
Known Limitations: Publisher transport and broker are intentionally not selected.
Discovered Delta: Duplicate delivery protection is consumer-local in this PoC.
