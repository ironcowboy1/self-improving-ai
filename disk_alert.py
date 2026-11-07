#!/usr/bin/env python3
import datetime
import subprocess

def main():
    now = datetime.datetime.utcnow().isoformat()
    try:
        with open("APPROVALS.md", "r") as f:
            if "[x]" not in f.read():
                return
        df = subprocess.getoutput("df -h / | tail -1")
        use = int(df.split()[4].replace("%",""))
        if use > 80:
            msg = f"DISK ALERT: {use}% used"
        else:
            msg = f"Disk OK: {use}% used"
        with open("ideas.log", "a") as f:
            f.write(f"{now}: {msg}\n---\n")
    except Exception as e:
        with open("ideas.log", "a") as f:
            f.write(f"{now}: disk_alert error: {e}\n---\n")

if __name__ == "__main__":
    main()
