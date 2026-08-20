# Personal Intelligence — SPEC CONFLICT REPORT

输入：`C:\Users\peng\Desktop\plan.md`

状态：审计发现，未擅自裁决。

## SC-001 — Blueprint 已完整但尚未达到可施工冻结

- 冲突位置：PART 01.17、PART 05.8、PART 16.12–16.15；尤其 L107153–L107175。
- 受影响：全部 P0 Requirement；ADR-001..006；M0-GATE-001、POC-GATE-001；所有后续 Task。
- 实际问题：文档称第一轮 Blueprint 完整，但同时明确 `COMPLETE DESIGN DRAFT`、`Architecture NOT FROZEN`，并列出 backend、Runtime、Queue、DB、REST/SSE 为 Blocking Decisions。
- 阻塞原因：Agent 无法知道哪些“当前倾向”可以作为施工约束，哪些只能作为实验假设。
- 最小修改：增加一份版本化 `BLUEPRINT_STATUS.md` 或在仓库内固定状态页，明确 `DESIGN_DRAFT → M0_ACTIVE → POC_ACTIVE → FOUNDATION_FROZEN` 的状态转换和允许动作。
- 可选方案：A. 先冻结逻辑边界、保留物理方案为实验；B. 等 M0+PoC 完成后整体 Freeze。
- 推荐方案：A。允许 M0 审计开始，但禁止任何 Product Core 和物理架构实现被当作已冻结。
- 影响范围：文档状态、Task 状态、Gate 记录，不改变产品架构。

## SC-002 — Requirement Traceability Map 缺失

- 冲突位置：PART 16.1.2–16.1.16 对 Map 的强制要求，与实际 PART 04–15/16 内容。
- 受影响：全部 Requirement、Function、Test、Task；示例 `REQ-DS-004 → UC-DS-001 → ... → TASK-M1-014`。
- 实际问题：除示例外，PART 15 没有 Requirement/Use Case 引用，M0/M1/M2/M3/M4 Task 没有 Requirement 字段，`docs/IMPLEMENTATION_MAP.md` 只是建议路径，实际不存在。
- 阻塞原因：无法判断漏实现、Scope Creep、测试覆盖和 Gate 完成度。
- 最小修改：生成一个只含 ID 的 Traceability Map；先覆盖 M0/PoC，再逐阶段补齐 P0 Requirement。为每个 M0 Task 添加 Requirement 或 `ARCH/NFR` 绑定。
- 可选方案：A. 立即为全量 94 个产品需求建 Map；B. 先建 M0/PoC slice，标记未覆盖项。
- 推荐方案：B，避免本轮重写计划书。
- 影响范围：Implementation Map、Task 文件、Gate evidence。

## SC-003 — M0 Task 没有满足自身规定的 Task Template

- 冲突位置：PART 16.2.1–16.2.20 与 PART 16.5 TASK-M0-001..014。
- 受影响：TASK-M0-001..014、M0-GATE-001。
- 实际问题：M0 任务没有 Status、Priority、Depends On、Blocks、Allowed/Forbidden Files、Required Tests、Commands、Acceptance Criteria、Stop Conditions 等字段。
- 阻塞原因：`READY` 的定义是 Spec 已冻结且允许 Agent 开始；当前 Agent 必须自行猜测任务边界，违反 Coding Agent Rules。
- 最小修改：为 TASK-M0-001..014 建独立 Task 文件或统一表，每项至少填完 PART 16.2 的必填字段，并把 M0-001 的输出路径冻结。
- 可选方案：A. 先只补 M0-001；B. 补齐整个 M0 Task packet。
- 推荐方案：B。M0-001 的框架必须服务其余 M0 审计，单独补一个任务仍会在 M0-002 处再次停住。
- 影响范围：M0 执行资格，不涉及业务代码。

## SC-004 — API/Event/Error 稳定 ID 与实际目录不一致

