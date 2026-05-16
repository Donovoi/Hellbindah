#!/usr/bin/env python3
"""Simple evaluator scaffold for Hellbindah agentic development.

The evaluator intentionally starts conservative. It scores candidate evidence files
rather than executing untrusted arbitrary code.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HARD_FAIL_FLAGS = {
    "uses_protected_assets",
    "contains_secrets",
    "broad_unscoped_rewrite",
    "unsafe_binary_blob",
}

WEIGHTS = {
    "build_passed": 20,
    "tests_passed": 20,
    "task_updated": 10,
    "kanban_updated": 10,
    "ip_review_passed": 15,
    "performance_not_regressed": 10,
    "small_reviewable_change": 10,
    "evidence_attached": 5,
}


def evaluate(payload: dict) -> dict:
    flags = set(payload.get("flags", []))
    hard_fails = sorted(flags & HARD_FAIL_FLAGS)
    if hard_fails:
        return {"score": 0, "decision": "reject", "hard_fails": hard_fails}

    score = 0
    details = {}
    for key, weight in WEIGHTS.items():
        value = bool(payload.get(key, False))
        details[key] = {"passed": value, "points": weight if value else 0}
        if value:
            score += weight

    decision = "accept" if score >= 80 else "needs_review" if score >= 60 else "reject"
    return {"score": score, "decision": decision, "details": details, "hard_fails": []}


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: evaluator.py candidate_evidence.json", file=sys.stderr)
        return 2
    payload = json.loads(Path(argv[1]).read_text(encoding="utf-8"))
    result = evaluate(payload)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["decision"] != "reject" else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
