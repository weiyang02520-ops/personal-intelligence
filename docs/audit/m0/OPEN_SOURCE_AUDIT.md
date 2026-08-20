# M0 Open-Source Audit Umbrella

Status: M0 evidence preparation / External Review required  
Canonical Blueprint: [`docs/plan(4).md`](../../plan(4).md)  
Scope: TASK-M0-001..014 only  
Architecture Status: NOT FROZEN

## Purpose

This is the umbrella index for M0 reuse, runtime, provider, algorithm, UI, infrastructure and security evidence. It is an evidence record, not an architecture decision and not an authorization to enter PoC or M1.

## Canonical Artifacts

| Capability | Canonical artifact | Source task |
|---|---|---|
| Audit schema and evidence rules | [`REUSE_AUDIT.md`](REUSE_AUDIT.md) | M0-001 |
| Runtime and extension surface | [`RUNTIME_AUDIT.md`](RUNTIME_AUDIT.md) | M0-002..004, M0-012 |
| Search, crawler and connector options | [`SEARCH_PROVIDER_AUDIT.md`](SEARCH_PROVIDER_AUDIT.md) | M0-007..009 |
| Research/discovery algorithm references | [`ALGORITHM_REUSE_AUDIT.md`](ALGORITHM_REUSE_AUDIT.md) | M0-005..006 |
| UI references | [`UI_REFERENCE_AUDIT.md`](UI_REFERENCE_AUDIT.md) | M0-010 |
| Cross-capability decisions | [`REUSE_DECISION_MATRIX.md`](REUSE_DECISION_MATRIX.md) | M0-011, M0-013 |
| Strategy candidates | [`STRATEGY_REGISTRY.md`](STRATEGY_REGISTRY.md) | M0-006, M0-013 |

`OPEN-SOURCE-AUDIT.md`, `REUSE-MATRIX.md` and `STRATEGY-REGISTRY.md` from PART 05.8 are legacy aliases in this repository. They are not parallel sources of truth; the files above are canonical.

## Classification Vocabulary

- `REUSE`: existing capability is verified at the required boundary and may be considered for direct reuse, subject to explicit architecture acceptance.
- `ADAPT`: existing capability is usable only through a thin adapter or bounded integration; not an accepted dependency.
- `REFERENCE`: ideas, algorithms, UI primitives or patterns only; no code adoption implied.
- `REJECT`: evidence shows unacceptable fit, license, security, maintenance or boundary risk.
- `UNKNOWN`: evidence is insufficient; no positive reuse claim is allowed.

The plan's `DIRECT_DEPENDENCY`, `ADAPTER`, `ALGORITHM_REFERENCE`, `UI_REFERENCE` and `INFRASTRUCTURE_OPTION` labels are retained as evidence fields and mapped to the canonical vocabulary above. `Build` in TASK-M0-013 means PI custom design candidate, not implementation started.

## Evidence Levels

`L0 UNVERIFIED` = name/claim only; `L1 SOURCE` = repository/document inspected; `L2 INTERFACE` = public API or extension surface inspected; `L3 BEHAVIOR` = reproducible behavior evidence; `L4 INTEGRATION` = isolated PI-boundary verification; `L5 SECURITY` = trust/permission/security verification. M0 may record L0-L5 but must not promote weak evidence silently.

## Governance

M0 reports may recommend options, record conflicts and propose ADR updates. Only an explicit architecture decision/review may accept Runtime, DB, Queue, Provider, Public API, Domain state or module-boundary changes. `M0-GATE-001` must remain non-PASS until External Review.

## Coverage Status

M0-001 framework: COMPLETE  
M0-002..012 audits: COMPLETE WITH PARTIAL/UNKNOWN EVIDENCE  
M0-013 synthesis: COMPLETE AS DECISION CANDIDATES  
M0-014 gate packet: READY_FOR_EXTERNAL_REVIEW  

Known global limitation: no credentials, live provider calls, upstream execution or architecture acceptance was performed in this M0 batch.
