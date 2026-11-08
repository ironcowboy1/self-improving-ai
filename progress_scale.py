#!/usr/bin/env python3
"""Generate human-scale progress statement for the daily email."""
import json
from pathlib import Path

ROOT = Path("/home/opc/self-improving-ai")
STATE = ROOT / "math_state.json"
LOG = ROOT / "daily_log.md"

def scale():
    if not STATE.exists():
        return "No math progress yet (still at 2+2)."
    s = json.loads(STATE.read_text())
    level = s.get("level", 1)
    correct = s.get("correct", 0)
    total = s.get("total", 0)
    if level == 1:
        desc = f"learned {correct} basic addition facts (grade-school level)"
    elif level == 2:
        desc = f"mastered multiplication tables (middle-school level)"
    elif level == 3:
        desc = f"advanced to exponents (early high-school)"
    else:
        desc = f"reached level {level} (high-school algebra range)"
    return f"Math progress: {desc}. Total problems solved: {total}."

line = "- " + scale() + "\n"
with open(LOG, "a") as f:
    f.write(line)
print(line.strip())
