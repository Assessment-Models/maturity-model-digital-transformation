# Digital Transformation Model — Persona Guide

This guide helps readers approach the model through the decisions they are responsible for. It is a navigation aid, not a substitute for the assessment criteria or methodology.

## 1. Start with the question you need to answer

| Persona | Primary question | Most useful model view | Expected output |
|---|---|---|---|
| Board member / executive | Is transformation changing enterprise value, resilience and strategic position? | Executive synthesis across all six dimensions | Strategic exposure, outcomes, investment choices and progress |
| Chief Digital / Transformation Officer | Where is transformation progressing, blocked or failing to realize value? | Operationalized six-dimension model and improvement cycle | Transformation portfolio, dependencies, accountable outcomes |
| Enterprise architect | Are strategy, business capabilities, information, platforms and operating model coherently aligned? | D2, D3, D4 and D6, with cross-dimension dependencies | Target-state gaps, architecture decisions and transition roadmap |
| Business / product leader | Are customer, partner and business-model outcomes improving? | D1 and D2 | Journey, ecosystem, proposition and value-realization priorities |
| Operations leader | Are services and operations more reliable, efficient, adaptive and measurable? | D4, supported by D3 and D6 | Operating capability gaps and specialist assessment referrals |
| Technology leader | Do platforms and technology enable the intended operating and business model? | D3, connected to D2, D4 and D6 | Platform, security, resilience and modernization priorities |
| Data / AI leader | Is trusted data and decision intelligence enabling better decisions and action? | D6, connected to D1–D4 | Data product, governance, AI readiness and intelligence roadmap |
| People / HR / change leader | Are leadership, workforce, culture and human-agent work practices ready? | D5, connected to all dimensions | Skills, organizational design, adoption and trust interventions |
| Assessment practitioner | Are findings evidence-based, reproducible and correctly resolved? | Criteria register, evaluation, scale and methodology | Traceable scorecard, confidence record and assessment report |
| Model maintainer / contributor | Is the model coherent, versioned, testable and interoperable? | Machine-readable artifacts, reconciliation and conformance | Reviewed model changes, validation and release evidence |

## 2. Executive and board pathway

Read:

1. [README overview](../../README.md)
2. Six-dimension scorecard and maturity scale in the README.
3. [Assessment methodology](../methodology/assessment-methodology.md), especially interpretation and outputs.

Ask:

- Which customer, ecosystem and enterprise outcomes are improving?
- Is the strategy changing the business model, or only modernizing technology?
- Are benefits evidenced in operational performance and value realization?
- Which capability constraints threaten the strategy?
- What decisions or investments are required now?

Do not treat a single maturity level as a proxy for realized financial value.

## 3. Transformation leader pathway

Read the six-dimension model, then the full [Assessment Methodology](../methodology/assessment-methodology.md).

Use the model to connect strategic intent to an evidence-backed improvement portfolio. Ensure that current capability, future readiness, performance and realized value are discussed distinctly.

Expected outputs include a baseline, target outcomes, prioritized initiatives, dependencies, owners and reassessment cadence.

## 4. Architecture, technology and data pathway

Start with D2 Strategy, Business Model & Value, D3 Digital Platforms & Technology Enablement, D4 Operations & Autonomous Service Delivery, and D6 Data & the Intelligent Enterprise.

Trace each technology or architecture investment to:

- A strategic or customer outcome.
- A business or operational capability.
- Information and data dependencies.
- Security, privacy, resilience and trust requirements.
- Measures of adoption, performance and value.

Technology adoption is evidence of an enabler being deployed; it is not, by itself, evidence that transformation outcomes have been realized.

## 5. Business, product and customer pathway

Start with D1 Customer & Ecosystem Value and D2 Strategy, Business Model & Value.

Examine the customer and partner journeys, proposition changes, ecosystem relationships, monetization logic and measures of value. Check whether changes are repeatable and supported by operating capabilities, data and platforms.

## 6. Operations pathway

Start with D4 Operations & Autonomous Service Delivery, supported by D3 and D6.

The Digital Transformation model should show whether operational modernization and autonomous capabilities are part of the enterprise transformation agenda and whether they contribute to outcomes.

When detailed operational autonomy is the question, continue to the specialist [Autonomous Operations Maturity Model](https://github.com/Assessment-Models/maturity-model-autonomous-operations). Do not use the Digital Transformation D4 score as a substitute for that specialist assessment.

## 7. People and change pathway

Start with D5 People, Culture & Human-Agent Teaming.

Look beyond training completion. Assess leadership behavior, workforce capability, organizational design, decision rights, incentives, adoption, inclusion, trust and how responsibilities are allocated between people and AI agents.

## 8. Assessor pathway

Use this sequence:

1. Confirm model line, scope, period and intended use.
2. Read the authoritative scale and evaluation artifacts.
3. Inspect the criterion register and evidence requirements.
4. Record criterion ratings with source evidence and rationale.
5. Validate findings with accountable owners.
6. Apply only the approved scoring and resolution rules.
7. Record missing evidence and confidence limitations.
8. Produce the complete assessment output described in the methodology.

Do not invent a rating conversion or treat an unassessed criterion as proof of absence. Consult the [Model Reconciliation](../reconciliation/model-reconciliation.md) for unresolved rules.

## 9. Model maintainer pathway

Treat YAML model artifacts as the authoritative machine-readable definition. Keep documentation claims traceable to those artifacts. Changes to scale semantics, scoring, weights, criteria, mandatory gates, benchmarks or version authority require explicit model governance and validation; they must not be introduced through a README edit.

Review [CR-DT-01](../../change-requests/CR-DT-01.md) and [Model Reconciliation](../reconciliation/model-reconciliation.md) before changing the documentation or model contract.
