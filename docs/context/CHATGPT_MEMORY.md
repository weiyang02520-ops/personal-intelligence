# CHATGPT_MEMORY

Memory Schema Version: 1
Memory Revision: 3
Last Updated: 2026-08-20
Current Milestone: Physical Architecture PoC

## CURRENT TRUTH

[REPO_CONFIRMED] Personal Intelligence 的 Public GitHub 仓库是 `weiyang02520-ops/personal-intelligence`，默认分支为 `main`。

[REPO_CONFIRMED] 当前 Physical Architecture PoC baseline 为 `bd12271c6e2cdc3a2e3e8fef440c47aaf86cfe82`；后续 checkpoint 不写自引用 Final HEAD。

[REPO_CONFIRMED] Blueprint canonical location 是 `docs/plan(4).md`，其源文件来自 `C:\Users\peng\Desktop\plan.md`，原文完整保留。

[EXTERNAL_REVIEW] `M0-GATE-001 PASS_WITH_NOTES`；允许 POC-001..012 连续执行，必须在 POC-GATE-001 External Review 停止。

## USER INTENT

[USER_STATED] Personal Intelligence 的价值在于跨路线、跨来源发现、证据、个人长期状态和可解释推荐，不是普通 AI 搜索框。

[USER_STATED] Workspace Agent 负责执行、测试、文档、commit、push、remote verify，并在 Gate 停止；External ChatGPT 负责独立审查。

[USER_STATED] 新项目默认使用 Public GitHub 仓库；本项目已存在正确的 Public 仓库，因此没有创建第二个仓库。

## ARCHITECTURE INTENT

[DESIGN_DECISION] plan.md 要求 Runtime 可替换、Search 统一归 PI SearchGateway、Evidence/Memory/Radar/Discovery State 属于 PI Core，Coding Agent 不拥有架构决策权。

[UNCERTAIN] backend、database、queue、Runtime selection、Public API/SSE 等仍需 M0/PoC/ADR 验证，不能当作已冻结方案。

## IMPORTANT EXTERNAL REVIEW FINDINGS

[EXTERNAL_REVIEW] Blueprint 覆盖到 PART 16，但仍是 Complete Design Draft，不是 Architecture Frozen。

[EXTERNAL_REVIEW] Requirement → Use Case → Module → Component → Function → Test → Task → Milestone → Gate 的实际 Map 尚未闭合；大量 Function 缺 Test ID，M0 Task 缺少完整 Task Template 字段。

[EXTERNAL_REVIEW] 本 M0 batch 已补齐 Task Packet、canonical audit artifacts、M0 traceability slice 与 Gate Evidence；审计结果仍保留 PARTIAL/UNKNOWN，不等于架构冻结。

[EXTERNAL_REVIEW] PoC must distinguish reviewed upstream commit from adopted/frozen dependency version, and Decision Classification from Plan Reuse Mode.

## OPEN QUESTIONS

详见 `docs/audit/OPEN_TBDS.md` 和 `docs/audit/SPEC_CONFLICTS.md`。不得将 OPEN/TBD 静默提升为 Design Decision。
