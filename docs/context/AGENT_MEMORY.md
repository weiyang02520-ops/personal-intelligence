# AGENT_MEMORY

Memory Schema Version: 1
Memory Revision: 3
Last Updated: 2026-08-20
Current Milestone: Physical Architecture PoC

## EXECUTION BOOTSTRAP

- Repository: `weiyang02520-ops/personal-intelligence`
- Visibility: PUBLIC
- Branch: `main`
- External Review Baseline: `bd12271c6e2cdc3a2e3e8fef440c47aaf86cfe82`
- Canonical Blueprint: `docs/plan(4).md`
- Canonical Workflow: `AI_LONG_TERM_WORKFLOW.md`

## CURRENT PROJECT TRUTH

- Current Phase: `PHYSICAL_ARCHITECTURE_POC`
- Current Gate: `POC-GATE-001 / CORRECTED EVIDENCE — EXTERNAL REVIEW REQUIRED`
- Implementation: `POC COMPLETE FOR REVIEW — no production implementation`
- M0 Readiness: `COMPLETE_WITH_NOTES`
- M0 External Review: `PASS_WITH_NOTES`
- M1, M2, M3 and M4 business implementation remains unauthorized.

## CURRENT NEXT TASK

The approved batch boundary is `TASK-POC-001..012`, limited to Physical Architecture PoC. Stop at `POC-GATE-001` External Review; no M1 task is authorized.

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
- Do not write a self-referential `Final HEAD` into tracked state. Record the review baseline and checkpoint content; report the final remote HEAD externally after push.
- Stop after `POC-GATE-001` External Review handoff.

## STOP RULES

Stop when repository identity is uncertain, a required credential is missing, an irreversible decision is required, a serious security issue appears, remote verification fails, or the current Gate is reached.

## AGENT_DISCOVERED_DELTA

- The current workspace root is a multi-project Git repository with unrelated modifications and is not the PI repository.
- The correct Public repository already existed; no repository creation was necessary.
- The local Pi source candidate was found separately at `C:\Users\peng\Desktop\pi分析\pi-source`, but it is only a future M0 audit input, not a PI dependency decision.

- External Review verdict: `M0-GATE-001 PASS_WITH_NOTES`; Physical Architecture PoC authorized, Architecture Freeze and M1 not authorized.
- Reviewed DeerFlow commit is pinned for audit; adopted runtime version remains NOT FROZEN.
- External Review returned `POC-GATE-001 CHANGES_REQUESTED` at `e7f6d5c97a62b35cacfbabf713daa81f55aea001`; only focused evidence closure is authorized.
- Focused closure is complete; corrected packet is ready for External Review. `TASK-POC-006` remains an explicit spec conflict, not an invented implementation.
