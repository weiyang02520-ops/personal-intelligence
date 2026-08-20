# TASK-M0-005 — Audit open deep research baselines

Task ID: TASK-M0-005  
Title: Audit open deep research baselines  
Milestone: M0  
Priority: P0  
Status: PARTIAL  
Owner Agent: Workspace Coding Agent  
Depends On: TASK-M0-001  
Blocks: TASK-M0-013

## Objective

审计 LangChain Open Deep Research、GPT Researcher、Deep Searcher 及其他已列候选，识别可避免重复自研的 research loop、compression、citation、query planning、benchmark 能力。

## Scope

记录每个候选的 repository、版本/commit、license、维护状态、相关文件/函数、代码与行为证据、失败模式、集成 fit，并形成 Capability Reuse Map。

## Out of Scope

不复制 research loop，不实现 Deep Search，不确定 Product Core ownership。

## Allowed Files

- `docs/tasks/m0/TASK-M0-005.md`
- `docs/audit/m0/ALGORITHM_REUSE_AUDIT.md`

## New Files Allowed

仅允许更新 `docs/audit/m0/ALGORITHM_REUSE_AUDIT.md`。

## Forbidden Files

Product Core、M1 Discovery/Research code、dependency manifests、ADR acceptance。

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

Repository/source inspection、license/maintenance evidence check、`git diff --check`。

## Commands To Run

`rg -n "research loop|compression|citation|query planning|benchmark" docs/audit/m0/ALGORITHM_REUSE_AUDIT.md`; `git diff --check`。

## Acceptance Criteria

每项能力区分 REUSE/ADAPT/REFERENCE/REJECT/UNKNOWN 候选，不以 README-only 证据宣称可复用。

## Evidence Required

精确来源、版本、相关代码位置、接口/行为/集成/安全证据、维护与失败模式、决策候选。

## Architecture Constraints

只能提出算法参考或集成候选，不改变 Discovery/Evidence/Research ownership。

## Stop Conditions

需要新增大型 dependency、改变 Domain 状态或跨模块 ownership。

## Execution Result

Status: PARTIAL  
Evidence: ODR, GPT Researcher and Deep Searcher rows pin exact remote commits/licenses and relevant repository trees.  
Artifacts Changed: `ALGORITHM_REUSE_AUDIT.md`.  
Acceptance Result: PARTIAL — capability map is complete as reference evidence; no code behavior/integration claim.  
Verification: GitHub metadata/tree inspection; no upstream execution.  
Known Limitations: Framework coupling, citation behavior and benchmark transfer remain open.  
Discovered Delta: Mature research-loop patterns exist, but PI Evidence/Citation ownership remains custom design.
