# CR-DT-02 — Normative Scoring, Evidence and Maturity Resolution

**Status:** Proposed  
**Change class:** Model-definition and evaluation-contract clarification  
**Repository:** `Assessment-Models/maturity-model-digital-transformation`  
**Applies to:** Composite and Operationalized model lines  
**Predecessor:** CR-DT-01 (documentation architecture)

## 1. Problem statement

The repository now has a coherent reader-facing description, but the machine-readable evaluation artifacts do not yet define a complete, reproducible path from criterion-level assessment to reported maturity.

The two model lines use different assessment structures and must retain distinct evaluation contracts. Both use the definitive five-level capability sequence **L-1 through L-5**, with **L-0 Not Assessed** reserved as a non-maturity sentinel. That adopted numbering is not under reconsideration by this CR.

The present artifacts leave material scoring and resolution behavior implicit, split across descriptions, scale fields, examples and validator assumptions. As a result, an assessor or independent implementation cannot reliably reproduce every reported result from criterion evidence.

## 2. Change objective

Establish a normative, testable evaluation specification for each model line that:

1. Defines the complete calculation from criterion response through subdimension, dimension and overall result where applicable.
2. Defines the distinction between a valid low rating, Not Assessed, Not Applicable and insufficient or invalid evidence.
3. Defines score conversion, aggregation, weighting, precision, rounding and score-band boundary behavior.
4. Defines evidence sufficiency, confidence and how these affect scoring and maturity resolution.
5. Defines mandatory-dimension and mandatory-criterion gates, including their interaction with weighted scores.
6. Defines the exact algorithm for resolving a score and conformance findings to L-1…L-5.
7. Defines the role and reporting semantics of effort multipliers, or removes that derived measure through a separately justified decision within this CR.
8. Supplies criterion-level worked examples and automated tests that prove the normative rules.

## 3. Adopted invariants

The following are fixed constraints, not options for reopening:

- **L-1…L-5** are the five capability maturity levels.
- **L-0 Not Assessed** is a sentinel state and is not a capability maturity level.
- A Not Assessed response must not be interpreted as evidence that capability is Absent.
- The Composite and Operationalized model lines remain distinct model definitions. Aligned level identifiers do not make their criteria, evidence, weights, scores or results interchangeable.
- The Operationalized model retains its six dimensions and current declared weights as the baseline for this CR: D1 0.20, D2 0.20, D3 0.20, D4 0.15, D5 0.10, D6 0.15. This CR does not authorize changing the dimensions or weights without an explicit decision and impact analysis.
- D1–D4 are currently designated mandatory and D5–D6 optional in the Operationalized evaluation. This CR must make the operational meaning of those designations explicit; it must not silently remove or weaken the gate.
- Existing maturity-band identifiers and ranges are treated as the current baseline. Any proposed change to them must be separately justified, versioned and assessed for historical comparability.

## 4. Current artifact observations

The following are initial findings from the merged `main` branch. They define the investigation baseline, not pre-approved solutions.

| ID | Artifact / concern | Current observation | Required resolution |
|---|---|---|---|
| F-01 | `maturity/operationalized/evaluation.yaml` | States “criterion 1-5 -> 0-100” but does not define the conversion function. | Define the exact mapping, including endpoints and intermediate values. |
| F-02 | `maturity/operationalized/model/d1.yaml` … `d6.yaml` | Criteria have five ordinal anchors (1–5), while the worked example supplies dimension scores directly. | Define how anchor ratings become criterion scores and how a criterion result is derived from evidence. |
| F-03 | Operationalized `lite_question` fields | Each subdimension has a five-point rapid-assessment question, but its relationship to full criterion assessment is not defined. | Define whether the lite path is screening, proxy scoring or a separate assessment mode, and prohibit unsupported equivalence. |
| F-04 | `maturity/operationalized/evaluation.yaml` | Declares mean-based subdimension/dimension aggregation and weighted overall aggregation, but omits missing-data, applicability and rounding rules. | Specify denominator, coverage and precision behavior at every aggregation level. |
| F-05 | Both scale artifacts | L-0 is described as scoring zero and lowering evidence confidence. | Separate unassessed status from a valid zero/lowest-capability rating; define how unassessed data affects coverage, confidence and aggregation without fabricating a maturity observation. |
| F-06 | Both evaluation artifacts | Refer to highest-conformant-level resolution; the Composite evaluation also lists evidence confidence and ecosystem participation as resolution inputs. | Define the complete, executable resolution algorithm and the role of each input. |
| F-07 | Operationalized evaluation | D1–D4 are mandatory, but the precise gate logic is not expressed as a formal rule. The example notes that all four dimensions are at least 46. | Define mandatory dimension/criterion thresholds, treatment of incomplete mandatory evidence and the interaction with the aggregate band. |
| F-08 | Scale progression | Declares forward-only progression and no level skipping, while assessment artifacts do not define whether this is a cross-sectional rating constraint, a longitudinal transition rule or both. | Separate current-state classification from longitudinal improvement constraints and define evidence needed for a claimed transition. |
| F-09 | Both scale artifacts and examples | Effort multipliers (1.0, 1.5, 2.5, 4.0, 6.0) are applied to a 0–100 score, producing values above 100 (for example, 168.0 and 314.4). | Define construct, unit, mathematical purpose, aggregation point and reporting name, or recommend retirement. |
| F-10 | `maturity/scale.yaml` | Its top-level description still describes L-0 Absent through L-4 Self-Optimising, despite the adopted L-0 sentinel and L-1…L-5 capability sequence. | Correct stale descriptive metadata as part of implementation after the intended scale semantics are confirmed. |
| F-11 | `scripts/local_validate.py` | Validator comments still describe old ordinal ranges and model-level assumptions; checks do not fully prove criterion-to-result semantics or Operationalized weighted example integrity. | Replace descriptive-only checks with executable conformance tests for the agreed rules. |
| F-12 | Composite evaluation | Uses four 0–100 component scores and weights 0.20/0.30/0.25/0.25, with two mandatory components, but its relationship between component-level expectations, weighted score bands and mandatory resolution needs a formal algorithm. | Specify the Composite contract independently from the Operationalized contract. |

