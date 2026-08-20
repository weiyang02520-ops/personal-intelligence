# M0 Runtime Audit — DeerFlow / Pi

Source tasks: TASK-M0-002, TASK-M0-003, TASK-M0-004, TASK-M0-012  
Status: PARTIAL — evidence-backed candidates; no Runtime decision accepted

## Candidate record: Pi

- Repository: https://github.com/badlogic/pi-mono
- Reviewed source: local snapshot `C:\Users\peng\Desktop\pi分析\pi-source`
- Exact reviewed commit: `2e4d23959485279aa2da1a45103de2ea22d46395` (2026-08-12)
- License / maintenance: MIT from local `LICENSE`; package snapshot reports `@earendil-works/pi-agent-core` version `0.84.1`.
- Relevant source anchors: local `README.md`, `AGENTS.md`, `packages/agent/package.json`, `packages/agent/docs/containerization.md`; exact PI-boundary interface mapping remains a PoC input.
- Claim: agent runtime with sessions, tools, model providers and headless/RPC-oriented packages.
- Code/interface evidence: `L1 SOURCE` from local snapshot; `L2 INTERFACE` PARTIAL pending exact contract extraction.
- Behavior/integration/security evidence: `L3 UNKNOWN`, `L4 UNKNOWN`, `L5 PARTIAL`.
- Confirmed limitation: README states there is no built-in permission system; sandbox/containerization is required for stronger isolation.
- Hard dependencies: model/provider credentials and host/runtime environment; permission enforcement is external.
- Failure modes: permission gap, cancellation/resume semantics not yet mapped to `IF-RUNTIME-001`, upgrade/API drift.
- Fit: possible alternate runtime through an adapter; not a direct dependency candidate yet.
- Decision candidate: `ADAPT` / `UNKNOWN` pending contract and isolated PoC.
- Plan reuse mode: `ADAPTER`.

## Candidate record: DeerFlow

- Repository: https://github.com/bytedance/deer-flow
- Exact reviewed commit: `a5acc25de6742b2166b3f41c97bd895822277b94` on `main` (2026-08-20 remote inspection)
- License / maintenance: MIT from upstream repository metadata and `LICENSE`; repository active at review time.
- Relevant source anchors: `backend/`, `contracts/`, `frontend/`, `skills/`, `tests/`, `README.md`, `extensions_config.example.json`.
- Claimed capability: runtime/agent execution, skills, MCP, files, sandbox, memory, subagents and streaming surfaces are named by upstream project materials.
- Code/interface evidence: `L1 SOURCE` from repository tree and `L2 INTERFACE` from `backend/docs/API.md` (`/api/langgraph/*` SSE, thread/run/file/skill/MCP routes); `L3 BEHAVIOR`, `L4 INTEGRATION`, `L5 SECURITY` remain UNKNOWN because the source was not cloned/executed in this batch.
- Hard dependencies/failure modes: `UNKNOWN`; likely runtime, model, storage and sandbox coupling must be inspected before any adapter claim.
- Fit: target audit candidate only.
- Decision candidate: `ADAPT` / `UNKNOWN`; API and extension surfaces are visible, but fit and security are not proven.
- Plan reuse mode: `ADAPTER` candidate, not accepted.

## TASK-M0-002 contract matrix

| Capability | DeerFlow | Pi | Evidence note |
|---|---|---|---|
| Start execution | PARTIAL | PARTIAL | DeerFlow documents `POST /api/langgraph/runs/stream`; no PI-boundary contract test |
| Status | PARTIAL | UNKNOWN | DeerFlow documents run history/status; PI mapping not frozen |
| Cancel | UNKNOWN | UNKNOWN | Cancellation semantics not verified |
| Stream events | PARTIAL | PARTIAL | DeerFlow documents SSE and bounded replay; event mapping not verified |
| Model/agent selection | PARTIAL | PARTIAL | DeerFlow documents configurable model/assistant; provider coupling remains |
| Skills / tools / MCP | PARTIAL | PARTIAL | DeerFlow source tree/API docs expose skills and MCP; extension behavior untested |
| Files / sandbox | PARTIAL | PARTIAL | DeerFlow exposes thread files/artifacts and sandbox concept; security enforcement unverified |
| Memory / resume | PARTIAL | UNKNOWN | DeerFlow documents memory/context, but PI recovery contract is not verified |
| Error isolation | UNKNOWN | UNKNOWN | No integration evidence |

## TASK-M0-003 extension hierarchy candidate

1. External API / documented extension surface — preferred if verified.
2. Skills / MCP / custom tools — candidate bounded extension.
3. Thin gateway adapter — candidate when contract translation is required.
4. Local patch — only if an exact missing contract is evidenced and upgrade impact is recorded.
5. Deep fork — reject as default due to upgrade and ownership risk.

This is a recommendation, not an accepted architecture.

## TASK-M0-012 security notes

Pi's permission gap means it cannot be treated as satisfying the PI Security Contract by itself. DeerFlow sandbox boundary is `UNKNOWN` until code-level and isolated security evidence exists. Any future candidate must prove tool permission enforcement, filesystem/network isolation, secret redaction and external-content untrusted handling.

## External source references inspected

- https://github.com/bytedance/deer-flow/blob/main/AGENTS.md
- https://github.com/bytedance/deer-flow/blob/main/backend/docs/API.md
- https://github.com/bytedance/deer-flow/blob/main/frontend/src/content/en/introduction/core-concepts.mdx
- https://github.com/bytedance/deer-flow/blob/main/docs/plans/2026-07-10-pluggable-authorization-rfc.md

These sources support interface/extension claims only. DeerFlow's own docs state that live tests require credentials and are opt-in; this audit did not run them. The authorization RFC also records that RBAC is not implemented, so the security contract remains open.

## Open gaps / PoC questions

- Pin DeerFlow commit and inspect actual gateway/API/event surfaces.
- Map Pi session/event/tool APIs to `IF-RUNTIME-001` without changing the contract.
- Prove cancel/resume/error isolation and permission enforcement in a sandboxed PoC.
- Record license and maintenance evidence at the exact selected version.
