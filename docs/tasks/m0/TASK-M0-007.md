# TASK-M0-007 — Audit Search providers

Task ID: TASK-M0-007  
Title: Audit Search providers  
Milestone: M0  
Priority: P0  
Status: PARTIAL  
Owner Agent: Workspace Coding Agent  
Depends On: TASK-M0-001  
Blocks: TASK-M0-013

## Objective

审计 SearXNG、Brave、Exa、Tavily、GitHub vertical，形成 Provider Capability Matrix。

## Scope

检查 API stability、query operators、pagination、metadata、freshness、cost、rate limits、regional availability、legal/terms、structured output；只提出 M1 最小 provider 组合候选。

## Out of Scope

不选择 provider，不申请凭证，不引入 SDK，不实现 Search Gateway。

## Allowed Files

- `docs/tasks/m0/TASK-M0-007.md`
- `docs/audit/m0/SEARCH_PROVIDER_AUDIT.md`

## New Files Allowed

仅允许更新 `docs/audit/m0/SEARCH_PROVIDER_AUDIT.md`。

## Forbidden Files

Search implementation、provider SDK manifests、secret/config、Public API、ADR acceptance。

## Required Interfaces
N/A — Audit Task；不得新增 `IF-SEARCH-*` contract。
## Required Functions
N/A — Audit Task。
## Required Behavior
N/A — Audit Task。
## Required Errors
N/A — Audit Task。
## Required Events
N/A — Audit Task。

## Required Tests

Official documentation/source inspection、terms/maintenance evidence check、`git diff --check`；无凭证时不做 live API call。

## Commands To Run

`rg -n "API stability|pagination|freshness|rate limits|structured output" docs/audit/m0/SEARCH_PROVIDER_AUDIT.md`; `git diff --check`。

## Acceptance Criteria

每个 provider 有精确版本/文档来源、接口能力、成本/限制、合规未知项、decision candidate；不将供应商 API 说成开源依赖。

## Evidence Required

Official URL/version/date、interface and response shape evidence、maintenance/terms/security notes、fit and failure modes。

## Architecture Constraints

Search planning/execution boundary和 provider health ownership 不得被改变。

## Stop Conditions

需要选择 provider、改变 Search ownership、引入大型 dependency 或使用未提供的 credential。

## Execution Result

Status: PARTIAL  
Evidence: SearXNG commit/license and official API candidates for Brave, Exa, Tavily and GitHub are recorded with required provider dimensions.  
Artifacts Changed: `SEARCH_PROVIDER_AUDIT.md`.  
Acceptance Result: PARTIAL — matrix is complete; live cost/rate/terms/response behavior is not verified.  
Verification: GitHub metadata and official provider documentation inspection; no credentials used.  
Known Limitations: M1 provider combination remains undecided.  
Discovered Delta: Hosted APIs are explicitly separated from open-source reuse; GitHub vertical is an adapter candidate.
