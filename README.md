# Digital Transformation Maturity Model

**The first independent model in the Assessment-Models ecosystem.** CR-AM-11
§31 first-model candidate, demonstrating all three CI levels on the same
repository (§14):

| Level | What runs here | What it checks |
|---|---|---|
| 1 | `.github/workflows/local-model-ci.yml` | Schema validation, vocabulary compliance, internal reference integrity, version consistency, examples |
| 2 | `.github/workflows/contract-conformance.yml` (reusable from `Assessment-Models/assessment-ci`) | Manifest + handshake against a pinned `technehub-labs/dea-metamodel` release; suite-resolved contract family + version (§15) |
| 3 | (re-uses `Assessment-Models/assessment-registry` resolution) | Immutability of every external reference; registry cross-checks record on this model |

This model is a **composite** spanning operations, technology, and
services-delivery child models. It uses the **OpenDEA EA reference instance**
(scale + evaluation + Benchmark 2026 baseline) as its scoring anchor.

## Status

`1.1.0-alpha` · composite model `1.0.0` stable + additive **operationalized** model line `1.0.0-alpha` · anchored on the OpenDEA EA reference instance

## Model lines (cross-reference)

This repository hosts the digital-transformation domain with two model lines:

| Line | Version | Definition | Scale | Status |
|---|---|---|---|---|
| Composite (CR-AM-11 §31 first-model candidate) | 1.0.0 | `maturity/evaluation.yaml` + `maturity/components/` (structure mapping in `standard.yaml`) | `dea:scale-digital-transformation-v1` (L-0..L-4) | stable |
| **Operationalized** (digital-business framing; from TM Forum DMM v5.0.2 re-harvest) | 1.0.0-alpha | `maturity/operationalized/` (scale + evaluation + model register 6 dims / 23 sub-dims / 70 criteria + 6 dimension components) + `examples/operationalized-2026.yaml` | `dea:scale-digital-transformation-operationalized-v1` (L-0..L-4, value-named levels, correlated 1:1 to the composite scale — never normalised, CR-AM-09 §9) | alpha |

Cross-references: catalog twin `dea:maturity-digital-transformation-operationalized` in
`dea-catalog-maturity-models` (PRs #6/#10/#12, proposal 0003 with the DMM v5.0.2 gap review);
registry issues `assessment-registry#11/#12/#13`; full mapping in
`mappings/digital-transformation-operationalized.yaml`. Added additively per repository
standard rules R1/R2 — nothing renamed, moved, or deleted.

## Repository standard

This repository declares adoption of
[AM-MODEL-REPOSITORY-STANDARD](https://github.com/Assessment-Models/maturity-model-standard)
v1.0.1 (CR-AM-ORG-RES-000) at conformance level **`structural`** via a root
`standard.yaml` declaration, validated by the reusable repository-standard
workflow — an additive gate alongside Levels 1/2/3. The composite model
definition (`maturity/evaluation.yaml` + `maturity/components/`) satisfies
the `model-definition` role through a **recorded structure mapping** (added
in standard v1.0.1, maturity-model-standard#3; rule R1: map, never rename;
migration matrix M2), integrity-checked and logged by the conformance gate.
`model.yaml` remains the authoritative identity manifest.

## Conformance contract (CR-AM-11 §15)

```yaml
conformance:
  contract:
    id: maturity-scale-contract        # resolves to family maturity-scale-contract in the pinned suite
  source:
    organization: technehub-labs
    repository: dea-metamodel
  version: "1.0"                        # any prefix of the published 1.0.0 satisfies
```

Resolved live by [`Assessment-Models/assessment-ci/scripts/resolve_contract.py`](https://github.com/Assessment-Models/assessment-ci/blob/main/scripts/resolve_contract.py) against the published [`assessment-models/contracts/contract-suite.yaml`](https://github.com/technehub-labs/dea-metamodel/blob/main/assessment-models/contracts/contract-suite.yaml).

## Layout

```
maturity-model-digital-transformation/
├── README.md                              ← this file
├── model.yaml                             ← the contract handshake (Level 2 entry point)
├── standard.yaml                          ← repository-standard declaration (CR-AM-ORG-RES-000)
├── VERSION
├── maturity/
│   ├── scale.yaml                         ← composite model-owned scale (5-level digital-native)
│   ├── evaluation.yaml                    ← weighted 0–100 evaluation over four criteria
│   ├── components/                        ← CR-AM-10 components (reusable)
│   └── operationalized/                   ← operationalized model line v1.0.0-alpha (added 1.1.0-alpha)
│       ├── scale.yaml / evaluation.yaml / model/ / components/
├── mappings/                              ← cross-references (incl. operationalized model line)
├── examples/
│   ├── enterprise-2026.yaml               ← composite worked example
│   └── operationalized-2026.yaml          ← operationalized worked example
├── .github/workflows/
│   ├── local-model-ci.yml                 ← Level 1
│   ├── contract-conformance.yml           ← Level 2 (reusable workflow_call)
│   └── repository-standard.yml            ← repository-standard conformance (reusable)
└── scripts/
    └── local_validate.py                  ← Level 1 validator (extended for operationalized/)
```

## Reuse from CR-AM-10

The four `components/` files import reusable maturity components from the
OpenDEA Component Registry (`dea:component-*`). The kind field is explicit
per CR-AM-10 §4 — `import` (consumer), `extend` (override criteria),
`override` (replace dimensions). Kindless references are refused by the
Level 1 validator.

---

*Established under [CR-AM-11 — Federated Assessment Model Ecosystem](https://github.com/technehub-labs/dea-metamodel/blob/main/change-requests/CR-AM-11.md) Phase 4.*
