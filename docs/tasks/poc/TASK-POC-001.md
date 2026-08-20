# TASK-POC-001 — Initialize architecture skeleton

Task ID: TASK-POC-001  
Title: Initialize architecture skeleton  
Milestone: PoC  
Priority: P0  
Status: READY  
Depends On: M0-GATE-001 PASS_WITH_NOTES  
Blocks: TASK-POC-002..012

## Objective

建立最小 `apps/web`, `apps/core`, `tests`, `benchmarks` skeleton，并验证 Web → PI API/Core → Capability Interfaces → Adapters → External Systems 的依赖方向。

## Scope

Identifiers、Clock、Error Envelope、Python package boundary、最小 Next.js package boundary、architecture import rules 和对应静态测试。

## Out of Scope

不创建数百个空文件，不实现业务 Domain、Discovery、Radar、Ranking、Memory、生产 UI、生产认证或 Architecture Freeze。

## Allowed Files

`apps/`, `tests/`, `benchmarks/`, `pyproject.toml`, `package.json`/workspace manifests、PoC docs/task packet。

## New Files Allowed

仅允许最小 skeleton、测试、PoC 配置和必要 README。

## Forbidden Files

`docs/plan(4).md`、M1/M2/M3/M4 feature code、ADR accepted、production migrations、real secrets。

## Required Interfaces

Capability interface placeholders only; no unapproved Public API expansion.

## Required Functions

Identifier creation, Clock now, error envelope serialization.

## Required Behavior

Runtime-specific imports cannot enter Product Core/domain modules.

## Required Errors

Base PoC error envelope with stable `code`, `message`, `request_id`.

## Required Events

No runtime event implementation; event types are introduced by POC-003.

## Required Tests

Architecture import/static checks and unit tests for identifiers/clock/error envelope.

## Commands To Run

`python -m pytest -q`; `npm test` or equivalent static check; `git diff --check`.

## Acceptance Criteria

Minimum directories exist; imports follow the direction; shared concepts are usable; no empty-code explosion or M1 feature appears.

## Evidence Required

Changed files, tests, import-rule output, known limitations, checkpoint reference and discovered delta.

## Architecture Constraints

Do not freeze physical layout beyond proven PoC boundaries. Runtime-specific types remain behind adapters.

## Stop Conditions

Architecture contradiction, required large dependency, need to change module boundaries/Public API, secret exposure or destructive action.

## Execution Result

Status: PENDING  
Evidence: —  
Artifacts Changed: —  
Acceptance Result: —  
Verification: —  
Known Limitations: —  
Discovered Delta: —
