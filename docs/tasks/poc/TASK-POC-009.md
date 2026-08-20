# TASK-POC-009 — Runtime tool bridge spike

Task ID: TASK-POC-009  
Title: Runtime tool bridge spike  
Milestone: PoC  
Priority: P0  
Status: READY  
Depends On: TASK-POC-006, TASK-POC-008  
Blocks: TASK-POC-012

## Objective

证明 DeerFlow 通过 PI-controlled Search tool bridge 访问 SearchGateway，且不接收 raw provider key。

## Scope

Minimum bounded tool surface, allowlist, PI adapter/gateway/sandbox enforcement split and disallowed-call behavior.

## Out of Scope

不扩展 Runtime authorization beyond PoC boundary，不把 DeerFlow guardrails/RBAC 当成完整 PI security。

## Allowed Files

`apps/core/`, `tests/`, PoC docs.

## New Files Allowed

Tool bridge, allowlist policy, controlled runtime fixture and security tests.

## Forbidden Files

Provider keys, broad tool registry, direct provider call from Runtime, production permission system.

## Required Interfaces

PI Search tool bridge; bounded allowlist interface.

## Required Functions

Allow call, deny call, forward normalized search request, redact credentials.

## Required Behavior

Allowed search reaches SearchGateway; disallowed tool call cannot silently execute; Runtime never receives provider key.

## Required Errors

Tool denied, malformed request, provider unavailable, secret boundary violation.

## Required Events

Tool call audit event without secret content.

## Required Tests

Allowlist, deny path, provider-key non-exposure, bridge contract and runtime-to-PI path.

## Commands To Run

`python -m pytest -q tests/poc/test_tool_bridge.py`; secret scan; `git diff --check`.

## Acceptance Criteria

Enforcement location is documented as PI/adapter/sandbox; no unsupported DeerFlow authorization claim.

## Evidence Required

Tool traces, deny result, secret scan, enforcement matrix and limitations.

## Architecture Constraints

PI owns outer permission boundary; Runtime receives minimum bounded tool surface.

## Stop Conditions

Provider key exposure, silent disallowed execution, or need to weaken security contract.

## Execution Result

Status: PENDING  
Evidence: —  
Artifacts Changed: —  
Acceptance Result: —  
Verification: —  
Known Limitations: —  
Discovered Delta: —
