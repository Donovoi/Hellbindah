#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "tasks" / "tasks.json").read_text(encoding="utf-8"))
tasks = data["tasks"]

lines = []
lines.append("# Hellbindah Kanban Board\n")
lines.append("Source of truth: `tasks/tasks.json`. Regenerate with `python scripts/render_kanban.py`.\n")
lines.append("## Board policy\n")
lines.append("- Todo: approved but not actively being worked.\n")
lines.append("- Doing: active work; max two active tasks per agent unless TL-01 overrides with a note.\n")
lines.append("- Done: acceptance criteria met and reviewed.\n")
lines.append("- PM-01 runs the weekly add/update/split/close/delete review.\n")

for status in ["Doing", "Todo", "Done"]:
    lines.append(f"## {status}\n")
    lines.append("| ID | Task | Assigned | Sprint | Due | SMART measurement | Dependencies |\n")
    lines.append("|---|---|---|---|---|---|---|\n")
    for task in tasks:
        if task["status"] != status:
            continue
        deps = ", ".join(task.get("dependencies", [])) or "None"
        measurement = task.get("measurable", "").replace("|", "/")
        lines.append(f"| {task['id']} | {task['title']} | {task['assigned_to']} | {task['sprint']} | {task['due_date']} | {measurement} | {deps} |\n")
    lines.append("\n")

out = ROOT / "tasks" / "KANBAN.md"
out.write_text("".join(lines), encoding="utf-8")
print(f"Wrote {out}")
