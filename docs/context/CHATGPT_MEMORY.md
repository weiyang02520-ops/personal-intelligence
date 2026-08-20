# CHATGPT_MEMORY

Memory Schema Version: 1
Memory Revision: 1
Last Updated: 2026-08-20
Current Milestone: PRE-M0

## CURRENT TRUTH

[REPO_CONFIRMED] Personal Intelligence 的 Public GitHub 仓库是 `weiyang02520-ops/personal-intelligence`，默认分支为 `main`。

[REPO_CONFIRMED] 当前仓库起始提交为 `690367c4be5b`，当前阶段是 Project Bootstrap / Blueprint Audit。

[REPO_CONFIRMED] Blueprint canonical location 是 `docs/plan(4).md`，其源文件来自 `C:\Users\peng\Desktop\plan.md`，原文完整保留。

[EXTERNAL_REVIEW] 当前审计结论为 `NOT_READY_FOR_M0`：M0 Task packet、canonical artifact names、M0 Gate evidence schema 和 repo continuity 已在本轮形成/记录，但 M0 Task 尚未 READY，需 External ChatGPT Review。

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

## OPEN QUESTIONS

详见 `docs/audit/OPEN_TBDS.md` 和 `docs/audit/SPEC_CONFLICTS.md`。不得将 OPEN/TBD 静默提升为 Design Decision。
