#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/home/opc/self-improving-ai")
LOG = ROOT / "daily_log.md"
with open(LOG, "a") as f:
    f.write("- Physics: retained g=9.8 m/s², c=3e8 m/s\n")
print("Physics basics logged")
