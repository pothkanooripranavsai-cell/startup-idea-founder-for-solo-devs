"""
Computes weighted total, evidence coverage, and verdict for an evaluation.

Usage:
    python scripts/score.py <evaluation.md> [--idea <idea.md>] [--write]

Reads the YAML frontmatter of an evaluation (schemas/evaluation.md), applies
rules/scoring_rubric.md, and prints the result. With --idea, gates 1 and 5 are
recomputed deterministically from the idea and config/founder_constraints.md
and override whatever the evaluator recorded.

The script never invents a score. It aggregates and thresholds what the
evaluator recorded.
"""

from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent

# Mirrors rules/scoring_rubric.md.
# Run 09: product-market fit is the single primary goal, so demand evidence carries the
# most weight and competition the least. See rules/scoring_rubric.md for the reasoning.
WEIGHTS: dict[str, float] = {
    "economic_model": 0.25,
    "demand_evidence": 0.35,
    "contestedness": 0.05,
    "bootstrap_feasibility": 0.15,
    "distribution": 0.10,
    "domain_tacit_fit": 0.10,
}

GATES = [
    "gate_1_validation_capital",
    "gate_2_domain_expertise",
    "gate_3_tacit_network",
    "gate_4_credentials_regulation",
    "gate_5_solo_operability",
    "gate_6_physical_dependency",
    "gate_7_distribution_access",
    "gate_8_self_funding",
]

GATE_STATES = {"PASS", "FAIL", "BLOCKED"}

REJECT_BELOW = 2.5
DEEP_EXPLORE_AT = 3.5
FACT_COVERAGE_MIN = 0.5
UNKNOWN_RATE_MAX = 0.3

# How many claims one underlying source may carry as direct support before the rest
# fall back to inference. Without a cap, one article can establish a whole candidate.
MAX_CLAIMS_PER_SOURCE = 2

# A direct claim counts only if at least one cited record is a FACT from one of these
# tiers. rules/evidence_policy.md already says community sources cannot alone support a
# FACT and promotional sources never solely support viability; until run 08 nothing
# enforced it, and six direct claims across four candidates rested on such records.
QUALIFYING_TIERS = {"primary", "secondary"}


def _scalar(raw: str) -> Any:
    s = raw.strip()
    if s in ("", "null", "~"):
        return None
    if s.lower() in ("true", "false"):
        return s.lower() == "true"
    if s.startswith("[") and s.endswith("]"):
        inner = s[1:-1].strip()
        return [_scalar(p) for p in inner.split(",") if p.strip()] if inner else []
    if len(s) > 1 and s[0] == s[-1] and s[0] in "\"'":
        return s[1:-1]
    try:
        return int(s)
    except ValueError:
        pass
    try:
        return float(s)
    except ValueError:
        pass
    return s


def parse_frontmatter(path: Path) -> dict[str, Any]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError(f"{path}: no YAML frontmatter")
    try:
        end = next(i for i, ln in enumerate(lines[1:], 1) if ln.strip() == "---")
    except StopIteration:
        raise ValueError(f"{path}: unterminated frontmatter")

    data: dict[str, Any] = {}
    parent: str | None = None
    for raw in lines[1:end]:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        line = raw.strip()
        if len(raw) - len(raw.lstrip()) == 0:
            key, _, val = line.partition(":")
            key = key.strip()
            if val.strip() == "":
                data[key] = None
                parent = key
            else:
                data[key] = _scalar(val)
                parent = None
        elif parent is not None:
            if line.startswith("- "):
                if not isinstance(data.get(parent), list):
                    data[parent] = []
                data[parent].append(_scalar(line[2:]))
            else:
                k, _, v = line.partition(":")
                if not isinstance(data.get(parent), dict):
                    data[parent] = {}
                data[parent][k.strip()] = _scalar(v)
    return data


def derive_gate(value: Any, ceiling: Any) -> str:
    if value is None or ceiling is None:
        return "BLOCKED"
    return "PASS" if value <= ceiling else "FAIL"


def derive_banded_gate(value: Any, floor: Any, stretch: Any) -> str:
    """Committed floor passes; the uncommitted band blocks; beyond the stretch fails."""
    if value is None or floor is None:
        return "BLOCKED"
    if value <= floor:
        return "PASS"
    if stretch is not None and value <= stretch:
        return "BLOCKED"
    return "FAIL"


