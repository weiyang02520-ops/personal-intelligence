# DeerFlow Source Contract Note — PoC

Status: REVIEWED FOR PHYSICAL ARCHITECTURE POC; adopted runtime version NOT FROZEN

## Reviewed source

- Upstream repository: `bytedance/deer-flow`
- Reviewed commit: `a5acc25de6742b2166b3f41c97bd895822277b94`
- Local audit checkout: `C:\Users\peng\Desktop\deer-flow-audit`
- Source was inspected from code at the pinned commit, not from README claims or a mock-only interface.

## Extracted contract anchors

| Concern | Source anchor | Observed semantics | PI PoC treatment |
|---|---|---|---|
| Client surface | `backend/packages/harness/deerflow/client.py`, `DeerFlowClient` near line 126 | In-process client exposes runtime-facing helper methods | Thin adapter only; no upstream types in PI public API |
| Stream events | `client.py`, `StreamEvent` near line 109 and `stream` near line 681 | Runtime interaction is represented as an iterable stream of typed events | Map event type/data into `RuntimeEvent` |
| Models | `client.py`, `list_models` near line 1103 | Capability/configuration inspection is available | Exposed only through adapter capability evidence |
| Skills | `client.py`, `list_skills` near line 1129 | Skill inspection is available | Recorded as optional capability, not Product Core state |
| Gateway lifecycle | `backend/app/gateway/app.py` lines 753–754; `backend/app/gateway/routers/thread_runs.py` lines 836, 846, 923, 983, 1406 | HTTP API creates a run, joins/streams it, returns status/messages/events, and cancels with `interrupt`/`rollback` | `DeerFlowRuntimeAdapter` now models this external boundary; controlled transport only |
| Gateway capabilities | `backend/app/gateway/app.py` line 777; gateway model/skills routers | `/health`, `/api/models` and `/api/skills` are available for capability evidence | Credential-free route contract verified; real service boot not claimed |

## Contract gaps

1. The reviewed embedded `DeerFlowClient` surface has no stable cancel method matching `IF-RUNTIME-001`; it remains a rejected boundary fixture and reports `RUNTIME_CONTRACT_GAP`.
2. The Gateway route family provides an external cancel lifecycle, and the PI adapter maps it through injected HTTP transport. Gateway HTTP/SSE contract is verified; real DeerFlow model execution is not.
3. Resume semantics and adopted runtime version are not frozen.

## Boundary decision for this PoC

PI owns the outer runtime contract, public event projection, permission boundary, and secret boundary. The Gateway HTTP/SSE surface is the preferred PoC external boundary because it preserves process/failure isolation and exposes cancel lifecycle; this is a PoC candidate, not an accepted ADR or Architecture Freeze. No Research Domain change, fork, or provider key injection is authorized by this note.
