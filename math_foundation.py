#!/usr/bin/env python3
"""Progressive math self-test. Starts simple, advances on success."""
import random
import json
from pathlib import Path

ROOT = Path("/home/opc/self-improving-ai")
STATE = ROOT / "math_state.json"
LOG = ROOT / "daily_log.md"

def load_state():
    if STATE.exists():
        return json.loads(STATE.read_text())
    return {"level": 1, "correct": 0, "total": 0}

def save_state(s):
    STATE.write_text(json.dumps(s))

def generate_problem(level):
    if level == 1:
        a, b = random.randint(1, 20), random.randint(1, 20)
        return f"{a} + {b}", a + b
    elif level == 2:
        a, b = random.randint(2, 12), random.randint(2, 12)
        return f"{a} * {b}", a * b
    else:
        a, b = random.randint(1, 10), random.randint(1, 5)
        return f"{a}**{b}", a ** b

def main():
    s = load_state()
    expr, ans = generate_problem(s["level"])
    try:
        result = eval(expr)
        correct = result == ans
    except Exception:
        correct = False
    s["total"] += 1
    if correct:
        s["correct"] += 1
        if s["correct"] >= 5 and s["level"] < 5:
            s["level"] += 1
            s["correct"] = 0
    save_state(s)
    line = f"- Math level {s[level]}: {expr} = {ans} ({OK if correct else FAIL}) correct={s[correct]}/{s[total]}\n"
    with open(LOG, "a") as f:
        f.write(line)
    print(line.strip())

if __name__ == "__main__":
    main()
