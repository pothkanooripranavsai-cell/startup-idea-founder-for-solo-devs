---
description: Evaluate a generated candidate following agents/evaluator.md
argument-hint: <path to idea file>
---

Act as the EVALUATOR role. Follow `startup-engine/agents/evaluator.md` exactly.

Evaluate: $ARGUMENTS

Read first:

1. `startup-engine/config/founder_constraints.md`
2. `startup-engine/rules/hard_gates.md`
3. `startup-engine/rules/evidence_policy.md`
4. `startup-engine/rules/scoring_rubric.md`
5. `startup-engine/schemas/evaluation.md`
6. The idea file above, and only the `data/` records it references

Do not load the whole `data/` tree.

Then:

1. Mark all eight gates PASS / FAIL / BLOCKED, with a reason for each — including passes. Gate 1 is a ₹0 cash test with a narrow tooling carve-out; Gate 8 asks whether customer payments fund what comes next.
2. Classify each claim as FACT / INFERENCE / HYPOTHESIS / UNKNOWN. Age does not change a classification; an old FACT stays a FACT and fails freshness instead.
3. Score each rubric dimension 0–5, or `null` where evidence does not resolve it. Never default to a midpoint.
4. Count the four coverage inputs. Do not merge inference into direct support.
5. Search for disconfirming evidence and record what you looked for and what came back.
6. Name the single critical unknown.

Write the evaluation to `startup-engine/runs/screened/<idea_id>.eval.md`, matching `schemas/evaluation.md`.

Leave `verdict` and `weighted_total` for the script. Then run:

```
python startup-engine/scripts/score.py startup-engine/runs/screened/<idea_id>.eval.md --idea <idea path> --write
```

If the script's verdict differs from what you expected, report the disagreement rather than editing the evaluation to match.

Do not rescue a candidate because it sounds attractive. Do not convert an unknown into a favorable assumption.
