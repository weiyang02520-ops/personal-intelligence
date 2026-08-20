# TASK-M0-011 — Audit queue/workflow infrastructure

Task ID: TASK-M0-011  
Title: Audit queue/workflow infrastructure  
Milestone: M0  
Priority: P0  
Status: PARTIAL  
Owner Agent: Workspace Coding Agent  
Depends On: TASK-M0-001  
Blocks: TASK-M0-013

## Objective

按最终 Python stack 评估 DB queue、light Python queue、Temporal-like durable workflow 及其它成熟选择，寻找满足 retry/schedule/heartbeat/cancel/recovery 的最简单方案。

## Scope

形成 Job Infrastructure Decision Input，记录候选 exact version/license、接口、运行行为、运维、安全、失败模式和 PI fit。

## Out of Scope

不选择 queue，不建 DB/outbox，不实现 worker/scheduler，不改变 runtime/database。

## Allowed Files

- `docs/tasks/m0/TASK-M0-011.md`
- `docs/audit/m0/REUSE_DECISION_MATRIX.md`
- `docs/audit/m0/OPEN_SOURCE_AUDIT.md`

## New Files Allowed

仅允许更新上述审计文件。

## Forbidden Files

Queue/worker implementation、migration、DB schema、dependency manifests、ADR acceptance。

## Required Interfaces
N/A — Audit Task；Job Contract 只作为评价维度。
## Required Functions
N/A — Audit Task。
## Required Behavior
N/A — Audit Task。
## Required Errors
N/A — Audit Task。
## Required Events
N/A — Audit Task。

## Required Tests

Official/source inspection、capability evidence check、`git diff --check`；不运行外部 worker。

## Commands To Run

`rg -n "retry|schedule|heartbeat|cancel|recovery" docs/audit/m0/REUSE_DECISION_MATRIX.md`; `git diff --check`。

## Acceptance Criteria

候选按最小能力与运维复杂度比较，保留 unresolved DB/runtime dependencies 和 PoC questions。

## Evidence Required

Repository/version/license、relevant APIs/classes、behavior/integration/security evidence、maintenance and failure modes。

## Architecture Constraints

不得把最终 Python stack、DB、Queue、Outbox 写成已冻结。

## Stop Conditions

需要新增大型 dependency、接受 queue/DB ADR 或修改 Job state semantics。

## Execution Result

Status: PARTIAL  
Evidence: `REUSE_DECISION_MATRIX.md` compares DB queue/light Python/durable workflow families and records retry/schedule/heartbeat/cancel/recovery questions.  
Artifacts Changed: `REUSE_DECISION_MATRIX.md`, `OPEN_SOURCE_AUDIT.md`.  
Acceptance Result: PARTIAL — decision input exists; no queue/DB/stack selection.  
Verification: Source/document capability review and classification scan.  
Known Limitations: Exact final Python stack and PoC persistence contract are unresolved.  
Discovered Delta: Queue choice remains a PoC/ADR input and cannot block evidence preparation itself.
