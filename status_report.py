#!/usr/bin/env python3
"""On-demand report + simple HTML page."""
import json
import shutil
from pathlib import Path

ROOT = Path("/home/opc/self-improving-ai")
STATE = ROOT / "math_state.json"
LOG = ROOT / "daily_log.md"
HTML = ROOT / "status.html"

lines = ["<html><head><meta charset=utf-8><title>AI Status</title>",
         "<meta name=viewport content=\"width=device-width\">",
         "<style>body{font-family:sans-serif;padding:1em;background:#111;color:#eee}</style></head><body>",
         "<h2>Self-Improving AI Status</h2>"]

if STATE.exists():
    s = json.loads(STATE.read_text())
    level = s.get("level", 1)
    correct = s.get("correct", 0)
    total = s.get("total", 0)
    if level == 1:
        scale = f"grade-school addition ({correct} correct)"
    elif level == 2:
        scale = "middle-school multiplication"
    elif level == 3:
        scale = "early high-school exponents"
    else:
        scale = "simple algebra (x + a = b)"
    lines.append(f"<p><b>Math scale:</b> {scale}</p>")
    lines.append(f"<p><b>Problems:</b> {correct} correct / {total} total</p>")
else:
    lines.append("<p><b>Math scale:</b> not started (still at 2+2)</p>")

total, used, free = shutil.disk_usage("/")
disk_pct = used / total * 100
meminfo = open("/proc/meminfo").read()
mem_total = int([l for l in meminfo.splitlines() if "MemTotal" in l][0].split()[1])
mem_avail = int([l for l in meminfo.splitlines() if "MemAvailable" in l][0].split()[1])
mem_pct = (1 - mem_avail / mem_total) * 100
load = float(open("/proc/loadavg").read().split()[0])
lines.append(f"<p><b>Resources:</b> disk {disk_pct:.1f}% used, memory {mem_pct:.1f}% used, load {load:.2f}</p>")

mods = list(ROOT.glob("*.py"))
lines.append(f"<p><b>Modules:</b> {len(mods)} Python files</p>")

if LOG.exists():
    recent = LOG.read_text().strip().splitlines()[-5:]
    lines.append("<p><b>Recent log:</b></p><ul>")
    for line in recent:
        lines.append(f"<li>{line}</li>")
    lines.append("</ul>")

lines.append("</body></html>")
HTML.write_text("\n".join(lines))
print("status.html updated")
print("Math scale and resources written.")
