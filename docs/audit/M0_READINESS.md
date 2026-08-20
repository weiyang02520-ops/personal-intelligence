# Personal Intelligence — M0 Readiness

结论：`NOT_READY_FOR_M0`

这里的“不 ready”指“不能正式把 Coding Agent 交给 TASK-M0-* 并要求其开始施工”。它不否定 M0 作为下一阶段的方向；plan.md 自己已把 M0 Reuse Audit 定义为下一 Gate。

## 判定依据

1. plan.md 当前状态是 `PRE-IMPLEMENTATION / COMPLETE DESIGN DRAFT / Coding NOT STARTED / Architecture NOT FROZEN`，下一 Gate 是 M0 Reuse Audit（PART 16.15.18–16.15.25）。
2. PART 16.1/16.2 规定只有 Spec 已冻结、Task 模板齐全的 Task 才能是 READY；TASK-M0-001..014 没有 Status、Depends On、Allowed Files、Forbidden Files、Commands、Acceptance Criteria、Stop Conditions 等必填字段。
3. M0 产物文件名在 PART 05.8 与 PART 16.5 不一致，M0-001 无法确定 canonical output。
4. M0 依赖的审计结果与 ADR 更新权限没有分离定义；M0-014 可以提出 Gate 结果，但不能自行接受架构 ADR。
5. M0-GATE-001 缺少可验证的 Evidence ID、Owner、Pass Rule 和 Review Record schema。

## TASK-M0-* 状态

| Task | 状态 | 结论 |
|---|---|---|
| TASK-M0-001 | NOT_READY | 方向正确，是解阻后的第一个执行 Task；当前缺完整 Task packet、canonical outputs 和 Gate evidence contract |
| TASK-M0-002..012 | NOT_READY | 依赖统一审计框架，但各自没有完整 Task contract；其中 Runtime/Search/Security 还受未关闭 Contract/TBD 约束 |
| TASK-M0-013 | NOT_READY | 依赖 M0-002..012，且输入输出文件名/决策权限未冻结 |
| TASK-M0-014 | NOT_READY | Gate evidence schema、reviewer、ADR acceptance rule 未定义 |
| M0-GATE-001 | NOT_READY | 还没有任何正式 M0 audit evidence |

## 阻塞 M0 的最小问题集合

只需先解决以下三项，不需要重写整个计划书：

1. 按 PART 16.2 为 M0-001..014 补齐最小 Task packet；初始状态保持 NOT_READY。
2. 统一 M0 审计产物命名，并确定 `REUSE_AUDIT`、分项 Audit、Reuse Matrix、Strategy Registry、ADR updates 的关系。
3. 明确 M0 审计只能生成 evidence/recommendation，架构接受必须通过独立 ADR/Architecture Review；同时为 M0-GATE-001 建立最小 Gate evidence 表。

这三项不要求选择 Runtime、数据库、Queue、Provider，也不要求实现 PoC；它们只是让 M0 审计本身可以在不越权的前提下启动。

## 解阻后的第一步

完成上述最小集合后，第一个执行 Task 应为：`TASK-M0-001 — Create reuse audit framework`。

执行范围只允许建立审计模板、证据等级、PASS/PARTIAL/FAIL/UNKNOWN 规则、复用模式和报告 schema；不得开始 DeerFlow、Search Provider、Radar、Ranking 或 Product Core 实现。

在 TASK-M0-001 完成并通过其文档验证前，不应执行 TASK-M0-002..014；在 M0-GATE-001 PASS 前，不应进入 Physical Architecture PoC。
