# Personal Intelligence — Blueprint Audit

审计输入：`C:\Users\peng\Desktop\plan.md`

审计日期：2026-08-20

审计结论：`NOT_READY_FOR_M0`

## 1. 审计范围与方法

本轮完整读取并结构化扫描了 plan.md 全文：107,481 行、835,619 个字符。覆盖 PART 01–16，以及所有 Requirement、Use Case、Domain Model、Module、Interface、Function、API、Event、Error、Test、Task、Milestone、Gate、ADR、TBD/VERIFY 和状态文本。

同时检查了当前工作区和桌面候选目录：工作区 Git 树存在大量与本项目无关的既有修改，不能直接作为 PI 项目根目录。已确认并克隆正确的 Public 仓库 `weiyang02520-ops/personal-intelligence`，并将 plan.md 复制为仓库内 canonical Blueprint。

本轮没有修改 plan.md、没有实现 M1/M2/M3/M4 功能、没有替代任何未冻结技术方案。

## 2. 文档覆盖索引

| 区域 | 文档内容 | 当前判断 |
|---|---|---|
| PART 01 | 项目宪章、标识符、Reuse First、Core Ownership、Dependency Direction、Freeze 原则 | 方向明确，但非冻结状态 |
| PART 02–03 | Product Requirements、页面结构、User Flow | 覆盖较完整；存在重复索引和状态未冻结 |
| PART 04 | Logical/Physical Architecture、Module Ownership、数据流、状态/恢复 | 结构丰富；Module ID 和物理方案未闭合 |
| PART 05 | 开源复用审计方法、证据等级、Reuse Matrix、PoC/License/Security Gate | 方法有，实际审计产物没有 |
| PART 06 | Domain Model、Aggregate、Evidence/Memory/Radar/Discover 模型 | 明确列出多项未决模型决策 |
| PART 07–08 | SearchGateway、Runtime Contract、Adapter、SSE、恢复 | Contract 方向存在；API/错误/状态 ID 仍不稳定 |
| PART 09–11 | Discovery、Radar/Discover、Evidence/Memory/Ranking | 差异化逻辑覆盖较多；跨模块 ownership 尚未完全落表 |
| PART 12 | Public API、Internal Contract、Event、Error、State Machine、Job | 语义丰富，但缺稳定目录和统一状态映射 |
| PART 13–14 | UI、Benchmark、Testing、Observability、Security、Privacy、Backup | 目标完整；与 Task 的逐项闭环不完整 |
| PART 15 | Function-level Specification、Physical Layout、Acceptance Matrix | 314 个详细 Function 中大量没有同块 Test ID |
| PART 16 | Implementation Map 规则、ADR、M0/PoC/M1–M4 Tasks、Dependency Graph、Freeze Checklist | 任务树存在，但不是符合模板的可执行 Task 文件 |

## 3. 标识符审计

全文扫描结果：

- Requirement：96 个唯一字符串，其中 94 个是产品需求体系，另有 `REQ-SEARCH-022`、`REQ-RUNTIME-006` 只出现在标识符示例中，造成伪目录项。
- Use Case：19 个唯一 ID，多个索引/页面段重复引用；`UC-DS-001` 和 `UC-RADAR-001` 各出现 5 次。
- Domain Entity：31 个唯一实体名；`ENT-ResearchRun`、`ENT-SolutionFamily`、`ENT-Evidence` 在总目录和 Domain 细节中重复声明。
- API：只有 2 个 `API-*` ID，但 PART 12 定义了大量 Public API endpoint。
- Event：只有 3 个 `EVT-*` ID，但 PART 12 定义了大量 Domain/Public Event 名称。
- Error：只有 4 个 `ERR-*` ID，但 PART 12 主要使用未编号的 `errorCode` 字符串。
- Test：161 个唯一 Test ID；`UT-DISC-001`、`UT-SEARCH-001`、`E2E-RESEARCH-001`、`E2E-RADAR-003` 重复声明。
- Task：实际 M0/PoC/M1/M2/M3/M4 任务树约 180 个任务，另有 `TASK-001`、`TASK-002` 等模板残留；`TASK-M0-001`、`TASK-M0-002`、`TASK-POC-001` 等重复出现。
- ADR：31 个 ADR 名称；ADR-001–006 等在清单、任务/门禁引用中重复出现，状态只有 Proposal/文字描述，没有仓库内 ADR 文件。

