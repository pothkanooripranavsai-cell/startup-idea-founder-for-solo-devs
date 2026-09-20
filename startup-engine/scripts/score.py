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
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent

# Mirrors rules/scoring_rubric.md.
WEIGHTS: dict[str, float] = {
    "bootstrap_feasibility": 0.25,
    "domain_tacit_fit": 0.25,
    "solo_feasibility": 0.15,
    "solo_transfer": 0.15,
    "validation_accessibility": 0.10,
    "distribution": 0.10,
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
) -> tuple[str, str]:
    failed = [g for g, s in gates.items() if s == "FAIL"]
    if failed:
        return "REJECT", f"gate FAIL: {', '.join(failed)}"

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
        computed = {
            "gate_1_validation_capital": derive_gate(
                idea.get("cash_validation_cost"), cfg.get("validation_capital_ceiling")
            ),
            "gate_5_solo_operability": derive_banded_gate(
                idea.get("hours_per_week_est"), cfg.get("hours_per_week"), cfg.get("hours_per_week_stretch")
            ),
        }
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

    total = None
    if all(v is not None for v in scores.values()):
        total = round(sum(WEIGHTS[d] * scores[d] for d in WEIGHTS), 2)

    fact_coverage, unknown_rate = coverage_figures(dict(ev.get("coverage") or {}))
    verdict, reason = decide(gates, scores, total, fact_coverage, unknown_rate)

    print(f"idea:            {ev.get('idea')}")
    print(f"weighted total:  {'n/a' if total is None else f'{total:.2f} / 5.00'}")
    print(f"fact coverage:   {'n/a' if fact_coverage is None else f'{fact_coverage:.0%}'}")
    print(f"unknown rate:    {'n/a' if unknown_rate is None else f'{unknown_rate:.0%}'}")
    print(f"verdict:         {verdict}")
    print(f"because:         {reason}")
    if ev.get("critical_unknown"):
        print(f"critical unknown: {ev['critical_unknown']}")
    for note in derived:
        print(f"! deterministic override: {note}")

    if args.write:
        write_back(args.evaluation, verdict, total)
        print(f"\nwrote verdict and weighted_total to {args.evaluation}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
