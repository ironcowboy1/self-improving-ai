#!/usr/bin/env python3
import datetime

def main():
    now = datetime.datetime.utcnow().isoformat()
    try:
        with open("resource.log", "r") as f:
            last = f.readlines()[-1]
        if "load=0.00" in last and "mem=" in last:
            with open("ideas.log", "a") as f:
                f.write(f"{now}: Anomaly check: system idle, no action needed.\n---\n")
    except:
        pass

if __name__ == "__main__":
    main()
