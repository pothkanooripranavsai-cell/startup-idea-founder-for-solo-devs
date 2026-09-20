---
description: Generate business-model adaptations following agents/generator.md
argument-hint: "[model family id, or blank to choose]"
---

Act as the GENERATOR role. Follow `startup-engine/agents/generator.md` exactly.

Read first, and read only what you need:

1. `startup-engine/config/founder_constraints.md`
2. `startup-engine/rules/hard_gates.md`
3. `startup-engine/schemas/idea.md`
4. The relevant record in `startup-engine/data/model_families/` — $ARGUMENTS if given, otherwise pick one and say why
5. Only the `startup-engine/data/companies/` records that model family references

Do not load the whole `data/` tree. Load the records relevant to this candidate and no more.

Then generate candidate adaptations for the target market. For each one:

- identify the underlying economic mechanism
- identify what makes the original work
- identify what is different in the target market
- design a meaningful adaptation, not a clone of any company's product
- record assumptions and unknowns honestly

Write each candidate to `startup-engine/runs/generated/idea_NN.md`, matching `schemas/idea.md` exactly, including the YAML frontmatter.

The founder has **₹0** validation capital. Only general-purpose AI and software subscriptions are carved out, and that carve-out is not a budget — see `config/founder_constraints.md`. Do not generate candidates that need advertising, inventory, infrastructure, deposits, paid help, or per-customer costs.

Set `cash_validation_cost_inr` to `0` only when you genuinely believe no money leaves before a customer pays, and name every cost you considered in `cash_validation_cost_basis`. Leave it `null` if you do not know. An honest null becomes a BLOCKED gate downstream, which is the intended behavior. A fabricated zero is not.

Every candidate must also state in `revenue_before_cost` how customer payment precedes and funds the next increment of cost. A candidate that cannot answer this fails Gate 8.

Do not evaluate, score, or rank what you generate.
