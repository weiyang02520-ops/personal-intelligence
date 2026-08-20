# TASK-POC-006 — SearchGateway spike

Task ID: TASK-POC-006  
Title: SearchGateway spike  
Milestone: PoC  
Priority: P0  
Status: PARTIAL
Depends On: TASK-POC-001  
Blocks: TASK-POC-009, TASK-POC-012

## Objective

实现 `IF-SEARCH-001`、FakeSearchProvider 和一个真实 provider adapter，优先 GitHub REST Search。

## Scope

Request/response normalization, pagination, provenance, timeout, 429/auth/no-result/cancel contract behavior.

## Out of Scope

不宣称 GitHub 是最终 general-web provider，不削弱 `IF-SEARCH-001`，不泄露 credentials。

## Allowed Files

`apps/core/`, `tests/`, PoC config/docs.

## New Files Allowed

Search interface, fake provider, GitHub adapter, transport abstraction and tests.

## Forbidden Files

Final provider selection, Search Product feature, provider secret in source/tests.

## Required Interfaces

`IF-SEARCH-001`, FakeSearchProvider, GitHub adapter boundary.

## Required Functions

Search, normalize result, paginate, map timeout/429/auth/no-result/cancel.

## Required Behavior

At least one successful real GitHub path when network permits; deterministic fake transport for error cases.

## Required Errors

Timeout, rate limited, authentication failure, no result, cancellation, provider unavailable.

## Required Events

No public event expansion; optional internal search observation only.

## Required Tests

Normal, timeout, 429, auth failure, no result, cancel, provenance and real-provider path.

## Commands To Run

`python -m pytest -q tests/poc/test_search.py`; optional `POC_GITHUB_TOKEN` through environment only; `git diff --check`.

## Acceptance Criteria

Provider boundary is normalized without selecting final M1 provider; credential/network blocking is accurately labeled.

## Evidence Required

Contract output, real path result metadata, error mappings, rate-limit observation, secret handling and limitations.

## Architecture Constraints

Search provider key stays outside Runtime; Search ownership remains within PI SearchGateway.

## Stop Conditions

Need a new secret, provider choice, API contract change or dependency expansion.

## Execution Result

Status: COMPLETE
Evidence: `apps/core/search.py`, `tests/poc/test_search.py`, `docs/audit/poc/SEARCH_CANCELLATION_CONFLICT.md`
Artifacts Changed: SearchGateway, fake provider, GitHub REST adapter
Acceptance Result: PARTIAL — cancellation requirement conflicts with canonical Blueprint; no unsupported API was invented
Verification: `python -m pytest -q tests/poc/test_search.py`; normal/timeout/429/auth/no-result/provenance pass
Known Limitations: Search cancellation semantics require Spec-owner decision; GitHub is not the final general-web provider; no live token was committed.
Discovered Delta: Provider credentials are owned by the PI-side adapter, not runtime; Search cancel remains an open contract conflict.
