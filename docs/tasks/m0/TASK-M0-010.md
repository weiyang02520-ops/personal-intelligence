# TASK-M0-010 — Audit UI references

Task ID: TASK-M0-010  
Title: Audit UI references  
Milestone: M0  
Priority: P0  
Status: PARTIAL  
Owner Agent: Workspace Coding Agent  
Depends On: TASK-M0-001  
Blocks: TASK-M0-013

## Objective

审计 Morphic、Vane、DeerFlow frontend、CC Switch visual reference，输出 UI reuse/reference matrix。

## Scope

提取可复用 primitives、interaction patterns、information hierarchy；记录许可证、代码/视觉证据、适配边界和维护风险。

## Out of Scope

不复制产品品牌/UI，不写前端，不锁定 exact colors/widths/radius。

## Allowed Files

- `docs/tasks/m0/TASK-M0-010.md`
- `docs/audit/m0/UI_REFERENCE_AUDIT.md`

## New Files Allowed

仅允许更新 `docs/audit/m0/UI_REFERENCE_AUDIT.md`。

## Forbidden Files

`apps/`、UI source、brand assets、dependency manifests、M4 design freeze、ADR acceptance。

## Required Interfaces
N/A — Audit Task。
## Required Functions
N/A — Audit Task。
## Required Behavior
N/A — Audit Task。
## Required Errors
N/A — Audit Task。
## Required Events
N/A — Audit Task。

## Required Tests

Source/visual reference inspection、license evidence check、`git diff --check`。

## Commands To Run

`rg -n "primitive|interaction|hierarchy|Morphic|Vane|DeerFlow|CC Switch" docs/audit/m0/UI_REFERENCE_AUDIT.md`; `git diff --check`。

## Acceptance Criteria

明确 code reuse 与 visual reference 的区别；未确认 license/implementation 的项目标 UNKNOWN。

## Evidence Required

Repository/URL/version/license、relevant components/patterns、behavior/maintenance/security notes、decision candidate。

## Architecture Constraints

UI 只能调用 PI API 的设计方向不变；不修改 Public API。

## Stop Conditions

需要复制品牌、改变 UI boundary 或新增 UI dependency。

## Execution Result

Status: PARTIAL  
Evidence: UI reference matrix separates Morphic/Vane/DeerFlow/CC Switch visual or primitive references from code reuse; DeerFlow source commit is recorded.  
Artifacts Changed: `UI_REFERENCE_AUDIT.md`.  
Acceptance Result: PARTIAL — information hierarchy candidates are recorded; component/license verification remains open.  
Verification: Repository/reference inspection; no UI code copied.  
Known Limitations: Component-level behavior and reuse licensing review is incomplete.  
Discovered Delta: UI references remain non-blocking and do not authorize brand or frontend implementation.
