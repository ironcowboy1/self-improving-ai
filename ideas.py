#!/usr/bin/env python3
import datetime

def main():
    now = datetime.datetime.utcnow().isoformat()
    idea = f"Idea logged at {now}: Review status.log and propose one small improvement."
    with open("ideas.log", "a") as f:
        f.write(idea + "\n")

if __name__ == "__main__":
    main()
