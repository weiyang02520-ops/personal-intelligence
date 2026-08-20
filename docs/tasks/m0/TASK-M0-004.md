# TASK-M0-004 — Audit Pi runtime alternative

Task ID: TASK-M0-004  
Title: Audit Pi runtime alternative  
Milestone: M0  
Priority: P0  
Status: PARTIAL  
Owner Agent: Workspace Coding Agent  
Depends On: TASK-M0-001  
Blocks: TASK-M0-013

## Objective

验证 Pi 是否能作为 `IF-RUNTIME-001` alternate runtime。

## Scope

审计 session start、events、tool registration、model runtime、headless/RPC、cancel/resume、subagents、context control，并输出 DeerFlow vs Pi contract comparison。

## Out of Scope

现在选择 Pi；引入 Pi dependency；修改 Runtime contract 或 PI Core。

## Allowed Files

- `docs/tasks/m0/TASK-M0-004.md`
- `docs/audit/m0/RUNTIME_AUDIT.md`

## New Files Allowed

仅允许更新 `docs/audit/m0/RUNTIME_AUDIT.md`。

## Forbidden Files

Product Core、dependency manifests、PoC/M1+、ADR acceptance、上游源码修改。

## Required Interfaces
`IF-RUNTIME-001` alternate comparison only。
## Required Functions
N/A — Audit Task。
## Required Behavior
N/A — Audit Task。
## Required Errors
N/A — Audit Task。
## Required Events
N/A — Audit Task。

## Required Tests

Local source inspection against recorded Pi commit; no untrusted upstream execution; `git diff --check`。

## Commands To Run

`rg -n "Pi|IF-RUNTIME-001|headless|RPC|permission" docs/audit/m0/RUNTIME_AUDIT.md`; `git diff --check`。

## Acceptance Criteria

Pi capability claims cite exact local/upstream evidence; permission gap and integration unknowns are explicit; no selection is made.

## Evidence Required

Repository, exact commit/version, license, relevant files/interfaces/functions, code/interface/behavior/security evidence, maintenance and failure modes.

## Architecture Constraints

No runtime selection or dependency change.

## Stop Conditions

需要接受 Pi/DeerFlow、改变 Runtime boundary 或执行未经隔离的上游代码。

## Execution Result

Status: PARTIAL  
Evidence: Pi snapshot pinned to `2e4d23959485279aa2da1a45103de2ea22d46395`, MIT, package `@earendil-works/pi-agent-core` `0.84.1`, README/AGENTS/package anchors.  
Artifacts Changed: `RUNTIME_AUDIT.md`.  
Acceptance Result: PARTIAL — alternate-runtime candidate is evidenced, not selected.  
Verification: Local source inspection; no Pi runtime execution.  
Known Limitations: No exact IF-RUNTIME-001 mapping, cancel/resume test or sandbox proof.  
Discovered Delta: Pi explicitly lacks built-in filesystem/process/network/credential permission enforcement; external sandboxing is required.