def evidence_index(evidence_dir: Path) -> dict[str, dict[str, str | None]]:
    """Map evidence id -> underlying source, classification and tier, read from the records
    themselves so independence and quality are enforced rather than remembered."""
    out: dict[str, dict[str, str | None]] = {}
    if not evidence_dir.is_dir():
        return out
    wanted = {"id", "underlying_source", "classification", "source_tier"}
    for path in sorted(evidence_dir.glob("ev_*.md")):
        rec: dict[str, str] = {}
        for line in path.read_text(encoding="utf-8").splitlines():
            key, _, value = line.partition(":")
            if key.strip() in wanted:
                rec[key.strip()] = value.strip()
            elif line.strip() == "---" and "id" in rec:
                break
        if "id" in rec:
            out[rec["id"]] = {
                "source": rec.get("underlying_source") or rec["id"],
                "classification": rec.get("classification"),
                "tier": rec.get("source_tier"),
            }
    return out


def parse_claims(raw: list[Any]) -> list[tuple[str, list[str]]]:
    """Each entry is "<support>: <ev ids or -> | <claim text>"."""
    claims = []
    for entry in raw:
        support, _, rest = str(entry).partition(":")
        ids_part = rest.partition("|")[0].strip()
        ids = [i.strip() for i in ids_part.split(",") if i.strip() and i.strip() != "-"]
        claims.append((support.strip().lower(), ids))
    return claims


def coverage_from_claims(
    claims: list[tuple[str, list[str]]], index: dict[str, dict[str, str | None]]
) -> tuple[float, float, dict[str, Any]]:
    """Derive coverage from the claim list.

    Two rules turn a claim written as direct back into inference. It must cite at least one
    record that is a FACT at a qualifying tier, or it is demoted. And each distinct
    underlying source counts toward direct support at most MAX_CLAIMS_PER_SOURCE times,
    because a single article establishing an entire candidate is the failure the
    independence rule exists to prevent.
    """
    required = len(claims)
    unknown = sum(1 for support, _ in claims if support == "unknown")

    used: dict[str, int] = {}
    direct = uncapped = demoted = 0
    for support, ids in claims:
        if support != "direct":
            continue
        uncapped += 1
        qualifying = [
            i for i in ids
            if index.get(i, {}).get("classification") == "FACT"
            and index.get(i, {}).get("tier") in QUALIFYING_TIERS
        ]
        if not qualifying:
            demoted += 1
            continue
        key = sorted({index[i]["source"] for i in qualifying})[0]
        if used.get(key, 0) < MAX_CLAIMS_PER_SOURCE:
            used[key] = used.get(key, 0) + 1
            direct += 1

    detail = {
        "required": required,
        "direct_capped": direct,
        "direct_uncapped": uncapped,
        "unknown": unknown,
        "independent_sources": len(used),
        "demoted": demoted,
        "capped_away": uncapped - demoted - direct,
    }
    return direct / required, unknown / required, detail


def weighted_total(scores: dict[str, Any]) -> float | None:
    """Weighted geometric mean, on the 0-5 scale.

    Deliberately multiplicative rather than additive. A weighted sum lets a strength
    in one dimension average away a fatal weakness in another - a candidate whose
    buyers are unreachable is worth nothing, not 10% less. Under a geometric mean a
    zero in any dimension drives the total to zero, and weak dimensions drag
    proportionally instead of being smoothed over.
    """
    if any(v is None for v in scores.values()):
        return None
    if any(v == 0 for v in scores.values()):
        return 0.0
    log_total = sum(WEIGHTS[d] * math.log(scores[d] / 5.0) for d in WEIGHTS)
    return round(5.0 * math.exp(log_total), 2)


def family_denominator(model_family: Any) -> tuple[Any, str]:
    """Read the attempt denominator for a mechanism family.

    Every source company in this corpus succeeded. Without knowing how many attempted
    the same mechanism, a count of successes is survivor-selected and says little about
    the odds. This surfaces that rather than letting revenue_evidenced_count read as proof.
    """
    if not model_family:
        return None, "no model family recorded"
    path = REPO_ROOT / "data" / "model_families" / f"{model_family}.md"
    if not path.is_file():
        return None, f"family record not found: {model_family}"
    try:
        fm = parse_frontmatter(path)
    except ValueError:
        return None, f"family record unparseable: {model_family}"
    return fm.get("attempt_denominator"), str(fm.get("denominator_basis") or "not stated")


