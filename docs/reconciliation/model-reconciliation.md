# Digital Transformation Model Reconciliation

**Purpose:** Establish what the repository currently defines, distinguish the two model lines, and identify the discrepancies that must be resolved before the documentation can be treated as a normative explanation.

**Review basis:** Current repository artifacts on the `main` branch at the time this document was prepared. Paths below are the source of truth for the observations; this document does not supersede them.

## 1. Executive finding

The repository hosts two different Digital Transformation model lines:

- **Composite:** a four-component model using imported, extended or overridden reusable components. It is the CR-AM-11 §31 first-model candidate.
- **Operationalized:** a more detailed, enterprise-oriented model line with six dimensions and a declared register of 23 subdimensions and 70 criteria.

They are related by domain and scale correlation, but they are not interchangeable assessments. A 1:1 level correlation does not establish equivalent criteria, evidence, scoring, weighting or assessment results.

The Operationalized model is the appropriate primary narrative for explaining enterprise digital transformation because it explicitly covers customer and ecosystem value, strategy and business model, platforms and technology, operations and service delivery, people and human-agent teaming, and data and intelligence.

## 2. Repository and model identity

| Concern | Current artifact | Observation |
|---|---|---|
| Repository release | `VERSION` | `2.0.0` |
| Contract identity | `model.yaml` | Version `2.0.0`; describes both model lines |
| Repository standard declaration | `standard.yaml` | Model version `2.0.0`; structural conformance to repository standard 1.0.1 |
| Composite model line | `maturity/scale.yaml`, `maturity/evaluation.yaml`, `maturity/components/` | Stable in README; the scale and evaluation artifacts carry version 2.0.0 |
| Operationalized model line | `maturity/operationalized/scale.yaml`, `maturity/operationalized/evaluation.yaml`, `maturity/operationalized/model/`, `maturity/operationalized/components/` | Alpha in model artifacts; scale and evaluation carry version 2.0.0 |
| Cross-line mapping | `mappings/digital-transformation-operationalized.yaml` | Describes the operationalized line as 1.0.0-alpha |
| Operationalized worked example | `examples/operationalized-2026.yaml` | References the operationalized model as 1.0.0-alpha |
| Composite worked example | `examples/enterprise-2026.yaml` | References the composite model as 1.0.0 |

### Finding

The repository-level release, model manifest, standard declaration, scale/evaluation artifact versions, mapping metadata and examples are not yet expressed through one clearly documented versioning convention. This is not necessarily a single incorrect version: they may represent different version scopes. The repository must state which version identifies which governed object and ensure each reference points to the intended release.

**Required decision:** define version authority and compatibility rules for repository release, model line, scale, evaluation, components and assessment examples.

## 3. The two model lines

### 3.1 Composite model

Source artifacts:

- `maturity/scale.yaml`
- `maturity/evaluation.yaml`
- `maturity/components/`
- `examples/enterprise-2026.yaml`

The composite evaluation aggregates four component criteria:

| Component | Weight | Mandatory |
|---|---:|---|
| Digital culture | 20% | Yes |
| Technology adoption | 30% | Yes |
| Operations modernization | 25% | No |
| Services delivery | 25% | No |
| **Total** | **100%** | |

The component model is intentionally compact and uses the component reuse model established by the repository. Its current framing is more technology/operating-practice oriented than the Operationalized model.

### 3.2 Operationalized model

Source artifacts:

- `maturity/operationalized/scale.yaml`
- `maturity/operationalized/evaluation.yaml`
- `maturity/operationalized/model/`
- `maturity/operationalized/components/`
- `examples/operationalized-2026.yaml`

The evaluation declares six dimensions:

| ID | Dimension | Weight | Mandatory |
|---|---|---:|---|
| D1 | Customer & Ecosystem Value | 20% | Yes |
| D2 | Strategy, Business Model & Value | 20% | Yes |
| D3 | Digital Platforms & Technology Enablement | 20% | Yes |
| D4 | Operations & Autonomous Service Delivery | 15% | Yes |
| D5 | People, Culture & Human-Agent Teaming | 10% | No |
| D6 | Data & the Intelligent Enterprise | 15% | No |
| | **Total** | **100%** | |

The repository README declares 23 subdimensions and 70 criteria in the operationalized register. Those counts should be verified automatically against the actual register as part of the model validation pipeline.

## 4. Scale and evaluation reconciliation

### 4.1 L-0 is a sentinel, not a maturity level

Both scale artifacts define L-0 Not Assessed as a state in which no evidence has been examined. They explicitly say it is not a capability maturity level.

The five capability maturity levels are L-1 through L-5. Documentation must not count L-0 as one of the five maturity levels.

### 4.2 Composite model inconsistency

The composite scale defines L-0 through L-5, with L-0 as Not Assessed and L-1 through L-5 as capability levels. Its evaluation model's narrative and aggregation comments refer in places to resolution to L-0…L-4, while its criterion expectations include L-1 through L-5.

The composite worked example also contains comments describing L-0…L-4 and refers to an L-4 ordinal that does not match the declared five-level sequence.

**Required decision:** confirm the intended five-level scale, map score bands to L-1…L-5, and correct stale comments and ordinal descriptions. Do not change level IDs or score semantics by inference.

### 4.3 Operationalized model inconsistency

The operationalized scale defines L-0 Not Assessed and five capability levels L-1…L-5. Its evaluation description, however, says the result is resolved to L-0…L-4. The evaluation dimension expectations include L-1…L-5, and the scale includes five score bands:

