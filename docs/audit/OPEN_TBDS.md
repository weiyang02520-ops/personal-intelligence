# Personal Intelligence — Open TBDs

来源：`C:\Users\peng\Desktop\plan.md`

分类原则：按照 PART 16.12 的 `BLOCKING / NON_BLOCKING / DEFERRED`，并区分“阻塞正式 M0 Task 执行”和“阻塞后续 PoC/Architecture Freeze”。

## A. 已解决的 Bootstrap 项

### RESOLVED-A01 — PI 仓库与事实源路径

证据：PART 16.15.35–16.15.37 要求先把蓝图保存进 Personal Intelligence repository。已确认仓库为 `weiyang02520-ops/personal-intelligence`，并已将 plan.md 完整复制为 `docs/plan(4).md`。

状态：已关闭。源文件仍保留在 Desktop；仓库内副本作为本项目 canonical Blueprint，源路径和复制事实已记录在 Handoff。

## B. 已由 M0 准备关闭的最小项

### RESOLVED-M0-01 — M0 Task packet schema

`docs/tasks/m0/TASK-M0-001.md` through `TASK-M0-014.md` now carry the PART 16.2 fields, explicit dependencies, allowed/forbidden paths, evidence and execution result sections.

### RESOLVED-M0-02 — Reuse artifact canonical names

`docs/audit/m0/` is the canonical namespace. `OPEN_SOURCE_AUDIT.md` is the umbrella; the seven plan-specified detailed artifacts are canonical. PART 05.8 names are legacy aliases only.

### RESOLVED-M0-03 — M0 evidence / ADR authority boundary

M0 artifacts record evidence, candidate classifications, conflicts, PoC questions and ADR update proposals. They do not accept ADRs, freeze architecture or authorize PoC/M1.

### RESOLVED-M0-04 — M0 Gate evidence schema

`docs/gates/M0-GATE-001.md` fixes Evidence ID, Gate ID, Condition, Source Task, Input Artifact, Evidence Level, Verification Method, Pass Rule, Observed Result, Status, Owner, Reviewer, Commit/Reference, Date and Known Limitations. The Gate remains non-PASS.

## C. Remaining items that block PoC or Architecture Freeze

### TBD-A02 — M0 Task packet schema (closed for M0)

证据：PART 16.2 与 TASK-M0-001..014 不一致。

已关闭于本 M0 batch；后续 Milestone Task 仍需按同一模板生成。

### TBD-A03 — Reuse artifact canonical names (closed for M0)

证据：PART 05.8 与 PART 16.5 文件名不一致。

已关闭；canonical 关系见 `docs/audit/m0/OPEN_SOURCE_AUDIT.md`。

### TBD-A04 — M0 audit scope 的架构权限 (closed for M0)

证据：PART 01.15、PART 16.3.23、PART 16.5.19 要求遇到架构变化停止；但 M0-013/014 会产出 ADR updates 和 Gate decision，未定义谁批准、哪些是报告、哪些是架构任务。

已关闭；Gate 仍等待 External Review。

## C. 不阻塞“审计框架”本身，但阻塞 PoC/Architecture Freeze

### TBD-B01 — 最终 backend/physical architecture

来源：TBD-001；ADR-001 PROPOSED；PART 15.2 PROPOSED。

当前倾向：Next.js Web + Python PI Core modular monolith + external runtime。需要 M0 + PoC 验证。

### TBD-B02 — 主数据库、UoW、Outbox、Migration

来源：TBD-002；ADR-005/006 PROPOSED；PART 04.11 和 PART 15.2。

PostgreSQL 是候选，不是已接受决策；SQLite local mode、队列、ArtifactStore、migration policy 未完全冻结。

### TBD-B03 — DeerFlow contract 与默认 Runtime

来源：TBD-004/005、TBD-RUNTIME-001..007；ADR-002/003 PROPOSED。

必须完成代码级 Contract Audit、extension surface audit 和最小 PoC；不得因 Adapter 失败改动 Product Core。

### TBD-B04 — Search Provider / SourceCollection / Crawl 组合

来源：TBD-006/007/018、TBD-SEARCH-FEED-001、TBD-SEARCH-PROVIDER-001..003、TBD-SEARCH-CRAWL-001。

需要确定 M1 的最小 provider capability set、GitHub vertical、Fetch/Crawl/Browser escalation boundary；不能由 Task Agent 自行选 Provider 或增加大型依赖。

### TBD-B05 — Public API / Event / Error registry

来源：PART 01.3、PART 12、SC-004。

需要至少冻结 PoC 所需 Research create/get/cancel、SSE reconnect、Error Envelope、Public Event projection 的 ID、schema、version 和 replay semantics。

### TBD-B06 — Research status/stage/cancellation mapping

来源：PART 02.33、PART 04.10、PART 12.3、PART 12.13。

需要一张唯一状态表和非法 transition tests。

### TBD-B07 — Candidate / Variant / Entity ownership

来源：TBD-DOMAIN-CAND-002、TBD-CANDIDATE-VARIANT-001、SC-006。

M1 CandidateProposal 与 M2 CandidateVariant 之间必须明确 identity owner、merge/redirect、variant semantics。

### TBD-B08 — Evidence assessment / Memory relation split

来源：TBD-CLAIM-ASSESSMENT-001、TBD-KNOWLEDGE-001、PART 06.17、PART 11。

这两项可推迟到 M2/M3 的正式实现，但在相关 Domain/Repository/API Task READY 前必须接受 ADR。

## C. 明确可延后的实验项

- `TBD-DOMAIN-SEARCHGRAPH`：M1 先用显式关系，不前置 Graph DB。
- `TBD-DISC-ASSUMPTION-001`：是否建立 ResearchAssumption，交由 M1 Benchmark。
- `TBD-DISC-CAND-001`：是否需要 Shortlist，暂不增加。
- `TBD-DISCOVER-STATE-001`：Discover Completed 语义，M4 前决定。
- `TBD-CONNECTION-001`、`TBD-DISC-BRANCH-TYPE-001`：Discover 数据治理实验。
- `TBD-RADAR-EVENT-001`、`TBD-RADAR-FEED-001`、`TBD-RADAR-SIGNAL-001`：M3 PoC/Replay 决定。
- Radar adaptive scheduling、Weak Signal 默认开启、Attention Budget 具体值、Policy 自动学习：M3 Benchmark 决定。
- UI exact colors/widths/radius：M4 Design Freeze，按计划不阻塞 M1。

## D. 未决但当前不应被错误升级为实现任务

- Vector DB、Graph DB、Browser Automation、Native Mobile、Advanced Notification。
- Authentication V1 范围，除非进入明确的 API/Security Task。
- 是否采用某个具体 Queue 框架，直到 Job Contract 和 PoC evidence 完成。
