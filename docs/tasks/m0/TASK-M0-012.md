# TASK-M0-012 — Audit security/sandbox options

Task ID: TASK-M0-012  
Title: Audit security/sandbox options  
Milestone: M0  
Priority: P0  
Status: PARTIAL  
Owner Agent: Workspace Coding Agent  
Depends On: TASK-M0-001  
Blocks: TASK-M0-013

## Objective

确认 external runtime、sandbox、tool permissions、network isolation 的可复用能力，并检查 DeerFlow sandbox boundary 是否满足 PI Security Contract。

## Scope

记录 trust boundary、permission enforcement、network/file isolation、secret handling、failure modes、maintenance 与验证缺口。

## Out of Scope

不运行不可信工具，不实现 sandbox，不改 Security Contract，不接受安全 ADR。

## Allowed Files

- `docs/tasks/m0/TASK-M0-012.md`
- `docs/audit/m0/REUSE_DECISION_MATRIX.md`
- `docs/audit/m0/RUNTIME_AUDIT.md`

## New Files Allowed

仅允许更新上述审计文件。

## Forbidden Files

Runtime/sandbox implementation、secrets、network policy、database、Public API、ADR acceptance。

## Required Interfaces
N/A — Audit Task；PI Security Contract 仅为比较条件。
## Required Functions
N/A — Audit Task。
## Required Behavior
N/A — Audit Task。
## Required Errors
N/A — Audit Task。
## Required Events
N/A — Audit Task。

## Required Tests

Source/document inspection、security evidence validation、`git diff --check`；不执行外部工具。

## Commands To Run

`rg -n "sandbox|permission|network isolation|trust boundary" docs/audit/m0/RUNTIME_AUDIT.md docs/audit/m0/REUSE_DECISION_MATRIX.md`; `git diff --check`。

## Acceptance Criteria

安全结论按 verified / partial / unknown 记录；明确 Pi 的 permission gap 与 DeerFlow boundary 的未验证项。

## Evidence Required

Exact source/version、security-relevant files/interfaces、integration/behavior evidence、maintenance and failure modes、PoC questions。

## Architecture Constraints

所有 external content/tool input 默认不可信；不得弱化 permission boundary。

## Stop Conditions

需要改变 trust boundary、允许无隔离执行、修改 Security Contract 或引入大型 dependency。

## Execution Result

Status: PARTIAL  
Evidence: Pi permission gap and DeerFlow sandbox/guardrail/RBAC boundary sources are recorded in `RUNTIME_AUDIT.md`.  
Artifacts Changed: `RUNTIME_AUDIT.md`, `REUSE_DECISION_MATRIX.md`.  
Acceptance Result: PARTIAL — security reuse cannot be claimed; trust/permission proof remains open.  
Verification: Official source/document inspection; no untrusted execution.  
Known Limitations: No sandbox integration or network/file isolation test.  
Discovered Delta: External sandbox plus explicit permission enforcement is PI custom-design territory.
