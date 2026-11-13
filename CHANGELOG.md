# Changelog

## [Unreleased] — CR-AM-11 Phase 5: component references normalized

### Changed

- `model.yaml` component references now source from
  `Assessment-Models/maturity-components` (the published component packages,
  CR-AM-11 §18–20) instead of `technehub-labs/dea-metamodel`. The upstream
  canonical component registry stays in dea-metamodel
  (`assessment-models/maturity/components/registry.yaml`, CR-AM-10); consumers
  reference component releases from the maturity-components repository. All
  references remain immutable (`v1.0.0` tag) and keep their CR-AM-10 §4 kinds
  (import / extend / override).

## [Unreleased] — CR-AM-11 Phase 4: First independent model (Digital Transformation)

The first independent model in the Assessment-Models ecosystem. CR-AM-11
§31 first-model candidate, demonstrating all three CI levels on the same
repository (§14).

### Added — Model
- **model.yaml** — the §15 contract handshake (contract: maturity-scale-contract,
  source: technehub-labs/dea-metamodel, version: 1.0) plus four kinded
  component references (import / extend / override per CR-AM-10 §4).
- **maturity/scale.yaml** — composite 5-level model-owned scale (L-0 Absent
  → L-1 Piloting → L-2 Defined → L-3 Scaled → L-4 Self-Optimising). Linear
  topology, exponential progression, per-level effort_multiplier
  (1.0× / 1.5× / 2.5× / 4.0× / 6.0×).
- **maturity/evaluation.yaml** — weighted 0–100 aggregation over four
  criteria (digital-culture, technology-adoption, operations-modernization,
  services-delivery) with per-level expectations covering all five levels.
- **maturity/components/** — four CR-AM-10-kinded components: digital-culture
  (import), technology-adoption (import), operations-modernization (extend
  with two composite dimensions), services-delivery (override the
  canonical cadence with platform-engineering).
- **examples/enterprise-2026.yaml** — worked scoring run: aggregated score
  78.60 resolves to L-3 (Adaptive) under the v2 band scheme; effort-adjusted
  value 314.40 reflects the maturity-v2 diminishing-returns insight at L-3.

### Added — CI (three levels on this same repository)
- **Level 1 — `.github/workflows/local-model-ci.yml`**: schema + scale +
  evaluation + component-kind guard + example-scoring math correctness.
  Local simulation: OK — model + scale + evaluation + 4 components + 1
  example all consistent.
- **Level 2 — `.github/workflows/contract-conformance.yml`**: consumes the
  reusable Level 2 workflow from `Assessment-Models/assessment-ci` at the
  pinned dea-metamodel release (commit SHA `1bbc08d0` from Phase 3 merge).
- **Level 3 — Level 1 + Level 2 together** demonstrate all three levels on
  this same model per §31. Cross-ecosystem validation (Level 3 in the
  stricter sense — registry-population checks) lands as a follow-on once
  the registry has a meaningful population.