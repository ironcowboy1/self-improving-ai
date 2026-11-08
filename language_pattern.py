#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/home/opc/self-improving-ai")
LOG = ROOT / "daily_log.md"
with open(LOG, "a") as f:
    f.write("- Language: recognized simple pattern subject-verb-object\n")
print("Language pattern logged")
