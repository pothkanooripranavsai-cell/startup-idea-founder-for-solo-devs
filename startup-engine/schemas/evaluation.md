# SCHEMA: EVALUATION

Output of `agents/evaluator.md`. One file per evaluated candidate: `runs/screened/idea_NN.eval.md`.

Markdown with YAML frontmatter. `scripts/score.py` reads the frontmatter and recomputes `weighted_total`, the coverage figures, and `verdict`. The evaluator fills in gate states and 0–5 scores; the script does the arithmetic and the thresholding.

## FRONTMATTER

| Field | Type | Required | Description |
|---|---|---|---|
| `idea` | string | yes | `id` of the evaluated idea. |
| `evaluated` | date | yes | Evaluation date. |
| `gates` | map | yes | One entry per gate in `rules/hard_gates.md`, each `PASS`, `FAIL`, or `BLOCKED`. |
| `scores` | map | yes | One entry per dimension in `rules/scoring_rubric.md`, integer `0`–`5` or `null` when unresolved. |
| `coverage` | map | yes | The four counts below. Computed figures are derived from them, never entered by hand. |
| `critical_unknown` | string \| null | yes | The single unknown that most constrains the decision. `null` only when nothing is unresolved. |
| `disconfirming_search` | string | yes | What was searched for that would contradict the candidate, and what came back. Required by evaluator step 7. |
| `verdict` | string | yes | `REJECT`, `WATCH`, or `DEEP_EXPLORE`. Written by `scripts/score.py`. |
| `weighted_total` | number \| null | yes | Written by `scripts/score.py`. `null` when any dimension is unscored. |

### `gates`

```yaml
gates:
  gate_1_validation_capital: PASS
  gate_2_domain_expertise: PASS
  gate_3_tacit_network: BLOCKED
  gate_4_credentials_regulation: PASS
  gate_5_solo_operability: PASS
  gate_6_physical_dependency: PASS
  gate_7_distribution_access: PASS
  gate_8_self_funding: PASS
```

### `scores`

```yaml
scores:
  bootstrap_feasibility: 4
  domain_tacit_fit: null
  solo_feasibility: 4
  transferability: 3
  validation_accessibility: 3
  distribution: 2
```

### `coverage`

Four counted inputs. Inference is tracked separately from direct evidence and is never added to it.

```yaml
coverage:
  required_claims: 12
  directly_supported_claims: 7
  inference_supported_claims: 3
  unknown_claims: 2
```

Derived by the script, not written by hand:

- `fact_coverage` = `directly_supported_claims / required_claims`
- `unknown_rate` = `unknown_claims / required_claims`

A claim supported only by inference counts toward `inference_supported_claims`. It never counts toward `fact_coverage`.

## BODY

Required sections, in order:

1. `## Gates` — one subsection per gate: state, reason, and the evidence ids it rests on. Reasons are required for `PASS` as well as `FAIL` and `BLOCKED`.
2. `## Scores` — one subsection per dimension: the 0–5 anchor chosen, why, and supporting evidence ids.
3. `## Evidence coverage` — what the required claims were, and which are unsupported.
4. `## Disconfirming search` — what was looked for that would contradict the candidate, and what was found.
5. `## Critical unknown` — the one unknown that most constrains the decision, and what would resolve it.

## RULES

A gate is `PASS` only on FACT or firm INFERENCE. Absence of evidence is `BLOCKED`, never `PASS`.

A dimension with no resolved evidence is `null`, never a midpoint guess. Any `null` suppresses `weighted_total`.

The evaluator does not write `verdict` or `weighted_total` by hand. If the script's output disagrees with the evaluator's expectation, the disagreement is the finding.

`weighted_total` orders nothing by itself. It exists to threshold into a verdict, not to rank candidates against each other.
