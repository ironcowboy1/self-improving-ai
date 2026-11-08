#!/usr/bin/env python3
"""Check APPROVALS.md for APPROVE self-mod, test candidate in isolation, hot-swap only on success."""
import subprocess
import tempfile
import shutil
from pathlib import Path

ROOT = Path("/home/opc/self-improving-ai")
APPROVALS = ROOT / "APPROVALS.md"
CANDIDATE = ROOT / "candidate_change.py"
STATUS = ROOT / "status.py"

if not APPROVALS.exists() or "APPROVE self-mod" not in APPROVALS.read_text():
    print("No approval found. Waiting.")
    exit(0)

if not CANDIDATE.exists():
    print("No candidate file.")
    exit(0)

# Isolated test
with tempfile.TemporaryDirectory() as tmp:
    test_path = Path(tmp) / "test_candidate.py"
    shutil.copy(CANDIDATE, test_path)
    result = subprocess.run(["python3", str(test_path)], capture_output=True, text=True)
    if result.returncode != 0:
        print("Isolated test failed:", result.stderr)
        exit(1)
    print("Isolated test passed:", result.stdout.strip())

# Hot-swap: append a comment line to status.py as the example change
with open(STATUS, "a") as f:
    f.write("\n# Self-mod health check applied\n")
print("Hot-swap applied to status.py")

# Clear the approval line so it does not re-fire
text = APPROVALS.read_text().replace("APPROVE self-mod", "APPROVED self-mod")
APPROVALS.write_text(text)
print("Approval marked complete.")
