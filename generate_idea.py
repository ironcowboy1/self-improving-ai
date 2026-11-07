#!/usr/bin/env python3
import datetime

def main():
    now = datetime.datetime.utcnow().isoformat()
    try:
        with open("status.log", "r") as f:
            last = f.readlines()[-5:]
        summary = "".join(last).strip()
    except:
        summary = "No status yet"
    idea = f"{now}: Reviewed status. Last lines:\n{summary}\nProposed: Monitor disk use and alert if over 80%."
    with open("ideas.log", "a") as f:
        f.write(idea + "\n---\n")

if __name__ == "__main__":
    main()
