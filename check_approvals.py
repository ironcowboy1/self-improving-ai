#!/usr/bin/env python3
import datetime

def main():
    now = datetime.datetime.utcnow().isoformat()
    try:
        with open("APPROVALS.md", "r") as f:
            content = f.read()
        approved = "[x]" in content
        status = "Approved items found" if approved else "No approvals yet"
    except:
        status = "No approvals file"
    with open("ideas.log", "a") as f:
        f.write(f"{now}: Approval check: {status}\n---\n")

if __name__ == "__main__":
    main()
