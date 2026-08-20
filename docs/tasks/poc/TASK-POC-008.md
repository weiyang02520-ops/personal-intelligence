# TASK-POC-008 — DeerFlowRuntimeAdapter spike

Task ID: TASK-POC-008  
Title: DeerFlowRuntimeAdapter spike  
Milestone: PoC  
Priority: P0  
Status: READY  
Depends On: TASK-POC-001, TASK-POC-002  
Blocks: TASK-POC-009, TASK-POC-012

## Objective

完成真实 DeerFlow source-level contract extraction，并以 thin `DeerFlowRuntimeAdapter` 验证 start/events/result/cancel/capabilities。

## Scope

Reviewed baseline `a5acc25de6742b2166b3f41c97bd895822277b94`; inspect source paths/functions/classes beyond README/API.md, translate semantics to `IF-RUNTIME-001`, and record contract gaps.

## Out of Scope

不修改 Research Domain，不 deep fork DeerFlow，不凭 mock 宣称 real integration，不引入生产 runtime selection。

## Allowed Files

`apps/core/`, `tests/`, `docs/audit/poc/`, PoC docs/config.

## New Files Allowed

Adapter, source contract notes, controlled fixtures and tests.

## Forbidden Files

Upstream repo edits, Research Domain changes, real credentials in repo/logs, runtime-specific public DTOs.

## Required Interfaces

`IF-RUNTIME-001`, DeerFlowRuntimeAdapter.

## Required Functions

Start, stream events, result, cancel, capabilities; investigate resume/error isolation.

## Required Behavior

Translate DeerFlow semantics into PI contract; failures become explicit CONTRACT GAP.

## Required Errors

Start failure, timeout, cancellation, upstream error, contract gap, credential-blocked.

## Required Events

PI-owned runtime event projection; no raw DeerFlow/LangGraph DTO leakage.

## Required Tests

Source contract tests, adapter unit/contract tests, controlled runtime fixture, real DeerFlow path if credential-free environment permits.

## Commands To Run

`python -m pytest -q tests/poc/test_deerflow_adapter.py`; source inspection; optional isolated gateway test; `git diff --check`.

## Acceptance Criteria

Exact source paths/functions/classes recorded; supported capabilities and gaps are accurate; Research Domain is unchanged.

## Evidence Required

Source anchors, adapter tests, real/mock distinction, credential status, capability matrix, contract gaps and limitations.

## Architecture Constraints

Reviewed upstream commit is pinned; adopted dependency version remains NOT FROZEN. PI owns the outer contract and permission boundary.

## Stop Conditions

Need to patch Product Core, expose raw runtime events, use unavailable credential for unrelated tasks or deep fork.

## Execution Result

Status: PENDING  
Evidence: —  
Artifacts Changed: —  
Acceptance Result: —  
Verification: —  
Known Limitations: —  
Discovered Delta: —
