# TASK-M0-009 — Audit community-source connectors

Task ID: TASK-M0-009  
Title: Audit community-source connectors  
Milestone: M0  
Priority: P0  
Status: PARTIAL  
Owner Agent: Workspace Coding Agent  
Depends On: TASK-M0-001  
Blocks: TASK-M0-013

## Objective

审计 SurfSense capabilities 以及稳定 REST/MCP connector patterns，寻找无需自写 scraper 的 community-source adapter candidates。

## Scope

记录 sources、授权、接口、metadata、pagination、错误、维护、集成与安全证据。

## Out of Scope

不接入社区源，不写 scraper，不改变 Source/Evidence ownership。

## Allowed Files

- `docs/tasks/m0/TASK-M0-009.md`
- `docs/audit/m0/SEARCH_PROVIDER_AUDIT.md`

## New Files Allowed

仅允许更新 `docs/audit/m0/SEARCH_PROVIDER_AUDIT.md`。

## Forbidden Files

Connector implementation、credential/config、database、Public API、ADR acceptance。

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

Official source inspection、adapter evidence validation、`git diff --check`。

## Commands To Run

`rg -n "SurfSense|REST|MCP|community|adapter" docs/audit/m0/SEARCH_PROVIDER_AUDIT.md`; `git diff --check`。

## Acceptance Criteria

候选 connector 有稳定性、授权/条款、失败模式与 integration fit；不把“有 connector”误判为可直接复用。

## Evidence Required

Repository/version/license、relevant connector files/interfaces/functions、behavior/integration/security/maintenance evidence。

## Architecture Constraints

保持 SourceCollection、Evidence、Search 的边界未决但不被审计任务改写。

## Stop Conditions

需要自写 scraper、跨越 ownership 或新增大型 dependency。

## Execution Result

Status: PARTIAL  
Evidence: SurfSense is pinned to `2b50e7a4025582e0b6a3df097249f1e439362bce`; REST/MCP patterns are recorded as adapter candidates.  
Artifacts Changed: `SEARCH_PROVIDER_AUDIT.md`.  
Acceptance Result: PARTIAL — connector patterns identified; license metadata, auth and behavior remain open.  
Verification: GitHub metadata/tree inspection; no connector execution.  
Known Limitations: Community-source terms and schema stability require source-by-source review.  
Discovered Delta: Stable API/connector boundary is preferable to self-written scraper, but no connector is accepted.
