# Startup Model Research Engine

## PURPOSE

Find existing, proven business models that can potentially be adapted to India and operated by a low-capital, low-domain-expertise solo founder.

The system is NOT trying to predict the next successful startup.

It is trying to reduce the search space using evidence, hard constraints, and explicit uncertainty.

## CORE PRINCIPLES

1. Start from proven business models, not arbitrary startup ideas.
2. Separate business MODEL from individual COMPANY.
3. Interest is not a required filter.
4. Value is treated as partially validated by the existence of a proven model, but local economic viability must still be tested.
5. Never treat missing information as positive evidence.
6. Clearly separate FACT, INFERENCE, HYPOTHESIS, and UNKNOWN.
7. Distinguish capital required for validation from capital raised for later scaling.
8. Give special attention to tacit domain expertise and network requirements.
9. Generator creates hypotheses.
10. Evaluator investigates hypotheses.
11. Deterministic scripts calculate scores where possible.
12. Deep research is reserved for survivors of the initial screening process.

## WORKFLOW

1. Read config/founder_constraints.md
2. Read the relevant rules.
3. Read relevant model-family/company/failure/market data.
4. Generate candidate adaptations.
5. Apply hard gates.
6. Evaluate surviving candidates using evidence.
7. Calculate scores using scripts.
8. Deep-research only the strongest candidates.
9. Save structured outputs.

## FILE STRUCTURE

agents/
rules/
schemas/
data/
runs/
scripts/

## IMPORTANT

Do not invent evidence.

Do not use the model's intuition as a substitute for missing evidence.

Do not optimize for impressive-sounding ideas.

Do not rank candidates unless the evaluation procedure explicitly requires it.

When information is uncertain, record the uncertainty.

Before making major architectural changes, inspect the existing files and preserve the separation between rules, data, agents, and calculations.
