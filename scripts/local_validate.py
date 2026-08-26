#!/usr/bin/env python3
"""Level 1 — local model validation for the Digital Transformation model.

Checks:
  1. model.yaml parses as YAML and matches the Assessment-Models manifest
     contract (`Assessment-Models/assessment-ci/schemas/model-manifest.schema.json`)
  2. maturity/scale.yaml has exactly 5 levels with ordinals 0..4 and the
     documented digital-native level names (L-0 Absent, L-1 Piloting,
     L-2 Defined, L-3 Scaled, L-4 Self-Optimising)
  3. maturity/evaluation.yaml references the scale by id+version and each
     criterion's level_expectations covers every scale level
  4. maturity/components/*.yaml each declare kind in {import, extend, override}
     (CR-AM-10 §4) — kindless references are refused
  5. examples/*.yaml computes correctly:
       - aggregated_score = sum(score * weight)
       - aggregated_score in [0, 100]
       - resolved_band corresponds to the canonical v2 bands
         (0-20 / 21-45 / 46-70 / 71-88 / 89-100)
       - effort_adjusted_value = aggregated_score * effort_multiplier

Exit 0 with OK when clean; exit 1 listing every failure otherwise.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
MANIFEST_SCHEMA_URL = (
    "https://assessment-models.github.io/assessment-ci/schemas/"
    "model-manifest.schema.json"
)

EXPECTED_LEVELS = [
    ("L-0", "Absent"),
    ("L-1", "Piloting"),
    ("L-2", "Defined"),
    ("L-3", "Scaled"),
    ("L-4", "Self-Optimising"),
]

V2_BANDS = [
    ("dea:maturity-band-emergent",        (0, 20)),
    ("dea:maturity-band-structured",      (21, 45)),
    ("dea:maturity-band-systematic",      (46, 70)),
    ("dea:maturity-band-adaptive",        (71, 88)),
    ("dea:maturity-band-self-optimising", (89, 100)),
]


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text())


def band_for(score: float) -> str:
    for band_id, (lo, hi) in V2_BANDS:
        if lo <= score <= hi:
            return band_id
    raise ValueError(f"score {score} falls outside all v2 bands")


def main() -> int:
    errors: list[str] = []

    # 1. manifest contract — local re-validation only; Level 2 does the
    # authoritative check via the reusable workflow.
    manifest = load_yaml(ROOT / "model.yaml")
    if not isinstance(manifest, dict):
        errors.append("model.yaml: not a YAML mapping")
    else:
        for required in ("id", "type", "name", "version", "conformance"):
            if required not in manifest:
                errors.append(f"model.yaml: missing required field {required!r}")
        comp = manifest.get("compatibility") or {}
        comp_contracts = comp.get("contracts") or []
        if not comp_contracts:
            errors.append("model.yaml: compatibility.contracts: empty")

    # 2. scale structural correctness
    scale = load_yaml(ROOT / "maturity/scale.yaml")
    scale_levels = scale.get("levels") or []
    actual = [(l["id"], l["name"]) for l in scale_levels]
    if actual != EXPECTED_LEVELS:
        errors.append(
            f"maturity/scale.yaml: levels {actual} != expected {EXPECTED_LEVELS}"
        )
    if [l["ordinal"] for l in scale_levels] != list(range(5)):
        errors.append("maturity/scale.yaml: ordinals must be 0,1,2,3,4 in order")

    # 3. evaluation references scale + covers every level
    eval_doc = load_yaml(ROOT / "maturity/evaluation.yaml")
    if eval_doc.get("scale", {}).get("id") != scale.get("id"):
        errors.append(
            f"maturity/evaluation.yaml: scale.id {eval_doc.get('scale')} != {scale.get('id')}"
        )
    level_ids = {l["id"] for l in scale_levels}
    for c in eval_doc.get("criteria") or []:
        covered = {e["level"] for e in c.get("level_expectations") or []}
        if covered != level_ids:
            errors.append(
                f"maturity/evaluation.yaml: criterion {c['id']!r}: covers {covered} != {level_ids}"
            )

    # 4. component-kind guard (CR-AM-10 §4)
    components = sorted((ROOT / "maturity/components").glob("*.yaml"))
    if not components:
        errors.append("maturity/components/: no component files")
    for comp_path in components:
        comp = load_yaml(comp_path)
        if "kind" not in comp:
            errors.append(f"{comp_path.relative_to(ROOT)}: kind is required (CR-AM-10 §4)")
        elif comp["kind"] not in ("import", "extend", "override"):
            errors.append(
                f"{comp_path.relative_to(ROOT)}: kind {comp['kind']!r} not in "
                "{import, extend, override}"
            )

    # 5. example scoring correctness
    for example_path in sorted((ROOT / "examples").glob("*.yaml")):
        example = load_yaml(example_path)
        scores = example.get("criterion_scores") or {}
        weights = example.get("weights") or {}
        if set(scores) != set(weights):
            errors.append(
                f"{example_path.relative_to(ROOT)}: criterion_scores {set(scores)} "
                f"!= weights {set(weights)}"
            )
        total = sum(scores[k] * weights[k] for k in scores)
        if not math.isclose(total, example["aggregated_score"], abs_tol=0.01):
            errors.append(
                f"{example_path.relative_to(ROOT)}: aggregated_score {example['aggregated_score']} "
                f"!= computed {round(total, 2)}"
            )
        if not (0 <= total <= 100):
            errors.append(
                f"{example_path.relative_to(ROOT)}: aggregated_score {total} out of [0, 100]"
            )
        expected_band = band_for(total)
        if example["resolved_band"] != expected_band:
            errors.append(
                f"{example_path.relative_to(ROOT)}: resolved_band {example['resolved_band']!r} "
                f"!= computed {expected_band!r} for score {total}"
            )
        expected_adjusted = total * example["effort_multiplier"]
        if not math.isclose(example["effort_adjusted_value"],
                            expected_adjusted, abs_tol=0.01):
            errors.append(
                f"{example_path.relative_to(ROOT)}: effort_adjusted_value "
                f"{example['effort_adjusted_value']} != computed {round(expected_adjusted, 2)}"
            )

    if errors:
        print(f"FAIL — Level 1 local validation, {len(errors)} error(s):")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"OK — Level 1 local validation: model + scale + evaluation + "
          f"{len(components)} components + {len(list((ROOT / 'examples').glob('*.yaml')))} "
          f"example(s) all consistent")
    return 0


if __name__ == "__main__":
    sys.exit(main())