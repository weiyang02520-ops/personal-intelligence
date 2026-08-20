# TASK-M0-003 — Audit DeerFlow extension surface

Task ID: TASK-M0-003  
Title: Audit DeerFlow extension surface  
Milestone: M0  
Priority: P0  
Status: PARTIAL  
Owner Agent: Workspace Coding Agent  
Depends On: TASK-M0-001  
Blocks: TASK-M0-013

## Objective

确认 DeerFlow 优先扩展方式是 skills、MCP、custom tools、API、custom agents 还是 deep fork。

## Scope

检查不修改 core 的扩展点、必须 patch 的位置、升级冲突风险，输出 Recommended Extension Hierarchy。

## Out of Scope

不 fork、patch 或运行 DeerFlow；不改变 PI 模块边界或 Runtime contract。

## Allowed Files

- `docs/tasks/m0/TASK-M0-003.md`
- `docs/audit/m0/RUNTIME_AUDIT.md`

## New Files Allowed

仅允许更新 `docs/audit/m0/RUNTIME_AUDIT.md`。

## Forbidden Files

Product Core、PoC/M1+ source、dependency manifests、ADR acceptance、Public API、Domain model。

## Required Interfaces
N/A — Audit Task；仅记录上游扩展面，不声明 PI contract。
## Required Functions
N/A — Audit Task。
## Required Behavior
N/A — Audit Task。
## Required Errors
N/A — Audit Task。
## Required Events
N/A — Audit Task。

## Required Tests

Source inspection、extension point evidence scan、`git diff --check`。

## Commands To Run

`rg -n "Extension|skills|MCP|custom tools|deep fork" docs/audit/m0/RUNTIME_AUDIT.md`; `git diff --check`。

## Acceptance Criteria

扩展层级按证据分级，明确 upgrade risk；未验证内容标 UNKNOWN。

## Evidence Required

Relevant files/interfaces/classes/functions、extension behavior claim、integration/security unknowns、decision candidate。

## Architecture Constraints

禁止将 extension hierarchy 写成已接受架构。

## Stop Conditions

需要改变 Runtime boundary、依赖方向、核心权限或 Public API。

## Execution Result

Status: PARTIAL  
Evidence: Extension hierarchy records API → skills/MCP/tools → thin gateway → local patch → deep fork, with source anchors and upgrade risks.  
Artifacts Changed: `RUNTIME_AUDIT.md`.  
Acceptance Result: PARTIAL — hierarchy is reviewable, not behavior-tested.  
Verification: DeerFlow repository map, extension example/config/docs inspection.  
Known Limitations: No upgrade simulation or PI integration.  
Discovered Delta: Deep fork is not a default candidate; extension surface still requires explicit boundary review.
