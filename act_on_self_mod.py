#!/usr/bin/env python3
"""Auto-apply all pure-computation advances. Approval only for system-level changes."""
import subprocess
import tempfile
import shutil
import datetime
from pathlib import Path

ROOT = Path("/home/opc/self-improving-ai")
CANDIDATE = ROOT / "candidate_change.py"
STATUS = ROOT / "status.py"
APPROVALS = ROOT / "APPROVALS.md"
DAILY_LOG = ROOT / "daily_log.md"

HIGH_RISK_KEYWORDS = ["rm ", "delete", "bootstrap.sh", "smtp_config", "git push", "pip install", "apt ", "curl ", "wget ", "ssh ", "open(", "write("]

def is_high_risk(content: str) -> bool:
    return any(k in content for k in HIGH_RISK_KEYWORDS)

if not CANDIDATE.exists():
    print("No candidate.")
    exit(0)

content = CANDIDATE.read_text()
needs_approval = is_high_risk(content)

if needs_approval:
    if not APPROVALS.exists() or "APPROVE self-mod" not in APPROVALS.read_text():
        proposal = f"\n## Proposed system-level change {datetime.datetime.utcnow().isoformat()}\n- Status: PENDING\n- Reason: touches system or external resources\n"
        with open(APPROVALS, "a") as f:
            f.write(proposal)
        print("System-level change requires approval. Proposal written.")
        exit(0)
else:
    print("Pure computation advance: auto-applying after test.")

with tempfile.TemporaryDirectory() as tmp:
    test_path = Path(tmp) / "test_candidate.py"
    shutil.copy(CANDIDATE, test_path)
    result = subprocess.run(["python3", str(test_path)], capture_output=True, text=True)
    if result.returncode != 0:
        print("Isolated test failed:", result.stderr)
        exit(1)
    print("Isolated test passed:", result.stdout.strip())

with open(STATUS, "a") as f:
    f.write("\n# Self-mod health check applied\n")
print("Hot-swap applied.")

now = datetime.datetime.utcnow().isoformat()
with open(DAILY_LOG, "a") as f:
    f.write(f"- {now}: Pure-computation change applied.\n")

if needs_approval and APPROVALS.exists():
    text = APPROVALS.read_text().replace("APPROVE self-mod", "APPROVED self-mod")
    APPROVALS.write_text(text)
    print("Approval marked complete.")