重复引用本身可以是索引引用，但文档没有明确区分“声明处”和“引用处”，部分章节也重复写入标题与状态，导致无法仅凭 ID 判定唯一规范来源。

## 4. Requirement → Function/Interface → Test → Task 闭环

这是当前最严重的结构性缺口。

- PART 16.1 明确要求完整链：`Requirement → Use Case → Module → Component → Function → Test → Task → Milestone → Gate`，并要求 Requirement、Function、Task 三类反向可追溯。
- 但 PART 04–15 基本没有 Requirement ID 引用；PART 15 没有 Requirement/Use Case 引用；PART 16 只有一个 `REQ-DS-004 → ... → TASK-M1-014` 示例。
- PART 16.1.7 只提出 `docs/IMPLEMENTATION_MAP.md` 为建议路径，并标注 Repository final layout 尚未 Freeze；实际 Map 内容不存在。
- 以详细 PART 15 Function 区间扫描，约 314 个 Function 声明中约 257 个在自己的 Function Spec 块内没有 Test ID。代表性缺口包括 `FN-COMMON-005`、`FN-RESEARCH-003`、`FN-DISC-002`、`FN-SEARCH-002`、`FN-RUNTIME-001`、`FN-EVID-001`、`FN-RANK-001`、`FN-MEM-003`、`FN-RADAR-003`、`FN-DISCOVER-001`、`FN-API-003`、`FN-JOBS-001`、`FN-PERSIST-001`、`FN-WEB-001`。
- M0 Task 文本没有 Requirement ID、Use Case ID、Interface ID、Test ID 或验收命令；因此即使任务目标清楚，也不能按文档自己的规则标成 READY。

结论：要求链条在“概念层”存在，在“可施工 Map”层没有闭合。

## 5. Task 与 Milestone 审计

### 已有内容

M0 → PoC → M1 → M2 → M3 → M4 的主顺序明确；M0-013 依赖 M0-002..012，PoC-003 依赖 PoC-002，PoC-009 依赖 PoC-006/008，M1/M2/M3/M4 的粗粒度依赖也有描述。

### 不满足 READY 的地方

PART 16.2 要求每个 Task 必须包含：Task ID、Title、Milestone、Priority、Status、Depends On、Blocks、Objective、Scope、Out of Scope、Allowed Files、New Files Allowed、Forbidden Files、Required Interfaces、Required Functions、Given/When/Then、Required Errors、Required Events、Required Tests、Commands、Acceptance Criteria、Evidence Required、Architecture Constraints、Stop Conditions。

TASK-M0-001 至 TASK-M0-014 当前只有 Title/Objective/少量 Scope/输出或检查项，没有上述固定 Task Header，也没有 Allowed Files、Forbidden Files、Commands、Acceptance Criteria、Status。按 PART 16.1.18–20 的规则，它们必须是 `NOT_READY`，不能由 Agent 猜测补齐。

## 6. Architecture / Ownership / Dependency 审计

### 6.1 已确认的稳定原则

- UI → Application/Intelligence → Domain → Capability Interfaces → Adapters → External Systems。
- Runtime 是可替换执行引擎，不能成为 Product Core。
- Search Gateway 归 Personal Intelligence，外部 Provider 只能通过 Adapter。
- Evidence、Memory、Radar State、Discovery State、Coverage、Candidate Evaluation 等属于核心产品资产。
- Domain Event 与 Public Event/SSE 应分离。

### 6.2 已确认的 ownership 缺口或冲突