| Level | Value alias | Score band |
|---|---|---:|
| L-1 | Unrealized | 0–20 |
| L-2 | Proven | 21–45 |
| L-3 | Standardized | 46–70 |
| L-4 | Compounding | 71–88 |
| L-5 | Leading | 89–100 |

**Required decision:** confirm that the five score bands resolve to L-1…L-5, with L-0 reserved for Not Assessed, and update the evaluation's resolution description and any dependent resolver logic accordingly.

### 4.4 Band boundaries and unassessed responses

The scale declares score ranges with integer boundaries. The methodology must define how fractional scores are treated, whether rounding occurs before band assignment, and how a criterion with no evidence differs from a genuine zero score.

These distinctions matter because Not Assessed is explicitly not a maturity level and must not be treated as proof of absent capability.

## 5. Scoring reconciliation

The Operationalized evaluation states:

- Criterion ratings are converted from 1–5 to 0–100.
- Subdimension score is the mean of criterion scores.
- Dimension score is the mean of subdimension scores.
- Overall score is the weighted sum of dimension scores.
- D1–D4 are mandatory; D5–D6 are optional.

The repository does not yet provide a complete, unambiguous normative definition of the 1–5 to 0–100 conversion, missing-data treatment, rounding, confidence adjustment and exact highest-conformant-level algorithm in the same assessment contract.

The worked example supplies dimension scores directly, so it does not prove the criterion-to-subdimension calculation.

**Required decision:** specify the full calculation chain and provide a testable example at criterion level.

## 6. Effort-adjusted value

Both scale artifacts declare effort multipliers for L-1 through L-5 (1.0, 1.5, 2.5, 4.0 and 6.0). The examples multiply the aggregated score by the resolved-level multiplier.

For example, the Operationalized example reports:

- Dimension scores: D1 72, D2 64, D3 58, D4 70, D5 80, D6 66.
- Weights: 0.20, 0.20, 0.20, 0.15, 0.10, 0.15.
- Weighted score: 67.2.
- Resolved band: Systematic.
- Resolved level: L-3.
- Effort multiplier: 2.5.
- Effort-adjusted value: 168.0.

The arithmetic is consistent with 67.2 × 2.5 = 168.0. The semantic interpretation is not sufficiently defined. The result exceeds the 0–100 score domain and should not be labelled as realized enterprise value, financial value or a normalized maturity score without an explicit definition.

**Required decision:** define the construct, units, intended use and reporting label, or retire it through a separate model change.

## 7. Model boundary: broad transformation and specialist autonomy

The Operationalized D4 dimension explicitly includes Operations & Autonomous Service Delivery. The maturity scale also references closed-loop operations, AI agents and digital twins.

This is appropriate as enterprise-level coverage: the model should establish whether autonomous operations are strategically relevant, governed, adopted and contributing to enterprise outcomes.

It should not duplicate the specialist Autonomous Operations maturity model's detailed assessment of operational autonomy, closed-loop control, autonomy levels, assurance and operational execution.

Recommended boundary:

- **Digital Transformation model:** assesses enterprise intent, adoption, governance, value contribution and integration of autonomous capabilities.
- **Autonomous Operations model:** assesses the depth, breadth, control integrity and operational performance of autonomous execution.

The README should make this distinction explicit.

## 8. Worked example interpretation

The Operationalized example is useful as a calculation illustration, but it is not a benchmark and does not include criterion-level evidence. It demonstrates weighted aggregation over six dimension scores and a resulting L-3 resolution.

Documentation must label it **illustrative** and distinguish:

1. A model example used to explain mechanics.
2. An actual organizational assessment supported by evidence.
3. A benchmark result based on a governed, immutable cohort and baseline.

These are different evidence classes and must not be conflated.

## 9. Reconciliation register

| ID | Finding | Severity | Required disposition |
|---|---|---|---|
| REC-01 | L-0…L-4 resolution text conflicts with L-1…L-5 capability levels | Critical | Align scale, evaluation, examples and resolver |
| REC-02 | Repository/model-line version authority is ambiguous | High | Define version scope and reference rules |
| REC-03 | Criterion 1–5 to 0–100 conversion is underspecified | Critical | Specify formula and missing-data rules |
| REC-04 | Effort-adjusted value lacks clear semantics and units | High | Define or remove through a model CR |
| REC-05 | Composite worked-example comments contain stale level/ordinal descriptions | High | Correct after REC-01 |
| REC-06 | Operationalized example bypasses criterion-level calculation | Medium | Add full traceable worked example |
| REC-07 | Evidence confidence and incomplete-evidence treatment need explicit methodology | High | Define evidence and confidence contract |
| REC-08 | Register counts need automated verification | Medium | Add CI count/reference checks |
| REC-09 | Broad autonomy coverage needs explicit boundary with Autonomous Operations model | Medium | Document cross-model specialization |

## 10. Safe documentation claims

Until the reconciliation items are resolved, documentation may safely state that:

- The repository contains two distinct Digital Transformation model lines.
- The Operationalized line defines six weighted dimensions and declares a 23-subdimension/70-criterion register.
- Both scale artifacts define L-0 as Not Assessed and L-1 through L-5 as capability levels.
- The Operationalized example reports a weighted score of 67.2 and L-3 resolution.
- The example is illustrative and does not establish a benchmark.
- The model covers autonomous operations at an enterprise transformation level; specialist operational autonomy is assessed in the Autonomous Operations model.

Documentation must not claim that all scoring semantics, level resolution and version references are fully reconciled until the relevant model changes are approved and validated.