def coverage_figures(cov: dict[str, Any]) -> tuple[float | None, float | None]:
    required = cov.get("required_claims")
    if not required:
        return None, None
    direct = cov.get("directly_supported_claims") or 0
    unknown = cov.get("unknown_claims") or 0
    return direct / required, unknown / required


def decide(
    gates: dict[str, str],
    scores: dict[str, Any],
    total: float | None,
    fact_coverage: float | None,
    unknown_rate: float | None,
    ceiling: Any = None,
) -> tuple[str, str]:
    failed = [g for g, s in gates.items() if s == "FAIL"]
    if failed:
        return "REJECT", f"gate FAIL: {', '.join(failed)}"

    # A zero on any scored dimension means the model cannot work, and that outranks an
    # unresolved gate. BLOCKED routes to WATCH because it represents ignorance, and you
    # should not reject on ignorance - but a scored zero is a judgement, not a gap.
    # Without this, a candidate whose niche is fully served by funded incumbents scores
    # 0.00 and still reads WATCH purely because some other gate is unresolved.
    if total is not None and total == 0.0:
        zeroed = [d for d, v in scores.items() if v == 0]
        return "REJECT", f"dimension scored zero: {', '.join(zeroed)} - the model cannot work"

    blocked = [g for g, s in gates.items() if s == "BLOCKED"]
    if blocked:
        return "WATCH", f"gate BLOCKED: {', '.join(blocked)}"

    unscored = [d for d, v in scores.items() if v is None]
    if unscored:
        return "WATCH", f"unscored dimension: {', '.join(unscored)}"

    assert total is not None
    if total < REJECT_BELOW:
        return "REJECT", f"weighted total {total:.2f} below {REJECT_BELOW}"

    if total >= DEEP_EXPLORE_AT:
        if ceiling is None:
            return "WATCH", "magnitude unstated - no ceiling estimate to judge expected value against"
        if fact_coverage is None or unknown_rate is None:
            return "WATCH", "coverage not computable"
        if fact_coverage < FACT_COVERAGE_MIN:
            return "WATCH", f"fact coverage {fact_coverage:.0%} below {FACT_COVERAGE_MIN:.0%}"
        if unknown_rate > UNKNOWN_RATE_MAX:
            return "WATCH", f"unknown rate {unknown_rate:.0%} above {UNKNOWN_RATE_MAX:.0%}"
        return "DEEP_EXPLORE", f"weighted total {total:.2f}, evidence sufficient"

    return "WATCH", f"weighted total {total:.2f} between {REJECT_BELOW} and {DEEP_EXPLORE_AT}"


