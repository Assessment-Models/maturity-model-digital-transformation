# CR-DT-01 — Digital Transformation Model Documentation Architecture

**Status:** Proposed  
**Change class:** Documentation architecture and model-definition reconciliation  
**Repository:** `Assessment-Models/maturity-model-digital-transformation`  
**Scope:** Both model lines, with the operationalized model as the primary enterprise-assessment narrative

## 1. Problem statement

The repository contains substantive model artifacts, but its entry-point documentation does not yet give readers a reliable understanding of digital transformation, the distinction between the two model lines, the assessment method, the evidence expected, or how different stakeholder personas should use the model.

The current documentation also contains cross-artifact inconsistencies. Rewriting prose alone would risk presenting unresolved semantics as settled facts.

## 2. Change objective

Establish a coherent documentation system that:

1. Explains digital transformation as enterprise-wide change in value creation and realization, not merely technology adoption.
2. Clearly distinguishes the **Composite** and **Operationalized** model lines.
3. Presents the Operationalized model's six dimensions, declared 23 subdimensions and 70 criteria as the primary detailed assessment structure.
4. Explains assessment scope, evidence, scoring, maturity resolution, interpretation and improvement planning.
5. Provides role-based entry points for executives, transformation leaders, enterprise architects, business and operations leaders, technology and data leaders, assessors, and model contributors.
6. Uses consistent diagrams and worked examples that are traceable to repository artifacts.
7. Makes unresolved model-definition issues visible and assigns them to explicit reconciliation work rather than hiding them in documentation.

## 3. Normative boundaries

This CR governs the documentation architecture and the minimum reconciliation required for documentation accuracy.

It does **not** silently redefine model semantics, scoring, maturity levels, weights, mandatory dimensions, benchmarks or assessment outcomes. Such changes require separately reviewed model-definition changes and corresponding versioning.

The model remains independently governed in this repository. Shared Assessment-Models standards govern repository structure, contracts, registry integration and conformance; they do not replace the model's own intellectual content.

## 4. Documentation deliverables

| Deliverable | Required content |
|---|---|
| Root README | Purpose, scope, model-line distinction, architecture figures, dimensions, maturity scale overview, assessment journey, personas, quick navigation and status |
| Model reconciliation | Artifact inventory, contradictions, impact, decisions required and ownership boundaries |
| Assessment methodology | Scope, evidence, rating, aggregation, maturity resolution, confidence, interpretation and improvement cycle |
| Persona guide | Questions each persona should ask, relevant model views, expected outputs and suggested reading path |
| Worked example | Clearly labelled illustrative assessment, calculation trace and limitations |
| Change traceability | Links from documentation statements to authoritative YAML and example artifacts |

## 5. Model reconciliation requirements

The following items must be resolved or explicitly marked as unresolved before any documentation claims them as normative:

### R1 — Scale identifier and level semantics

- Distinguish L-0 Not Assessed from capability maturity levels.
- Reconcile scale descriptions, comments, evaluation references and examples.
- Confirm whether the five capability levels are L-1 through L-5 for both model lines.
- Do not describe a five-level scale as L-0 through L-4 if L-0 is a non-maturity sentinel.

### R2 — Evaluation-to-scale resolution

- Make each evaluation model's resolution range consistent with its corresponding scale.
- Confirm how band boundaries map to level identifiers.
- Confirm the highest-conformant-level rule and mandatory-dimension gate, including treatment of unassessed criteria and incomplete evidence.

### R3 — Version and status authority

- Define the meaning and authority of repository VERSION, model.yaml version, standard.yaml version, model-line versions, scale/evaluation versions, mapping metadata and example model references.
- Correct stale comments and references only after version ownership is agreed.
- Preserve the distinction between repository release status and each model line's maturity/status.

### R4 — Criterion scoring semantics

- Specify the conversion from criterion ratings (described as 1–5) to the 0–100 score domain.
- Define treatment of missing, not-assessed, not-applicable and insufficient-evidence responses.
- Confirm aggregation precision, rounding and boundary behavior.

### R5 — Effort-adjusted value

- Define the semantic purpose, units, normalization and intended use of the effort multiplier.
- Explain why the resulting value may exceed 100, or change the construct through a separately governed model change.
- Do not present the effort-adjusted result as enterprise value or realized financial value without an explicit definition.

### R6 — Evidence and confidence

- Define evidence quality, recency, provenance, ownership, sampling and validation.
- Define how evidence confidence affects criterion scores and maturity resolution.
- Make evidence traceability inspectable from assessment result to criterion and source artifact.

### R7 — Model boundary and specialist depth

- The Digital Transformation model provides broad enterprise coverage.
- Deep autonomous/adaptive operations capability assessment belongs to the specialist Autonomous Operations model.
- The Digital Transformation model may assess strategic intent, adoption, governance and outcomes related to autonomy without duplicating the specialist model's detailed operational criteria.

## 6. Documentation architecture

Recommended structure:

```text
README.md
change-requests/
  CR-DT-01.md
docs/
  reconciliation/
    model-reconciliation.md
  methodology/
    assessment-methodology.md
  guides/
    persona-guide.md
```

The machine-readable model artifacts remain authoritative for model identity, dimensions, criteria, weights, scale, evaluation and examples. Documentation explains and navigates those artifacts; it must not become a competing specification.

## 7. Acceptance criteria

- [ ] README explains the purpose and boundary of Digital Transformation maturity.
- [ ] README distinguishes Composite and Operationalized model lines without implying score interchangeability.
- [ ] Six Operationalized dimensions and their weights are represented accurately.
- [ ] L-0 is consistently described as Not Assessed, not as a maturity level.
- [ ] L-1 through L-5 are presented as five capability maturity levels only where supported by the relevant scale.
- [ ] The L-0…L-4 versus L-5 evaluation-resolution contradiction is recorded and not obscured.
- [ ] Version/status discrepancies are documented with source paths.
- [ ] Criterion-to-0–100 conversion and effort-adjusted value are marked as unresolved until formally specified.
- [ ] Assessment methodology covers evidence, scoring, aggregation, resolution, interpretation and improvement.
- [ ] Persona guidance is provided for executive, transformation, architecture, business/operations, technology/data, assessor and model-maintainer audiences.
- [ ] Diagrams render in GitHub Markdown and correspond to the described model structure.
- [ ] All examples are labelled illustrative unless backed by an approved benchmark or validated assessment.
- [ ] Documentation changes do not silently alter machine-readable model semantics.

## 8. Delivery sequence

1. Reconcile the current artifacts and publish the reconciliation record.
2. Publish the methodology and persona guide with explicit unresolved-semantic warnings.
3. Replace the root README with a persona-oriented entry point and diagrams.
4. Resolve model-definition issues through separately reviewed CRs before claiming full normative consistency.
5. Add CI checks for documentation links, Mermaid syntax where supported, and model/documentation cross-reference integrity.

## 9. Out of scope

- Redesigning the six dimensions or their weights.
- Changing the 23-subdimension/70-criterion register.
- Replacing the Composite model with the Operationalized model.
- Changing maturity bands, progression topology or benchmark baselines.
- Rewriting the Autonomous Operations maturity model.
- Declaring an illustrative example to be a benchmark.

## 10. Governance note

This CR is a documentation change proposal and reconciliation record. It is not approval to mutate unresolved model semantics. Any such mutation must be separately proposed, reviewed, versioned and validated against the applicable Assessment-Models contracts.
