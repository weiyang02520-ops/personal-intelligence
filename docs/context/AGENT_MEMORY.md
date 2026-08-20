# AGENT_MEMORY

Memory Schema Version: 1
Memory Revision: 1
Last Updated: 2026-08-20
Current Milestone: PRE-M0

## EXECUTION BOOTSTRAP

- Repository: `weiyang02520-ops/personal-intelligence`
- Visibility: PUBLIC
- Branch: `main`
- Starting HEAD: `690367c4be5b`
- Canonical Blueprint: `docs/plan(4).md`
- Canonical Workflow: `AI_LONG_TERM_WORKFLOW.md`

## CURRENT PROJECT TRUTH

- Current Phase: `PROJECT_BOOTSTRAP / BLUEPRINT_AUDIT`
- Current Gate: `PRE-M0 / EXTERNAL REVIEW REQUIRED`
- Implementation: `NOT STARTED`
- M0 Readiness: `NOT_READY_FOR_M0`
- No Product Core, PoC, M1, M2, M3 or M4 business implementation is authorized in this checkpoint.

## CURRENT NEXT TASK

No READY task. After External ChatGPT Review and closure of the minimum readiness set, the intended first task is `TASK-M0-001 — Create reuse audit framework`.

## ARCHITECTURE RULES

- Treat `docs/plan(4).md` as the highest project-specific design source.
- Treat `AI_LONG_TERM_WORKFLOW.md` as the collaboration/execution protocol.
- Do not change database, Runtime, module boundaries, Public API, Domain states, Search ownership or Dependency Direction without an explicit architecture decision task.
- On contradiction, stop the affected work and write a SPEC CONFLICT REPORT.

## DEPENDENCY DIRECTION

UI → Application/Intelligence → Domain → Capability Interfaces → Adapters → External Systems.

## GIT / CHECKPOINT RULES

- Keep PI changes isolated from the workspace super-repository.
- Never commit secrets or unrelated files.
- Run status, diff, secret checks and relevant documentation checks before commit.
- Push only the scoped checkpoint and verify local HEAD equals the expected remote branch HEAD.
- Stop after External Review handoff.

## STOP RULES

Stop when repository identity is uncertain, a required credential is missing, an irreversible decision is required, a serious security issue appears, remote verification fails, or the current Gate is reached.

## AGENT_DISCOVERED_DELTA

- The current workspace root is a multi-project Git repository with unrelated modifications and is not the PI repository.
- The correct Public repository already existed; no repository creation was necessary.
- The local Pi source candidate was found separately at `C:\Users\peng\Desktop\pi分析\pi-source`, but it is only a future M0 audit input, not a PI dependency decision.
