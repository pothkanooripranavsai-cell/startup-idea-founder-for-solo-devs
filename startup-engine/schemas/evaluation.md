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
| `claims` | list | yes | One entry per required claim, naming the evidence behind it. The script derives all coverage figures from this. See below. |
| `coverage` | map | legacy | The four hand-entered counts. Superseded by `claims`; retained so older evaluations still parse. Where both exist, `claims` governs and the script prints the discrepancy. |
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

### `claims` — and why it replaced hand-entered counts

The run 04 bias audit found that every coverage figure in this project was self-reported. `scripts/score.py` divided two numbers typed in by the same process that benefited from them being high, and printed the result in a way that looked computed. Nothing checked whether the claimed supports existed or were distinct.

Each entry is one line: `<support>: <evidence ids, or -> | <claim text>`.

```yaml
claims:
  - direct: ev_017 | The mechanism produces revenue at solo scale
  - direct: ev_016 | Six solo operators earn disclosed revenue across the family
  - inference: ev_022 | Collection from primary publishers is permissible
  - inference: - | Cash validation cost is zero
  - unknown: - | Whether anyone subscribes before a public archive exists
```

`support` is `direct`, `inference`, or `unknown`. Only `direct` counts toward `fact_coverage`, and only when the cited record is itself classified `FACT`.

**The independence cap.** The script reads `underlying_source` from each cited evidence record and groups claims by it. One underlying source may carry at most `MAX_CLAIMS_PER_SOURCE` claims as direct support; further claims from the same source fall back to inference.

This exists because one article establishing an entire candidate is the failure the independence rule was written to prevent, and it was happening. In `idea_13`, four of seven directly supported claims traced to a single founder interview, and two evidence records cited the same web page under different `underlying_source` labels. Correcting both moved fact coverage from a self-reported 54% to a derived 38%, and the verdict from `DEEP_EXPLORE` to `WATCH`.

The evaluator can still write a claim list generously. It can no longer decide how much any one source is worth.

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
