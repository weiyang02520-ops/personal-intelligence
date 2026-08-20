# M0 Reuse Audit Framework

Source task: TASK-M0-001  
Status: COMPLETE — framework only  
Decision authority: External Architecture Review / explicit ADR, not this artifact

## Required record

Each candidate record must contain:

| Field | Required evidence |
|---|---|
| Capability / candidate | What boundary is being evaluated |
| Repository / URL | Canonical upstream location |
| Exact commit / version / date | Reproducible review point |
| License | License file or official terms; unknown is not acceptable as PASS |
| Active status | Release/commit/maintenance evidence |
| Relevant files/interfaces/classes/functions | Code-level anchor, not README-only |
| Claimed capability | What upstream claims |
| Code/interface/behavior evidence | L1/L2/L3 status separately |
| Integration/security evidence | L4/L5 status separately |
| Hard dependencies | Runtime, DB, cloud, credentials, OS or browser assumptions |
| Failure modes | Timeout, cancellation, retry, partial result, upgrade, security |
| Fit | Boundary and ownership fit for Personal Intelligence |
| Decision candidate | REUSE / ADAPT / REFERENCE / REJECT / UNKNOWN |
| Plan reuse mode | DIRECT_DEPENDENCY / ADAPTER / ALGORITHM_REFERENCE / UI_REFERENCE / INFRASTRUCTURE_OPTION / REJECT |
| Open questions | What must be tested or decided later |

## Evidence levels

| Level | Meaning | Permitted claim |
|---|---|---|
| L0 | Name, search result or README claim only | Candidate exists; no capability claim |
| L1 | Source, docs or license inspected | Capability appears in inspected source/docs |
| L2 | Callable interface or extension surface inspected | Boundary may be mapped; behavior unproven |
| L3 | Reproducible isolated behavior | Behavior claim at the tested scenario |
| L4 | PI boundary integration evidence | Integration candidate only |
| L5 | Security/trust/permission evidence | Security claim only for tested boundary |

## Status rules

`PASS` means the stated audit question is evidenced at the required level. `PARTIAL` means some capabilities or conditions pass but important gaps remain. `FAIL` means the candidate does not meet the stated condition. `UNKNOWN` means evidence is insufficient. A README-only statement cannot produce `PASS` for code/API/behavior/integration/security.

## Classification rules

`REUSE` requires verified existing capability and explicit future architecture acceptance. `ADAPT` means a bounded adapter/patch is likely. `REFERENCE` means conceptual or visual reuse only. `REJECT` records a negative decision candidate. `UNKNOWN` preserves uncertainty. A `Build` label from the plan is represented as `PI CUSTOM DESIGN CANDIDATE`; it is not an implementation authorization.

## Minimal audit checklist

- [x] Unified status and evidence vocabulary.
- [x] Repository/version/license/maintenance fields.
- [x] Code/interface/behavior/integration/security separation.
- [x] Failure modes and hard dependencies.
- [x] Reuse classification and plan-mode mapping.
- [x] Explicit no-ADR-acceptance rule.

## Validation

The framework is document-only. Validation is required-field scan plus `git diff --check`; no third-party code is executed by TASK-M0-001.
