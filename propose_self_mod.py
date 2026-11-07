#!/usr/bin/env python3
import datetime

def main():
    now = datetime.datetime.utcnow().isoformat()
    proposal = f"""{now}: Self-modification proposal
System is idle. Proposed change:
Add a lightweight task queue that can accept simple jobs (e.g. "summarize last 24h") and process them on the next hourly run.

Approve by adding this line to APPROVALS.md:
- [x] Add simple task queue
"""
    with open("ideas.log", "a") as f:
        f.write(proposal + "\n---\n")

if __name__ == "__main__":
    main()
