# TASK-POC-010 — Frontend PI API spike

Task ID: TASK-POC-010  
Title: Frontend PI API spike  
Milestone: PoC  
Priority: P0  
Status: READY  
Depends On: TASK-POC-002, TASK-POC-003  
Blocks: TASK-POC-012

## Objective

实现最小 Next.js interface：Create Research、Research ID、status、SSE updates、reconnect demonstration。

## Scope

One page, PI API client, SSE client, minimal reconnect state and static boundary check.

## Out of Scope

不做 production visual design、design system、large component library、auth 或 full UI。

## Allowed Files

`apps/web/`, frontend tests/config and PoC docs.

## New Files Allowed

Minimal Next.js app, API client, page and static boundary test.

## Forbidden Files

DeerFlow/LangGraph endpoints, runtime credentials, provider credentials, production UI.

## Required Interfaces

PI API `/research`, `/research/{id}`, PI SSE endpoint only.

## Required Functions

Create research, show status, subscribe/reconnect SSE.

## Required Behavior

Frontend knows PI API and no Runtime endpoint or secret.

## Required Errors

API failure, SSE disconnect/reconnect, invalid response.

## Required Events

Consume PI-owned public events only.

## Required Tests

Static endpoint/secret scan; component/API client test where toolchain permits; POC-003 reconnect evidence.

## Commands To Run

`npm test` or configured frontend check; static `rg`; `git diff --check`.

## Acceptance Criteria

Minimal page works against PoC API and stays runtime-agnostic.

## Evidence Required

Screenshot or test output, static boundary scan, reconnect result and limitations.

## Architecture Constraints

UI → PI API only.

## Stop Conditions

Need to expose runtime endpoint, add production UI system or add credentials.

## Execution Result

Status: PENDING  
Evidence: —  
Artifacts Changed: —  
Acceptance Result: —  
Verification: —  
Known Limitations: —  
Discovered Delta: —
