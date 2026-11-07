#!/usr/bin/env python3
import datetime
import subprocess

def main():
    now = datetime.datetime.utcnow().isoformat()
    try:
        with open("APPROVALS.md", "r") as f:
            if "[x] Add resource monitor" not in f.read():
                return
        load = subprocess.getoutput("uptime | awk -F'load average:' '{print $2}' | awk '{print $1}' | tr -d ','")
        mem = subprocess.getoutput("free | awk '/Mem:/ {printf \"%.0f\", $3/$2 * 100}'")
        line = f"{now}: load={load} mem={mem}%"
        with open("resource.log", "a") as f:
            f.write(line + "\n")
        if float(load) > 1.0 or int(mem) > 80:
            with open("ideas.log", "a") as f:
                f.write(f"{now}: RESOURCE ALERT - {line}\n---\n")
    except Exception as e:
        with open("ideas.log", "a") as f:
            f.write(f"{now}: resource_monitor error: {e}\n---\n")

if __name__ == "__main__":
    main()
