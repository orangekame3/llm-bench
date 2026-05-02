#!/usr/bin/env python3
"""Aggregate evaluation results into a model x agent matrix table."""

import json
import sys
from pathlib import Path


def load_evaluations(eval_dir: Path) -> list[dict]:
    results = []
    for path in eval_dir.rglob("*.json"):
        with open(path) as f:
            data = json.load(f)
        data["_file"] = str(path.relative_to(eval_dir))
        results.append(data)
    return results


def build_matrix(results: list[dict]) -> tuple[list[str], list[str], dict]:
    models: set[str] = set()
    agents: set[str] = set()
    scores: dict[tuple[str, str], list[int]] = {}

    for r in results:
        model = r.get("model", "unknown")
        agent = r.get("agent", "unknown")
        total = r.get("total_score")
        if total is None:
            continue
        models.add(model)
        agents.add(agent)
        scores.setdefault((model, agent), []).append(total)

    return sorted(models), sorted(agents), scores


def print_matrix(models: list[str], agents: list[str], scores: dict):
    if not models or not agents:
        print("No evaluation data found.")
        return

    # Column widths
    model_col = max(len(m) for m in models)
    model_col = max(model_col, len("model"))
    cell_w = max(max((len(a) for a in agents), default=5), 7)

    # Header
    header = f"{'model':<{model_col}}"
    for a in agents:
        header += f"  {a:>{cell_w}}"
    print(header)
    print("-" * len(header))

    # Rows
    for m in models:
        row = f"{m:<{model_col}}"
        for a in agents:
            vals = scores.get((m, a))
            if vals:
                avg = sum(vals) / len(vals)
                cell = f"{avg:.1f}"
            else:
                cell = "-"
            row += f"  {cell:>{cell_w}}"
        print(row)


def print_detail(results: list[dict]):
    if not results:
        return

    print("\n--- Detail ---\n")
    for r in sorted(results, key=lambda x: x.get("_file", "")):
        prompt_id = r.get("prompt_id", "?")
        model = r.get("model", "?")
        agent = r.get("agent", "?")
        total = r.get("total_score", "?")
        print(f"[{prompt_id}] {model} x {agent}: {total}/100")

        categories = r.get("categories", {})
        for cat, info in categories.items():
            score = info.get("score", "?")
            max_score = info.get("max", "?")
            comment = info.get("comment", "")
            print(f"  {cat}: {score}/{max_score}  {comment}")
        print()


def main():
    repo_root = Path(__file__).resolve().parent.parent
    eval_dir = repo_root / "evaluations"

    if not eval_dir.exists():
        print("No evaluations/ directory found.")
        sys.exit(0)

    results = load_evaluations(eval_dir)
    if not results:
        print("No evaluation results found yet.")
        print(f"Add evaluation JSON files to: {eval_dir}/")
        sys.exit(0)

    models, agents, scores = build_matrix(results)
    print_matrix(models, agents, scores)

    if "--detail" in sys.argv:
        print_detail(results)


if __name__ == "__main__":
    main()
