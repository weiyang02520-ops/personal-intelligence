# TASK-M0-002 — Audit DeerFlow runtime contract

Task ID: TASK-M0-002  
Title: Audit DeerFlow runtime contract  
Milestone: M0  
Priority: P0  
Status: PARTIAL  
Owner Agent: Workspace Coding Agent  
Depends On: TASK-M0-001  
Blocks: TASK-M0-013

## Objective

代码级验证 DeerFlow 是否可实现 `IF-RUNTIME-001`。

## Scope

审计 start/status/cancel/stream events/model selection/agent selection/skills/MCP/files/sandbox/memory/resume/error isolation；区分 README 声明和可从外部可靠调用的代码/API；记录 thin gateway patch 点。

## Out of Scope

不修改 PI Core Architecture，不选择 DeerFlow 为默认 Runtime，不实现 Adapter 或 PoC。

## Allowed Files

- `docs/tasks/m0/TASK-M0-002.md`
- `docs/audit/m0/RUNTIME_AUDIT.md`
- `docs/audit/m0/OPEN_SOURCE_AUDIT.md`

## New Files Allowed

仅允许上述审计 artifact（若已有则更新）。

## Forbidden Files

`docs/plan(4).md`、`apps/`、`packages/`、`src/`、`infra/`、migration、ADR acceptance、Runtime implementation。

## Required Interfaces
`IF-RUNTIME-001` 作为审计对象。
## Required Functions
N/A — Audit Task；不得补造 contract。
## Required Behavior
N/A — Audit Task；不得把上游行为写成 PI behavior。
## Required Errors
N/A — Audit Task。
## Required Events
N/A — Audit Task。

## Required Tests

Source/API inspection, evidence-level validation, `git diff --check`；不执行上游代码。

## Commands To Run

`rg -n "DeerFlow|IF-RUNTIME-001" docs/audit/m0/RUNTIME_AUDIT.md`; `git diff --check`。

## Acceptance Criteria

每项能力有 source/reference、版本或 commit、证据等级、状态、failure mode、gateway patch note 和 unknown gap。

## Evidence Required

Repository URL、exact commit/version、license、relevant files/interfaces/classes/functions、claim/code/interface/behavior/integration/security evidence、maintenance、fit、decision candidate。

## Architecture Constraints

结论只能是 evidence-backed candidate；不接受 Runtime ADR。

## Stop Conditions

需要改 Runtime boundary、PI Core、Public API、权限模型，或无法在不凭猜测的情况下给出证据。

## Execution Result

Status: PARTIAL  
Evidence: `RUNTIME_AUDIT.md` pins DeerFlow `a5acc25de6742b2166b3f41c97bd895822277b94`, MIT, repository tree and official API/extension references.  
Artifacts Changed: `RUNTIME_AUDIT.md`.  
Acceptance Result: PARTIAL — interface evidence exists; behavior/integration/security remain unverified.  
Verification: GitHub API tree/metadata and official API/docs inspection; no upstream execution.  
Known Limitations: No live credential/API test; exact PI adapter contract is not accepted.  
Discovered Delta: DeerFlow exposes documented Gateway/SSE/thread/file/skill/MCP surfaces, but RBAC/security proof remains open.
