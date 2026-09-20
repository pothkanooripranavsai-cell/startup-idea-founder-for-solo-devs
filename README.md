# Startup Model Research Engine

A file-based system for screening business models against hard founder constraints, using evidence rather than intuition.

It does not try to predict which startup will succeed. It reduces a search space, and it is explicit about what it does not know.

## What it does

Given a set of founder constraints, the engine:

1. Starts from **proven business mechanisms**, not invented ideas.
2. Generates candidate adaptations of those mechanisms.
3. Screens each candidate against **eight hard gates** — pass, fail, or blocked.
4. Scores survivors on **six weighted dimensions**, 0–5.
5. Computes verdicts **deterministically** with a script, not by judgement.
6. Deep-researches only candidates that earn it.

## The parts

| Path | What it holds |
|---|---|
| `startup-engine/README.md` | The charter — purpose, principles, workflow |
| `startup-engine/config/` | Founder constraints: capital, hours, delivery mode |
| `startup-engine/agents/` | Generator and evaluator, as roles rather than running processes |
| `startup-engine/rules/` | Hard gates, scoring rubric, evidence policy, deep-research protocol |
| `startup-engine/schemas/` | Record formats — idea, evaluation, evidence, model family, company, failure, market fact |
| `startup-engine/scripts/score.py` | Deterministic scoring, gate resolution, verdict assignment |
| `startup-engine/data/` | The evidence corpus: sourced records, companies, mechanisms, recorded failures |
| `.claude/commands/` | `/generate` and `/evaluate` slash commands |

`startup-engine/runs/` holds generated candidates and their evaluations. It is intentionally **not published** — the method is public, the findings are not.

## Design decisions worth knowing

**Records are Markdown with YAML frontmatter.** Machine-readable fields for the script, prose for the reasoning. Data is never pasted into prompts; only the records relevant to a candidate are read.

**Four classifications, never blurred.** Every claim is `FACT`, `INFERENCE`, `HYPOTHESIS`, or `UNKNOWN`. Age never changes a classification — an old fact stays a fact and fails a freshness check instead.

**Evidence coverage is several numbers, not one ratio.** Required claims, directly supported, inference-supported and unknown are tracked separately, so a chain of reasoning is never counted as equivalent to a source.

**Independence requires a different underlying source.** Three outlets reproducing one press release count as one, not three.

**Absence of evidence is never positive evidence.** An unanswerable gate returns `BLOCKED`, which routes to research rather than passing quietly.

**The total is a threshold, not a ranking.** Candidates are not ordered by score unless a run explicitly asks for it.

## Running it

```bash
# Generate candidates from a model family
/generate

# Evaluate one candidate
/evaluate startup-engine/runs/generated/idea_01.md

# Score it deterministically
python startup-engine/scripts/score.py \
  startup-engine/runs/screened/idea_01.eval.md \
  --idea startup-engine/runs/generated/idea_01.md --write
```

`score.py` is stdlib-only — no dependencies, including no YAML library. It parses the frontmatter subset the schemas use.

The script never invents a score. It aggregates what the evaluator recorded, applies the weights, and thresholds the result. Where the evaluator's gate state disagrees with what the script can compute from the constraints, the computed value wins and the disagreement is reported.

## Adapting it to your own constraints

Edit `startup-engine/config/founder_constraints.md`. The gates read it directly.

An unset constraint is an unknown, not permission — leaving a value `null` makes the gates that depend on it return `BLOCKED` rather than `PASS`. That is deliberate.
