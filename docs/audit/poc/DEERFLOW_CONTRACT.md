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
| Gateway lifecycle | `backend/app/gateway/app.py` and gateway `AGENTS.md` | API/gateway route family covers thread runs, streaming, cancellation/join, skills/MCP/artifacts | Not imported into M0/M1 Product Core; future adapter decision remains open |

## Contract gaps

1. The reviewed embedded `DeerFlowClient` surface has no stable cancel method matching `IF-RUNTIME-001`. `DeerFlowRuntimeAdapter.cancel()` therefore returns an explicit `RUNTIME_CONTRACT_GAP` error rather than inventing semantics.
2. Resume semantics and adopted runtime version are not frozen.
3. A real credentialed runtime path was not claimed in this PoC. Fixture tests prove translation only; source evidence proves the inspected surface.

## Boundary decision for this PoC

PI owns the outer runtime contract, public event projection, permission boundary, and secret boundary. DeerFlow remains a runtime candidate behind a thin adapter. No Research Domain change, fork, provider key injection, or Architecture Freeze is authorized by this note.
