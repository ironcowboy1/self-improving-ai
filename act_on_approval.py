#!/usr/bin/env python3
import datetime

def main():
    now = datetime.datetime.utcnow().isoformat()
    try:
        with open("APPROVALS.md", "r") as f:
            content = f.read()
        if "[x]" in content:
            action = "Would add disk alert (approval found)"
        else:
            action = "No approval, skipping action"
    except:
        action = "No approvals file"
    with open("ideas.log", "a") as f:
        f.write(f"{now}: Action check: {action}\n---\n")

if __name__ == "__main__":
    main()
