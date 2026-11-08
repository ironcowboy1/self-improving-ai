#!/usr/bin/env python3
"""Generate and isolated-test a tiny pure-Python helper."""
from pathlib import Path
ROOT = Path("/home/opc/self-improving-ai")
LOG = ROOT / "daily_log.md"
candidate = ROOT / "candidate_util.py"
candidate.write_text("def add(a, b):\n    return a + b\nprint(add(2, 2))\n")
with open(LOG, "a") as f:
    f.write("- Code scaffold: wrote candidate_util.py (add function)\n")
print("Code scaffold wrote candidate")
