# TASK-M0-006 — Audit discovery algorithm references

Task ID: TASK-M0-006  
Title: Audit discovery algorithm references  
Milestone: M0  
Priority: P0  
Status: PARTIAL  
Owner Agent: Workspace Coding Agent  
Depends On: TASK-M0-001  
Blocks: TASK-M0-013

## Objective

审计 MindSearch、STORM/Co-STORM、Alibaba DeepResearch family 及其他参考，形成 Strategy Cards。

## Scope

逐项回答 perspective discovery、dynamic graph、question expansion、context compression、outline construction、gap detection、stopping、source coverage、candidate verification。

## Out of Scope

不实现 Discovery Engine，不接受任何策略为默认策略。

## Allowed Files

- `docs/tasks/m0/TASK-M0-006.md`
- `docs/audit/m0/ALGORITHM_REUSE_AUDIT.md`
- `docs/audit/m0/STRATEGY_REGISTRY.md`

## New Files Allowed

仅允许更新上述审计/登记文件。

## Forbidden Files

Discovery、Radar、Ranking、Evidence implementation；dependency manifests；ADR acceptance。

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

Source/research inspection、strategy card schema validation、`git diff --check`。

## Commands To Run

`rg -n "Perspective|Dynamic graph|Question expansion|Stopping|Source coverage" docs/audit/m0/ALGORITHM_REUSE_AUDIT.md`; `git diff --check`。

## Acceptance Criteria

每张 Strategy Card 有来源、能力、证据等级、适配边界、失败模式、未知项和 PoC 问题；不写成已冻结策略。

## Evidence Required

URL/commit/version/license、relevant code/paper sections、behavior/interface evidence、fit and maintenance notes。

## Architecture Constraints

保持 Discovery、Evidence、Radar 的既有 ownership 假设，不作裁决。

## Stop Conditions

需要改变 Discovery state machine、Search ownership 或新增大型 dependency。

## Execution Result

Status: PARTIAL  
Evidence: STORM, MindSearch and Alibaba DeepResearch rows pin remote commits/licenses; Strategy Cards answer all requested capability dimensions.  
Artifacts Changed: `ALGORITHM_REUSE_AUDIT.md`, `STRATEGY_REGISTRY.md`.  
Acceptance Result: PARTIAL — reference strategies identified; no default strategy accepted.  
Verification: GitHub metadata/tree inspection and source/document review.  
Known Limitations: Stop thresholds, ownership and benchmark evidence deferred to M1/PoC.  
Discovered Delta: Dynamic graph and perspective strategies are references only until ownership and cost behavior are proven.