- 冲突位置：PART 01.3 的 ID 规范；PART 12.3、12.4、12.10；PART 15 API/Event Function Specs。
- 受影响：API-RESEARCH-001、API-RADAR-003、IF-SEARCH-001、IF-RUNTIME-001；所有 Public Event、ErrorCode、API Task。
- 实际问题：全文只有 2 个 API ID、3 个 EVT ID、4 个 ERR ID，但 PART 12 已定义大量 endpoint、event type、errorCode；它们没有统一注册表、版本、owner、schema 和 Test ID。
- 阻塞原因：不能稳定生成 OpenAPI/SSE/Error contract，也无法判断 Public API 与 Internal API 边界。
- 最小修改：明确“声明 ID”与“名称引用”规则，补齐 M0/PoC 需要的 API/IF/Event/Error registry；全量目录可延后到对应 Milestone。
- 可选方案：A. 采用现有 `API-* / EVT-* / ERR-*` 体系；B. 改为 endpoint/event/errorCode 为唯一键。
- 推荐方案：A，符合 PART 01 已冻结的标识符方向；需要由架构任务确认编号分配方式。
- 影响范围：API Contract、SSE、Error mapping、Test Matrix。

## SC-005 — Research status/stage 语义未统一

- 冲突位置：PART 02.33、PART 04.10、PART 12.3.16、PART 12.13。
- 受影响：REQ-CORE-015、REQ-DS-020/021；ResearchReadModel；FN-RESEARCH-*；TASK-M2-001、TASK-POC-002。
- 实际问题：产品章节把 `CREATED/PLANNING/RESEARCHING/...` 列为状态；PART 12.13 定义 `ResearchStatus=ACTIVE/...`、`ResearchStage=CREATED/...`；API ReadModel 又写 `status=RUNNING/...`。三者的映射没有冻结。
- 阻塞原因：API、事件、非法状态转换和恢复逻辑会产生不同实现。
- 最小修改：建立一个 Research State/Stage 表，声明每个 Public status、Domain status、stage、cancellationState 的唯一映射和允许转换。
- 可选方案：A. Status/Stage 分离并保留 `ACTIVE`；B. 单一状态枚举。
- 推荐方案：A，符合 PART 12.13 的设计方向，但需在 ADR/Contract Task 中正式接受。
- 影响范围：Research Domain、Public API、Event、UI、Recovery。

## SC-006 — Candidate / Entity / Discovery ownership 不一致

- 冲突位置：PART 04.2.5、PART 06.2/06.7、PART 15 module list、PART 16.7/16.8。
- 受影响：Candidate、CandidateVariant、Entity；MOD-DISCOVERY-001、MOD-ENTITY-001；FN-DISC-015、FN-ENTITY-*；TASK-M1-011/012、TASK-M2-015。
- 实际问题：PART 04 声明 Candidate Module 拥有 identity/normalization；PART 15 没有 Candidate Module ID；M1 Discovery 负责 CandidateProposal/M1 family funnel；M2 又负责 Candidate identity + Variant。
- 阻塞原因：无法确定谁写 Candidate/Entity Repository、谁发布 CandidateCreated、谁负责 merge/redirect、谁依赖谁。
- 最小修改：新增/确认 Candidate ownership 表，明确 Proposal、Entity identity、Variant、Evidence-backed fact、Evaluation 的边界；为 owner 分配 stable Module/Contract ID。
- 可选方案：A. Candidate 作为 Entity 的产品投影；B. Candidate 作为独立 Domain Module。
- 推荐方案：先由架构任务选择并写 ADR，Coding Agent 不得猜。
- 影响范围：Domain、Persistence、Discovery、Evidence、Ranking、API。

## SC-007 — Search / Collection / Radar / Evidence 的 dedup 与 health ownership 重叠

- 冲突位置：PART 04.2.4/04.2.9/04.2.11、PART 07、PART 10、PART 11、PART 15.7/15.12/15.14。
- 受影响：IF-SEARCH-001、SourceCollectionGateway、RadarCandidate、SourceProfile、SourceObservation；TASK-M0-007/008/009、TASK-M1-005/006、TASK-M3-006/007/008。
- 实际问题：Search 做 request-level dedup/canonicalization 和 provider health；Radar 做 exact/near dedup、event resolution；Evidence 做 source identity；Source Intelligence 做 source health/reliability。canonical key、时空范围和唯一写入者未定义。
- 阻塞原因：同一 URL/Entity/Event 可能被重复建模，或模块互相覆盖 health/novelty。
- 最小修改：冻结四层语义：request result dedup、observation dedup、entity resolution、cross-source event resolution；为 health 拆分 provider/source/connector/runtime 四种 owner。
- 可选方案：A. 分层去重；B. 由 Entity/Source Intelligence 统一持有。
- 推荐方案：A，保留 Search 的局部优化并让 Evidence/Entity 持有长期 identity。
- 影响范围：Search、Evidence、Radar、Memory、Source Intelligence、数据模型。

