#!/usr/bin/env python3
import datetime, subprocess
def main():
    now = datetime.datetime.utcnow().isoformat()
    load = subprocess.getoutput("uptime | awk -F'load average:' '{print $2}' | awk '{print $1}' | tr -d ','")
    mem = subprocess.getoutput("free | awk '/Mem:/ {printf \"%.0f\", $3/$2 * 100}'")
    with open("auto_status.log", "a") as f:
        f.write(f"{now}: load={load} mem={mem}%\n")
if __name__ == "__main__":
    main()
