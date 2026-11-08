#!/usr/bin/env python3
"""Check remaining headroom. Exit 0 if safe to run more work, 1 if tight."""
import shutil
import os

def check():
    # Disk
    total, used, free = shutil.disk_usage("/")
    disk_pct = used / total * 100
    # Memory (rough)
    meminfo = open("/proc/meminfo").read()
    mem_total = int([l for l in meminfo.splitlines() if "MemTotal" in l][0].split()[1])
    mem_avail = int([l for l in meminfo.splitlines() if "MemAvailable" in l][0].split()[1])
    mem_pct = (1 - mem_avail / mem_total) * 100
    # Load
    load = float(open("/proc/loadavg").read().split()[0])
    print(f"disk={disk_pct:.1f}% mem={mem_pct:.1f}% load={load:.2f}")
    if disk_pct > 85 or mem_pct > 80 or load > 1.5:
        print("Resources tight - skipping extra work")
        return 1
    return 0

if __name__ == "__main__":
    exit(check())