## SC-008 — Data Model 未冻结但 PoC 任务预设 PostgreSQL/Outbox

- 冲突位置：PART 04.11、PART 15.2.32–15.2.60、ADR-005/006、TASK-POC-002/004。
- 受影响：ResearchRun、Outbox、Repository/UoW、POC-GATE-001、ADR-001/005/006。
- 实际问题：文档多处说明 DB/Queue/Outbox 仍需 PoC/ADR 接受，但 POC-002 直接规定 Persistence=PostgreSQL，POC-004 又以 PostgreSQL transaction + outbox 为验证对象。
- 阻塞原因：PoC 可能把候选方案误当成已冻结方案，失败时无法判断是架构失败还是候选技术失败。
- 最小修改：把 PostgreSQL 标为 Candidate A，并定义可替代 Candidate B 的最小比较标准；PoC-002/004 必须输出 evidence，不自动改 ADR。
- 可选方案：A. 只验证 PostgreSQL；B. 验证抽象 Contract 后用 PostgreSQL 做一个实现。
- 推荐方案：B，保持 Domain/Persistence Contract 与技术选择分离。
- 影响范围：Physical Architecture、Persistence、Migration、Outbox、PoC Gate。

## SC-009 — Reuse 产物文件名冲突

- 冲突位置：PART 05.8.2–05.8.4 与 PART 16.5.3。
- 受影响：TASK-M0-001、TASK-M0-013、M0-GATE-001、ADR updates。
- 实际问题：PART 05 要求 `OPEN-SOURCE-AUDIT.md`、`REUSE-MATRIX.md`、`STRATEGY-REGISTRY.md`；PART 16.5 要求 `REUSE_AUDIT.md`、`RUNTIME_AUDIT.md`、`SEARCH_PROVIDER_AUDIT.md`、`ALGORITHM_REUSE_AUDIT.md`、`UI_REFERENCE_AUDIT.md`、`REUSE_DECISION_MATRIX.md`。没有 source of truth 和兼容命名规则。
- 阻塞原因：M0-001 无法知道应创建哪些文件，M0-013 无法知道收敛输入。
- 最小修改：声明一套 canonical artifact names，另一套仅作 legacy alias 或移除。
- 可选方案：A. 以 PART 16.5 的分项审计为 canonical；B. 以 PART 05.8 的总目录为 canonical。
- 推荐方案：A 为执行文件，B 作为索引页。
- 影响范围：M0 文档产物和 Gate 输入。

## SC-010 — Architecture Freeze Gate 没有可执行 evidence contract

- 冲突位置：PART 01.17、PART 05.8、PART 16.12–16.13。
- 受影响：BLUEPRINT-GATE-001、M0-GATE-001、POC-GATE-001、ARCHITECTURE_FREEZE.md。
- 实际问题：Checklist 使用“待 PoC/需 ACCEPT/必须”，Gate 使用问题清单，但没有 evidence ID、artifact path、owner、command、threshold、reviewer、版本和复验规则。
- 阻塞原因：Gate 只能被口头宣布通过，无法审计或阻止错误进入下一阶段。
- 最小修改：为每个 Gate 条件增加 `Input Artifact / Test or Review / Pass Rule / Owner / Recorded Result / Date / Commit`。
- 可选方案：A. 先为 M0/PoC Gate 建轻量 schema；B. 立即把所有 Gate 完整化。
- 推荐方案：A，先支撑当前阶段，不扩大本轮范围。
- 影响范围：Gate governance、Milestone transition、审计可重复性。

## SC-011 — PART 15 Function → Test 闭合缺失

- 冲突位置：PART 15.1、15.20.19、15.20.27 与详细 Function specs。
- 受影响：约 314 个 Function 声明；约 257 个 Function block 未见 Test ID。
- 实际问题：文档规定任何 P0 Function 没有 Test ID 即 Spec 不完整，但大量 Function 只有输入/输出/依赖/错误说明，没有对应 Test。
- 阻塞原因：无法为 Task 生成 Required Tests，也无法验收“实现存在但未验证”的函数。
- 最小修改：先对 M0/PoC/M1 范围内 Function 补 Test ID；剩余模块在对应 Milestone 前补齐。
- 可选方案：A. 全量补齐；B. 按 Milestone 增量补齐。
- 推荐方案：B，符合 M0→PoC→M1 顺序。
- 影响范围：Function Specs、Test Matrix、Task readiness。

