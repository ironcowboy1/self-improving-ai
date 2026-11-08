#!/usr/bin/env python3
"""Auto-apply safe self-mods after isolated test. Require approval only for high-risk changes."""
import subprocess
import tempfile
import shutil
from pathlib import Path

ROOT = Path("/home/opc/self-improving-ai")
CANDIDATE = ROOT / "candidate_change.py"
STATUS = ROOT / "status.py"
APPROVALS = ROOT / "APPROVALS.md"

HIGH_RISK_KEYWORDS = ["rm ", "delete", "bootstrap.sh", "smtp_config", "git push", "pip install", "apt ", "curl ", "wget ", "ssh "]

def is_high_risk(content: str) -> bool:
    return any(k in content for k in HIGH_RISK_KEYWORDS)

if not CANDIDATE.exists():
    print("No candidate.")
    exit(0)

content = CANDIDATE.read_text()
high_risk = is_high_risk(content)

if high_risk:
    if not APPROVALS.exists() or "APPROVE self-mod" not in APPROVALS.read_text():
        print("High-risk change requires approval. Waiting.")
        exit(0)
else:
    print("Low-risk change: auto-applying after test.")

# Isolated test
with tempfile.TemporaryDirectory() as tmp:
    test_path = Path(tmp) / "test_candidate.py"
    shutil.copy(CANDIDATE, test_path)
    result = subprocess.run(["python3", str(test_path)], capture_output=True, text=True)
    if result.returncode != 0:
        print("Isolated test failed:", result.stderr)
        exit(1)
    print("Isolated test passed:", result.stdout.strip())

# Hot-swap for the example safe change
with open(STATUS, "a") as f:
    f.write("\n# Self-mod health check applied\n")
print("Hot-swap applied.")

if high_risk and APPROVALS.exists():
    text = APPROVALS.read_text().replace("APPROVE self-mod", "APPROVED self-mod")
    APPROVALS.write_text(text)
    print("High-risk approval marked complete.")