1. PART 04.2 明确列出 Candidate Module，并称其拥有 Candidate identity/normalization；PART 15 的模块列表和 `MOD-*` 清单没有 Candidate Module，只有 Entity、Discovery、Evidence、Ranking 等模块，Candidate 创建/身份/Variant 又分散在 Discovery 与 M2 Ranking/Evidence 链上。`MOD-CANDIDATE-001`、Candidate owner 和跨模块 Contract 缺失。
2. Search 负责 provider health、基础 dedup/canonicalization；Source Intelligence 负责 source health/reliability；Radar 又负责 exact/near dedup 与 event resolution；Evidence 负责 Source/Observation identity。文档没有冻结四种 dedup/health 的边界、canonical key 和唯一写入者。
3. Radar “调用” Personal Novelty/Personal Relevance，但 PART 15 没有对应稳定 Module ID；M3 Task 又把两者作为 Radar 内部实现，编译/依赖边界未定义。
4. Source、SourceObservation、Entity、ProviderProfile、SourceProfile 的边界在多处被引用，但 `SourceProfile vs ProviderProfile`、`CandidateVariant`、`Knowledge/Usage/Interest`、`ClaimAssessment` 均仍为 TBD/Proposal。

这些问题不是实现细节；它们会影响 Domain ownership、Repository ownership、Event publisher、数据库写入边界和依赖方向，Coding Agent 无权自行解决。

## 7. API / Event / Error / State Machine 审计

- PART 12.3 的 API 使用 `/api/v1/research` 等 endpoint，但没有 `API-*` 稳定 ID、版本化 DTO 清单、字段级 schema 文件或 Error/Test 映射。
- Research API ReadModel 写出 `status: RUNNING / COMPLETED / PARTIAL...`；PART 12.13 又定义 `ResearchStatus = ACTIVE / COMPLETED / PARTIAL / CANCELLED / FAILED / ARCHIVED`，产品级章节还把 `CREATED/PLANNING/...` 作为状态。文档说要区分 status/stage，但 API 的 `RUNNING` 与 Domain `ACTIVE` 的映射未冻结。
- PART 12.13 的 ResearchStage 包含 `CREATED, PLANNING, RESEARCHING, CRITIQUING, VERIFYING, RANKING, COMPOSING, DONE`；PART 02 直接把同一组前半段称为产品状态。当前可表达，但不是一个明确的统一 State/Stage Contract。
- Domain Event 与 Public Event 分离规则清楚，但 Event Catalog 只有事件名称，没有 `EVT-*` ID、payload schema、publisher owner、version、replay policy 的统一注册表。
- Error Taxonomy 和 errorCode 字符串较完整，但没有 `ERR-*` 注册表，也没有把每个 Function/Task 的 Required Errors 绑定到稳定 ID。

结论：实现 API、SSE、错误映射和状态转换会遇到缺失/冲突契约，属于 SPEC CONFLICT，而不是 Agent 可以自行补齐的字段。

## 8. Data Model 与 Domain Model

PART 06 明确声明 Domain Model 尚未 Frozen，需要 Data Model、API、Search、Runtime、Evidence、Memory、Ranking 反向验证；PART 15.2 又把 Python/PostgreSQL/Repository/UoW/Outbox 作为 Proposed；PART 15.17 的 ORM/table/index 细节仍留待后续。

因此目前只有逻辑实体，没有冻结的：

- Aggregate/Repository ownership 表；
- 表/字段/约束/索引/migration contract；
- outbox、event replay、idempotency 的物理 schema；
- Domain DTO 与 persistence row 的一一映射；
- deletion/retention/backup 的最终数据边界。

这直接影响 PoC-002、PoC-004 和所有需要持久化的 M1/M2 Task。不能将“PostgreSQL proposed”当作已经接受的数据库决定。

## 9. Runtime-specific 类型泄漏审计

文本规则明确禁止 Runtime-specific fields 进入 Product DTO，且 Public API 不应暴露原始 Runtime messages；本轮未发现一个已实现代码仓库可供静态检查，因此不能证明实际不会泄漏。

