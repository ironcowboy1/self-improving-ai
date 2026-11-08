#!/usr/bin/env python3
"""Append a retained fact / hypothesis."""
from pathlib import Path
import datetime
ROOT = Path("/home/opc/self-improving-ai")
KB = ROOT / "knowledge.md"
LOG = ROOT / "daily_log.md"
fact = f"- {datetime.datetime.utcnow().isoformat()}: Retained: 2+2=4 verified.\n"
with open(KB, "a") as f:
    f.write(fact)
with open(LOG, "a") as f:
    f.write("- Knowledge base updated\n")
print("Knowledge base updated")
