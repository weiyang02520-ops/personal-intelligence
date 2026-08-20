# TASK-POC-007 — FetchGateway security spike

Task ID: TASK-POC-007  
Title: FetchGateway security spike  
Milestone: PoC  
Priority: P0  
Status: COMPLETE
Depends On: TASK-POC-001  
Blocks: TASK-POC-012

## Objective

实现最小 HTTP/HTTPS FetchGateway、bounded timeout/size、redirect handling、provenance 和 SSRF protection。

## Scope

Block localhost, loopback, RFC1918, link-local, cloud metadata and public-to-private redirects; DNS validation must not rely only on original hostname.

## Out of Scope

不实现 browser automation 或 full crawler。

## Allowed Files

`apps/core/`, `tests/`, PoC docs.

## New Files Allowed

FetchGateway, resolver/policy helper, artifact/provenance model and security tests.

## Forbidden Files

Browser runtime, crawler product, unsafe bypass flags, real user data.

## Required Interfaces

Minimal FetchGateway capability interface.

## Required Functions

Fetch URL, validate target, validate redirects, enforce timeout/size, create provenance.

## Required Behavior

All required local/private/metadata/redirect cases are blocked.

## Required Errors

SSRF blocked, unsupported scheme, timeout, size exceeded, redirect blocked, fetch failure.

## Required Events

No public event expansion.

## Required Tests

localhost, 127/8, ::1, RFC1918, link-local, metadata IP, DNS rebinding-like resolution and public→private redirect.

## Commands To Run

`python -m pytest -q tests/poc/test_fetch_security.py`; `git diff --check`.

## Acceptance Criteria

Security tests prove required blocks; safe HTTP behavior is bounded and provenance is represented.

## Evidence Required

Test output, resolver decisions, blocked URLs/classes, safe-fetch result and limitations.

## Architecture Constraints

External content is untrusted; no network isolation decision is accepted by this task.

## Stop Conditions

Cannot establish safe resolver behavior, need unsafe network access or security incident.

## Execution Result

Status: COMPLETE
Evidence: `apps/core/fetch.py`, `tests/poc/test_fetch.py`, `docs/audit/poc/POC_SECURITY_MATRIX.md`
Artifacts Changed: bounded FetchGateway with URL/DNS/redirect validation
Acceptance Result: PASS
Verification: `python -m pytest -q tests/poc/test_fetch.py`
Known Limitations: Production egress isolation and DNS rebinding controls remain open.
Discovered Delta: SSRF protection is a gateway concern and does not belong in the runtime adapter.
