# TASK-M0-008 — Audit crawler/fetch/browser options

Task ID: TASK-M0-008  
Title: Audit crawler/fetch/browser options  
Milestone: M0  
Priority: P0  
Status: PARTIAL  
Owner Agent: Workspace Coding Agent  
Depends On: TASK-M0-001  
Blocks: TASK-M0-013

## Objective

审计 Crawl4AI、Firecrawl、Browser Use、direct HTTP fetch tools，明确普通 Fetch、site Crawl、adaptive Crawl、Browser fallback 边界。

## Scope

输出 Escalation Ladder，记录各候选的 repository/version/license、接口、行为、集成、安全与失败模式证据。

## Out of Scope

不实现 crawler/fetch/browser，不引入 browser automation，不改变 external content trust rule。

## Allowed Files

- `docs/tasks/m0/TASK-M0-008.md`
- `docs/audit/m0/SEARCH_PROVIDER_AUDIT.md`

## New Files Allowed

仅允许更新 `docs/audit/m0/SEARCH_PROVIDER_AUDIT.md`。

## Forbidden Files

Fetcher/Crawler code、browser dependency、secrets、API/Public contract、ADR acceptance。

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

Source/API inspection、trust-boundary evidence check、`git diff --check`；无 live credential/browser run。

## Commands To Run

`rg -n "Fetch|Crawl|Browser fallback|Escalation" docs/audit/m0/SEARCH_PROVIDER_AUDIT.md`; `git diff --check`。

## Acceptance Criteria

升级阶梯有触发条件、退出条件、成本/安全风险和 ownership note；未知项不被填成 PASS。

## Evidence Required

Exact repository/commit/version, relevant interfaces/functions, behavior/integration/security evidence, maintenance and failure modes。

## Architecture Constraints

Fetch/Crawl/Browser remains capability boundary; all external content is untrusted.

## Stop Conditions

需要决定 browser runtime、网络隔离、Crawler ownership 或引入大型依赖。

## Execution Result

Status: PARTIAL  
Evidence: Crawl4AI, Firecrawl and Browser Use commits/licenses plus five-level fetch/crawl/browser escalation ladder are recorded.  
Artifacts Changed: `SEARCH_PROVIDER_AUDIT.md`.  
Acceptance Result: PARTIAL — boundaries and candidates are explicit; no crawler/browser behavior or security test.  
Verification: GitHub metadata/tree inspection and document review.  
Known Limitations: SSRF, robots/terms, isolation, cost and nondeterminism require PoC evidence.  
Discovered Delta: Direct HTTP remains the common-case PI boundary candidate; browser is an isolated fallback.