## 5. Required specification decisions

### 5.1 Assessment response states

Define and distinguish at least:

- **Rated:** a criterion has been assessed against its anchors and has sufficient evidence for a rating.
- **Not Assessed (L-0):** no defensible rating has been established.
- **Not Applicable:** the criterion is legitimately outside the declared assessment scope, with rationale and approval.
- **Insufficient Evidence:** evidence was considered but does not support a defensible rating.
- **Invalid / Conflicting Evidence:** evidence is contradictory, unreliable or fails the applicable validation requirements.

The specification must state which states are permitted at criterion, subdimension and dimension levels, and how each contributes to coverage, confidence, aggregation and maturity resolution. Not Assessed must never be silently converted to a numeric zero or to L-1 Absent.

### 5.2 Criterion rating and score conversion

For the Operationalized line, define the transformation from five ordinal evidence anchors to the numeric scoring domain, including:

- Whether the anchors are ordinal categories or equally spaced numeric values.
- Whether the conversion is linear, non-linear or lookup-based.
- Exact mapping for all five anchor positions.
- Whether assessors may use intermediate ratings and, if so, how.
- How evidence confidence qualifies or constrains a rating.

For the Composite line, define how each component's native 0–100 score is established and how its level expectations and mandatory status constrain resolution.

Do not assume that an arithmetic mapping is valid merely because the anchors are numbered 1–5. The chosen rule must be justified and testable.

### 5.3 Aggregation and missingness

Specify the exact calculation and denominator at each level:

- Criterion → subdimension.
- Subdimension → dimension.
- Dimension → overall model score.
- Composite component → Composite overall score.

Define the behavior for Not Assessed, Not Applicable, insufficient evidence, partial coverage and mandatory omissions. Specify whether weights are renormalized, whether minimum coverage thresholds apply, and when an overall result must be withheld rather than calculated.

Define numeric precision, intermediate rounding, final rounding and score-band assignment. Boundary tests must cover values immediately below, exactly at and immediately above every band boundary.

### 5.4 Evidence confidence

Define evidence quality and sufficiency in operational terms, including provenance, recency, relevance, ownership, corroboration and assessor verification.

Specify whether confidence is:
- a separate reported dimension of assessment quality;
- a constraint on whether a criterion can receive a rating;
- an input to maturity resolution; or
- some explicitly justified combination.

Avoid applying an opaque confidence multiplier that changes a capability score without a transparent rationale and traceable calculation.

### 5.5 Maturity and conformance resolution

Specify an unambiguous algorithm that determines:

- the score band;
- the candidate maturity level;
- mandatory criterion and dimension gate outcomes;
- highest conformant level;
- final resolved level or a non-level outcome such as Not Assessed / insufficient evidence;
- conformance status and its relationship to maturity.

The specification must explain whether a high weighted score can be capped by a mandatory dimension, whether a mandatory failure blocks resolution entirely, and how conflicting criterion-level findings are handled.

### 5.6 Progression and longitudinal claims

Separate two concepts:

1. **Current-state maturity:** the level supported by the current assessment evidence.
2. **Demonstrated progression:** a longitudinal claim that the organization has moved from a prior state to a higher state.

A forward-only/no-skipping rule, if retained, must be assigned to the appropriate concept. A current-state assessment must not assume an organization's historical path unless prior validated assessment evidence is available.