文档自身已有风险点：API diagnostics 允许暴露 runtime executions，RuntimeExecution/RuntimeEvent 也在 Domain Model 中；这可以成立，但必须冻结为“诊断 DTO/内部 Contract”，不能复用 Product DTO。当前没有字段级 DTO 定义和测试，状态为 `UNVERIFIED / BLOCKING BEFORE API FREEZE`。

## 10. Reuse First 审计

PART 05 只定义了审计方法和目标，没有完成实际项目的 pinned version、commit、license、maintenance、extension surface、failure mode 和 reuse decision 记录。PART 16.5 才安排 M0-002..012 执行这些工作，因此当前不能确认是否存在重复自研。

已发现可作为后续 M0 输入、但尚未形成正式结论的本地候选：

- `C:\Users\peng\Desktop\pi分析\pi-source`：Pi mono source，HEAD `2e4d239`，remote 为 `badlogic/pi-mono.git`。其 README 明确写出默认没有内建 permission system，需要 containerize/sandbox；这提示 M0-004/M0-012 必须把安全 Contract 作为硬验证项。
- `C:\Users\peng\Desktop\课讯CampusCue-交付\CampusCue`：存在 DeerFlow adapter/client 与测试，可作为本地适配经验参考，但未按 PART 05 的证据等级审计，不能直接当作 DeerFlow Contract 结论。

因此本轮仅完成 Reuse Audit 准备，不把上述候选标为 REUSE/ADAPT/REFERENCE/REJECT。

## 11. Milestone 边界判断

- M0：Reuse feasibility 和审计框架，边界合理；不应写 Product Core。
- PoC：Physical Architecture proof，边界合理；但 PoC-002 当前直接写 PostgreSQL，需要标明为 candidate experiment，不能预先冻结 ADR-005。
- M1：Discovery Proof，目标与 M2/M3 分界基本合理；Benchmark foundation 应先于复杂 Discovery Engine。
- M2：Deep Search Alpha，Evidence/Ranking/API/SSE/UI 组合较大但逻辑完整；应继续受 M1 Gate 限制。
- M3：Radar Alpha，依赖 M1 PASS 和 M2 基础能力，边界基本合理；Event Aggregate、Feed persistence、Attention Budget 仍应保留为实验项。
- M4：Product V1，包含 Discover/Library/Settings/恢复/安全/隐私，范围大但符合产品集成阶段；不能提前挪到 M1/M2。

主顺序合理；问题在于 Task 级 Depends On 不完整、Gate evidence 未绑定、以及状态/契约未闭合。

## 12. Architecture Freeze Gate 可执行性

当前不可执行为实际 Freeze Gate：

- PART 16.12 的 checklist 仍大量使用“待 PoC”“需 ACCEPT”“必须”，没有每项的 Evidence ID、Owner、验收命令和 Pass/Fail 记录。
- PART 16.13 只给出 Gate 问题和文字条件，没有 Gate 输入 artifact 的固定路径和版本。
- PART 16.15 自己声明：Blueprint = COMPLETE DESIGN DRAFT、Architecture = NOT FROZEN、Next Gate = M0 REUSE AUDIT，并列出 Physical architecture、Runtime、Queue、PostgreSQL/UoW、REST/SSE 等 Blocking Decisions。
- PART 05.8 要求的产物名与 PART 16.5 不一致：`OPEN-SOURCE-AUDIT.md / REUSE-MATRIX.md / STRATEGY-REGISTRY.md` 对比 `REUSE_AUDIT.md / RUNTIME_AUDIT.md / ... / REUSE_DECISION_MATRIX.md`。

结论：Blueprint Gate 只能判为 `PASS AS DESIGN DRAFT`，不能判为 Architecture Freeze。仓库身份和 canonical 文档路径已解决，但不改变 Blueprint 的冻结结论。

## 13. 最小结论

本轮不批准任何 Product Core、PoC、M1、M2、M3、M4 实施。

最小解阻集合见：

- `SPEC_CONFLICTS.md`
- `OPEN_TBDS.md`
- `M0_READINESS.md`
