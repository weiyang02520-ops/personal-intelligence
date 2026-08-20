# TASK-M0-001 — Create reuse audit framework

Task ID: TASK-M0-001  
Title: Create reuse audit framework  
Milestone: M0  
Priority: P0  
Status: PASS  
Owner Agent: Workspace Coding Agent  
Depends On: None  
Blocks: TASK-M0-002..012

## Objective

建立统一的 PASS / PARTIAL / FAIL / UNKNOWN 审计状态、Evidence Level、复用分类和报告 schema。

## Scope

定义审计模板、证据要求、决策标准、风险字段，以及每个第三方项目必须记录的 repository、commit/version、license、active status、capabilities、extension points、hard dependencies、failure modes、reuse mode。

## Out of Scope

不审计具体项目内容；不实现 Product Core、Runtime、Search、Crawler、Radar、Ranking、UI 或基础设施。

## Allowed Files

- `docs/tasks/m0/TASK-M0-001.md`
- `docs/audit/m0/REUSE_AUDIT.md`
- `docs/audit/m0/OPEN_SOURCE_AUDIT.md`
- `docs/audit/m0/REUSE_DECISION_MATRIX.md`

## New Files Allowed

- `docs/audit/m0/REUSE_AUDIT.md`

## Forbidden Files

`docs/plan(4).md`、Product Core、PoC/M1+ source、database/migration、ADR acceptance、Public API、Domain state、Dependency Direction。

## Required Interfaces
N/A — Audit Task.
## Required Functions
N/A — Audit Task.
## Required Behavior
Document schema only; no runtime behavior may be added.
## Required Errors
N/A — Audit Task.
## Required Events
N/A — Audit Task.

## Required Tests

Document validation only: required-field scan, canonical path scan, `git diff --check`。

## Commands To Run

`rg -n "Evidence Level|PASS|PARTIAL|FAIL|UNKNOWN|reuse mode" docs/audit/m0/REUSE_AUDIT.md`; `git diff --check`。

## Acceptance Criteria

1. Later M0 audits can use one schema.
2. README-only claims are explicitly weaker than code/API/behavior evidence.
3. Classifications include REUSE, ADAPT, REFERENCE, REJECT and UNKNOWN; plan reuse modes remain mappable.
4. No architecture decision is accepted.

## Evidence Required

Changed files, validation commands/output, output artifact, known limitations, checkpoint reference, discovered delta.

## Architecture Constraints

Audit evidence may recommend options only. It may not select Runtime, DB, Queue, Provider, module ownership or Public API.

## Stop Conditions

Contradictory spec, missing contract, credential requirement, secret exposure, untrusted code execution request, or architecture decision required.

## Execution Result

Status: PASS  
Evidence: `docs/audit/m0/REUSE_AUDIT.md` defines schema, levels, classifications and no-ADR rule.  
Artifacts Changed: `REUSE_AUDIT.md`, umbrella/index references.  
Acceptance Result: PASS — later M0 audits have one required record format.  
Verification: Required-field review and `git diff --check`.  
Known Limitations: Framework does not prove any third-party behavior.  
Discovered Delta: Legacy PART 05 names are mapped as aliases; canonical files are under `docs/audit/m0/`.