### 5.7 Effort-adjusted measure

Determine whether the effort multiplier measures implementation effort, organizational complexity, progression difficulty, investment intensity or another construct. These are not interchangeable.

If retained, specify its unit, formula, scale, aggregation point, interpretation and permissible comparisons. It must not be called maturity, capability, realized value or financial return. If no coherent construct and valid use can be established, recommend retiring the measure and assess the impact on existing examples and consumers.

## 6. Model-line separation

The resulting specification must contain two explicit evaluation profiles:

| Profile | Assessment structure | Required rules |
|---|---|---|
| Composite | Four component scores, component weights and mandatory flags | Native score derivation, component-level evidence, weighted aggregation, mandatory resolution and L-1…L-5 resolution |
| Operationalized | Five-anchor criteria, 23 subdimensions, six weighted dimensions, mandatory D1–D4 | Anchor conversion, evidence states, full aggregation chain, coverage/confidence, mandatory gates and L-1…L-5 resolution |

Shared rules may be expressed once only where their semantics are genuinely identical. Differences must be explicit rather than hidden behind a single generic formula.

## 7. Deliverables

| ID | Deliverable | Acceptance evidence |
|---|---|---|
| D-01 | Evaluation semantics decision record | Each decision in §5 is explicit, justified and approved |
| D-02 | Normative scoring specification for both model lines | Formulae, state handling, denominators, precision and examples are complete |
| D-03 | Normative maturity/conformance resolution algorithm | Deterministic decision table or pseudocode, with no undefined inputs |
| D-04 | Evidence and confidence contract | Evidence states, quality dimensions, sufficiency and reporting behavior are testable |
| D-05 | Criterion-level worked assessment | At least one Operationalized end-to-end example traces evidence → anchors → criterion score → subdimension → dimension → overall score → resolved level |
| D-06 | Composite worked assessment | At least one example demonstrates component-level findings, mandatory gates and overall resolution |
| D-07 | Validation suite | Automated tests cover arithmetic, missingness, gates, confidence, band boundaries and deterministic resolution |
| D-08 | Artifact alignment | YAML artifacts, examples, methodology and validator express the same approved rules |
| D-09 | Compatibility and migration assessment | Existing assessment records, examples, consumers and historical comparability are addressed |

## 8. Acceptance criteria

- [ ] The adopted L-1…L-5 capability sequence and L-0 Not Assessed sentinel are preserved.
- [ ] Not Assessed is not treated as Absent or silently assigned a zero capability score.
- [ ] The Composite and Operationalized evaluation contracts are separately specified.
- [ ] Every valid criterion response has a deterministic and documented scoring interpretation.
- [ ] Every assessment state has a defined effect on coverage, confidence, aggregation and resolution.
- [ ] Aggregation denominators, weighting, rounding and band boundaries are normative.
- [ ] Mandatory criteria and dimension gates are executable and have negative as well as positive tests.
- [ ] Highest-conformant-level resolution is deterministic and independently reproducible.
- [ ] Current-state maturity is distinguished from longitudinal progression.
- [ ] Effort-adjusted measure is defined coherently or retired through an explicit decision.
- [ ] Worked examples trace raw criterion evidence through to final result for both model lines.
- [ ] CI validates the normative behavior rather than merely checking YAML shape or example arithmetic.
- [ ] Existing examples and assessment data have a documented compatibility disposition.
- [ ] No change to dimensions, weights, criterion intent or maturity bands is made without explicit impact analysis and approval.

## 9. Out of scope

- Redesigning the six Operationalized dimensions, 23 subdimensions or 70 criteria.
- Reweighting the six dimensions or changing mandatory D1–D4 status without a separately justified decision.
- Reopening the adopted L-1…L-5 numbering or treating L-0 as a maturity level.
- Collapsing Composite and Operationalized into one assessment.
- Redesigning the specialist Autonomous Operations model.
- Declaring illustrative examples to be benchmarks.
- Implementing speculative scoring rules before the decisions in this CR are reviewed and accepted.

## 10. Delivery sequence

1. Inventory all current scoring, scale, evidence and resolution declarations in both model lines.
2. Resolve the decisions in §5 through a decision record, including worked alternatives where semantics are contested.
3. Publish the normative evaluation specification for each model line.
4. Implement machine-readable artifact changes and criterion-level examples in controlled, reviewable increments.
5. Extend local and contract CI to validate the complete assessment calculation and resolution behavior.
6. Assess compatibility, versioning and migration impact before release.

## 11. Governance

This CR authorizes investigation, specification and proposal of the evaluation rules. It does **not** authorize silently changing scores, maturity bands, weights, criteria or historical assessment outcomes.

All normative decisions must be recorded before implementation. Any breaking change must identify affected artifacts, consumers, examples, assessment records, model versions and migration requirements.
