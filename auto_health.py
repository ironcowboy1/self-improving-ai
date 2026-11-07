#!/usr/bin/env python3
import datetime, subprocess
def main():
    now = datetime.datetime.utcnow().isoformat()
    disk = subprocess.getoutput("df -h / | tail -1 | awk '{print $5}'")
    with open("health.log", "a") as f:
        f.write(f"{now}: disk={disk}\n")
if __name__ == "__main__":
    main()