def write_back(path: Path, verdict: str, total: float | None) -> None:
    lines = path.read_text(encoding="utf-8").splitlines()
    end = next(i for i, ln in enumerate(lines[1:], 1) if ln.strip() == "---")
    updates = {"verdict": verdict, "weighted_total": "null" if total is None else f"{total:.2f}"}
    for i in range(1, end):
        key = lines[i].partition(":")[0].strip()
        if key in updates:
            lines[i] = f"{key}: {updates.pop(key)}"
    for key, val in updates.items():
        lines.insert(end, f"{key}: {val}")
        end += 1
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    if round(sum(WEIGHTS.values()), 6) != 1.0:
        print(f"error: weights sum to {sum(WEIGHTS.values())}, expected 1.0", file=sys.stderr)
        return 2

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("evaluation", type=Path)
    parser.add_argument("--idea", type=Path, help="recompute gates 1 and 5 deterministically")
    parser.add_argument("--config", type=Path, default=REPO_ROOT / "config" / "founder_constraints.md")
    parser.add_argument("--write", action="store_true", help="write verdict and weighted_total back")
    args = parser.parse_args()

    ev = parse_frontmatter(args.evaluation)

    gates = dict(ev.get("gates") or {})
    missing = [g for g in GATES if g not in gates]
    if missing:
        print(f"error: evaluation missing gates: {', '.join(missing)}", file=sys.stderr)
        return 2
    bad = {g: s for g, s in gates.items() if s not in GATE_STATES}
    if bad:
        print(f"error: invalid gate states: {bad}", file=sys.stderr)
        return 2

    derived: list[str] = []
    if args.idea:
        idea = parse_frontmatter(args.idea)
        cfg = parse_frontmatter(args.config)
        # Gate 5 is deliberately no longer derived. The founder has stated that hours per
        # week and number of founders are not concerns and that time will be adjusted
        # later, so operating load is recorded for information and never blocks. Gate 1
        # remains derived, because the zero-capital starting line is still absolute.
        computed = {
            "gate_1_validation_capital": derive_gate(
                idea.get("cash_validation_cost"), cfg.get("validation_capital_ceiling")
            ),
        }
        gates["gate_5_solo_operability"] = "PASS"
        hours = idea.get("hours_per_week_est")
        if hours is not None:
            derived.append(f"gate_5 informational: operating load estimated at {hours} h/week, not blocking")
        for gate, state in computed.items():
            if state != gates[gate]:
                derived.append(f"{gate}: evaluator said {gates[gate]}, computed {state}")
            gates[gate] = state

    scores = dict(ev.get("scores") or {})
    unknown_dims = [d for d in scores if d not in WEIGHTS]
    if unknown_dims:
        print(f"error: unknown dimensions: {', '.join(unknown_dims)}", file=sys.stderr)
        return 2
    for dim, val in scores.items():
        if val is not None and not (isinstance(val, int) and 0 <= val <= 5):
            print(f"error: {dim} must be an integer 0-5 or null, got {val!r}", file=sys.stderr)
            return 2
    scores = {d: scores.get(d) for d in WEIGHTS}
    total = weighted_total(scores)

    ceiling = idea.get("ceiling_annual_revenue") if idea else None
    denominator, denominator_basis = family_denominator(idea.get("model_family") if idea else None)

    claims = parse_claims(list(ev.get("claims") or []))
    detail = None
    if claims:
        index = evidence_index(args.evaluation.parents[2] / "data" / "evidence")
        fact_coverage, unknown_rate, detail = coverage_from_claims(claims, index)
        self_reported = coverage_figures(dict(ev.get("coverage") or {}))[0]
    else:
        fact_coverage, unknown_rate = coverage_figures(dict(ev.get("coverage") or {}))
        self_reported = None
    verdict, reason = decide(gates, scores, total, fact_coverage, unknown_rate, ceiling)

    print(f"idea:            {ev.get('idea')}")
    print(f"weighted total:  {'n/a' if total is None else f'{total:.2f} / 5.00'}  (geometric)")
    if ceiling is None:
        print("ceiling:         UNSTATED — magnitude is required to judge expected value")
    else:
        print(f"ceiling:         {ceiling:,} / year (estimate)" if isinstance(ceiling, (int, float)) else f"ceiling:         {ceiling}")
    if denominator in (None, "UNKNOWN", "unknown"):
        print(f"survivorship:    attempt denominator UNKNOWN — {denominator_basis}")
        print("                 successes are survivor-selected; this is not a probability")
    else:
        print(f"survivorship:    {denominator} known attempts — {denominator_basis}")
    print(f"fact coverage:   {'n/a' if fact_coverage is None else f'{fact_coverage:.0%}'}")
    print(f"unknown rate:    {'n/a' if unknown_rate is None else f'{unknown_rate:.0%}'}")
    if detail:
        print(
            f"  derived from:  {detail['required']} claims, "
            f"{detail['direct_uncapped']} written as direct, {detail['direct_capped']} counted across "
            f"{detail['independent_sources']} independent sources, {detail['demoted']} demoted "
            f"(no FACT at primary or secondary tier), {detail['capped_away']} capped away"
        )
        if self_reported is not None and abs(self_reported - fact_coverage) > 0.005:
            print(
                f"! self-reported coverage was {self_reported:.0%}, "
                f"derived is {fact_coverage:.0%} — the derived figure governs"
            )
    else:
        print("  coverage:      self-reported (no claims list) — not independence-checked")
    print(f"verdict:         {verdict}")
    print(f"because:         {reason}")
    if ev.get("critical_unknown"):
        print(f"critical unknown: {ev['critical_unknown']}")
    for note in derived:
        print(f"! deterministic override: {note}")

    recorded_verdict, recorded_total = ev.get("verdict"), ev.get("weighted_total")
    if recorded_verdict not in (None, verdict) or (
        isinstance(recorded_total, (int, float)) and total is not None and abs(recorded_total - total) > 0.005
    ):
        print(f"! file recorded {recorded_verdict} / {recorded_total}; computed {verdict} / "
              f"{'n/a' if total is None else f'{total:.2f}'} - the computed values govern")

    if args.write:
        write_back(args.evaluation, verdict, total)
        print(f"\nwrote verdict and weighted_total to {args.evaluation}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
