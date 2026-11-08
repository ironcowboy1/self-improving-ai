#!/usr/bin/env python3
"""List current modules and note a gap."""
from pathlib import Path
ROOT = Path("/home/opc/self-improving-ai")
LOG = ROOT / "daily_log.md"
mods = [p.name for p in ROOT.glob("*.py")]
line = f"- Capability inventory: {len(mods)} modules. Gap: advanced symbolic math.\n"
with open(LOG, "a") as f:
    f.write(line)
print(line.strip())
