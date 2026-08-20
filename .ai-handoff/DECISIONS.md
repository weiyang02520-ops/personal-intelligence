# DECISIONS

## Current confirmed facts

- The project repository is `weiyang02520-ops/personal-intelligence`.
- Repository visibility is Public.
- The canonical Blueprint copy is `docs/plan(4).md`.
- Architecture is not frozen.
- No Product Core implementation is started.

## Not decisions

Backend language, database, queue, Runtime selection, Provider mix, API schema details and unresolved Domain ownership remain TBD/PROPOSED as documented in `docs/plan(4).md` and `docs/audit/OPEN_TBDS.md`.

## M0 evidence decisions (not architecture decisions)

- `docs/audit/m0/` is the canonical M0 audit namespace; PART 05.8 names are legacy aliases.
- M0 classifications are evidence candidates: REUSE, ADAPT, REFERENCE, REJECT, UNKNOWN.
- M0-013/014 may synthesize and prepare a Gate packet but may not accept ADRs or mark `M0-GATE-001 PASS`.
- Current candidate directions: Pi ADAPT with external sandbox; DeerFlow ADAPT/UNKNOWN pending contract/security proof; research/discovery/UI mostly REFERENCE; provider/crawler/queue remain PoC inputs.

## External Review update

- `M0-GATE-001`: `PASS_WITH_NOTES`.
- Physical Architecture PoC is authorized; Architecture Freeze is not.
- M1 remains unauthorized until `POC-GATE-001` is externally reviewed.
- DeerFlow reviewed upstream commit is pinned; adopted runtime version remains NOT FROZEN.
- Reuse Decision Classification and Plan Reuse Mode are separate fields.
