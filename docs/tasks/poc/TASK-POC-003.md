# TASK-POC-003 — Public SSE event spike

Task ID: TASK-POC-003  
Title: Public SSE event spike  
Milestone: PoC  
Priority: P0  
Status: COMPLETE
Depends On: TASK-POC-002  
Blocks: TASK-POC-010, TASK-POC-012

## Objective

证明 FakeRuntime → internal event → PI-owned PublicEvent projection → SSE → Web client，并支持断线后按 monotonically increasing sequence 补事件。

## Scope

Public event SPI, SSE endpoint, event sequence/replay storage and reconnect contract.

## Out of Scope

不暴露 DeerFlow/LangGraph SSE，不实现生产 event registry、full UI 或 M1 events。

## Allowed Files

`apps/core/`, `apps/web/`, `tests/`, PoC docs.

## New Files Allowed

PublicEvent model, SSE route, replay helper and contract tests.

## Forbidden Files

Runtime-specific DTOs in public modules, M1 event expansion, production broker.

## Required Interfaces

PI-owned public event stream for a research ID.

## Required Functions

Project internal event, append sequence, stream from cursor, reconnect replay.

## Required Behavior

Disconnect does not stop job; reconnect receives missing events in sequence order.

## Required Errors

Invalid cursor, unknown research, replay gap behavior.

## Required Events

At least lifecycle public events with stable PoC names and sequence.

## Required Tests

Contract test for start/disconnect/continue/reconnect; no runtime DTO leakage; monotonic sequence.

## Commands To Run

`python -m pytest -q tests/poc/test_sse.py`; static DTO scan; `git diff --check`.

## Acceptance Criteria

Frontend connects only to PI API; replay works within PoC retention; event projection is PI-owned.

## Evidence Required

SSE test output, sample event envelopes, reconnect result, retention limitation and discovered delta.

## Architecture Constraints

Domain/internal events and Public SSE events remain separate.

## Stop Conditions

Need to expose runtime events directly or change public event semantics.

## Execution Result

Status: COMPLETE
Evidence: `apps/core/events.py`, SSE endpoint, `tests/poc/test_sse.py`
Artifacts Changed: PI-owned public event projection and replay-by-sequence SSE
Acceptance Result: PASS
Verification: `python -m pytest -q tests/poc/test_sse.py`
Known Limitations: In-process streaming is sufficient for PoC evidence; broker/fanout selection remains open.
Discovered Delta: Browser reconnect is represented by `after_sequence`; production Last-Event-ID mapping remains open.
