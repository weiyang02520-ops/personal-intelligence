# Search Cancellation Contract Conflict

Status: OPEN SPEC CONFLICT — no Search cancellation implementation was invented.

## Inspection

The canonical Blueprint defines Search ownership and SearchGateway normalization, including timeout, retry, provider degradation, provenance and deduplication. The same Blueprint places cancellation in the Research/Runtime path (`cancelResearch`, `cancelExecution`, and UI → Research Application → Research Execution Control → AgentRuntime). A direct search for `IF-SEARCH-001` and a Search-specific cancellation contract in `docs/plan(4).md` found no canonical definition.

## Affected scope

- `TASK-POC-006` requires a Search cancellation case even though the canonical contract does not define one.
- `SearchGateway` and the Search provider boundary would be affected if a new cancellation token or error became mandatory.
- No Product Requirement or public API was changed in this closure batch.

## Decision for this batch

Do not invent a Search cancellation API. The existing timeout/provider error contract remains unchanged. `TASK-POC-006` is `PARTIAL` pending an architecture/spec owner decision on whether cancellation belongs to Search execution or only to Research/Runtime cancellation.

## Minimal resolution options

1. Remove Search cancellation from the Task requirement and keep cancellation at Runtime/Research execution control.
2. Add an explicit canonical Search execution contract, error, token semantics and tests before changing the gateway.

This is an External Review/spec-owner decision. It does not authorize Architecture Freeze or M1.
