#!/usr/bin/env python3
"""Propose a sandboxed self-modification. Writes proposal to APPROVALS.md and a candidate file."""
import datetime
from pathlib import Path

ROOT = Path("/home/opc/self-improving-ai")
APPROVALS = ROOT / "APPROVALS.md"
CANDIDATE = ROOT / "candidate_change.py"

proposal = f"""
## Proposed self-mod {datetime.datetime.utcnow().isoformat()}
- Action: Add a simple health-check print to status.py
- Candidate file: candidate_change.py
- Status: PENDING
- To approve: reply APPROVE self-mod in chat, then run act_on_approval.py
"""

APPROVALS.write_text(APPROVALS.read_text() + proposal if APPROVALS.exists() else proposal)
CANDIDATE.write_text("print(\"Candidate self-mod health check OK\")\n")
print("Proposal written to APPROVALS.md and candidate_change.py created.")
