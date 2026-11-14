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

`1.0.0` · stable — composite model, anchored on the OpenDEA EA reference instance

## Repository standard

This repository declares adoption of
[AM-MODEL-REPOSITORY-STANDARD](https://github.com/Assessment-Models/maturity-model-standard)
v1.0.0 (CR-AM-ORG-RES-000) at conformance level **`registered`** via a root
`standard.yaml` declaration, validated by the reusable repository-standard
workflow — an additive gate alongside Levels 1/2/3. The composite model
definition (`maturity/evaluation.yaml` + `maturity/components/`) is **mapped,
not restructured** (migration matrix M2); `model.yaml` remains the
authoritative identity manifest.

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
│   ├── scale.yaml                         ← the composite model-owned scale (5-level digital-native)
│   ├── evaluation.yaml                    ← weighted 0–100 evaluation over four criteria
│   └── components/
│       ├── digital-culture.yaml           ← CR-AM-10 component (reusable)
│       ├── technology-adoption.yaml
│       ├── operations-modernization.yaml
│       └── services-delivery.yaml
├── examples/
│   └── enterprise-2026.yaml              ← worked scoring example
├── .github/workflows/
│   ├── local-model-ci.yml                 ← Level 1
│   ├── contract-conformance.yml           ← Level 2 (reusable workflow_call)
│   └── repository-standard.yml            ← repository-standard conformance (reusable)
└── scripts/
    └── check_immutable_refs.py            ← Level 3 immutable-reference guard (consumer copy)
```

## Reuse from CR-AM-10

The four `components/` files import reusable maturity components from the
OpenDEA Component Registry (`dea:component-*`). The kind field is explicit
per CR-AM-10 §4 — `import` (consumer), `extend` (override criteria),
`override` (replace dimensions). Kindless references are refused by the
Level 1 validator.

---

*Established under [CR-AM-11 — Federated Assessment Model Ecosystem](https://github.com/technehub-labs/dea-metamodel/blob/main/change-requests/CR-AM-11.md) Phase 4.*
