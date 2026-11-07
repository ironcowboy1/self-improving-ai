#!/usr/bin/env python3
import datetime, os
def main():
    now = datetime.datetime.utcnow().isoformat()
    py = len([f for f in os.listdir(".") if f.endswith(".py")])
    logs = len([f for f in os.listdir(".") if f.endswith(".log")])
    with open("progress.log", "a") as f:
        f.write(f"{now}: {py} modules, {logs} logs. System advancing.\n")
if __name__ == "__main__":
    main()
