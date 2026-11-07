#!/usr/bin/env python3
import datetime

def main():
    now = datetime.datetime.utcnow().isoformat()
    proposal = f"""{now}: Next proposal
Add a simple resource monitor that:
1. Checks CPU load and memory use
2. Writes a one-line summary to resource.log
3. Proposes an alert if load > 1.0 or memory > 80%

Approve by adding this line to APPROVALS.md:
- [x] Add resource monitor
"""
    with open("ideas.log", "a") as f:
        f.write(proposal + "\n---\n")

if __name__ == "__main__":
    main()
