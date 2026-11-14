# Contributing to `maturity-model-digital-transformation`

## Change control

Changes go through a pull request with a rationale and a `CHANGELOG.md`
entry. Semver applies:

- **MAJOR** — scale, evaluation or level definition change
- **MINOR** — new dimension, criterion or component reference
- **PATCH** — clarifications, corrections, additional evidence examples

## Rules

1. **Do not alter model semantics without a change request.** Scale levels,
   evaluation weights, criteria and evidence are the model's substantive
   content; changing them changes what the instrument measures.
2. **Scale and scoring anchor are part of the model definition.** The
   composite model-owned scale (`maturity/scale.yaml`) and the OpenDEA EA
   evaluation anchor (`dea-evaluation-opendea-enterprise-architecture-v1`)
   change only through a change request; canonical semantics remain owned by
   `technehub-labs/dea-metamodel`.
3. **Component kinds are explicit.** The four `components/` references follow
   CR-AM-10 §4 — `import`, `extend`, `override`. Kindless references are
   refused by the Level 1 validator.
4. **References are immutable.** Every external reference (component, scale,
   dependency) must be a tag `vX.Y.Z`, a 40-character commit SHA, or a
   sha256 digest. `main`, `master` and `latest` are rejected by CI.
5. **Level 1, Level 2 and the repository-standard gate must be green** before
   merge. Level 2 resolves the handshake against the pinned
   `dea-metamodel` release.
6. **Model identity is the registration id.** The `id` in `model.yaml` must
   match the id in `Assessment-Models/assessment-registry`. The repository
   name is a location, not an identity.
7. **Version coherence is machine-checked.** `model.yaml`, `VERSION`, the
   README `## Status` line and `standard.yaml` must always agree — the
   repository-standard conformance workflow fails the build on drift.

## Registering a release

After a release is tagged, add or update the registration record under
`Assessment-Models/assessment-registry/registry/` with the immutable tag
reference. A record must not point at a repository or reference that does
not resolve — the ecosystem validator checks this.

## Licence

By contributing you agree that your contributions are licensed under the MIT
licence of this repository.
