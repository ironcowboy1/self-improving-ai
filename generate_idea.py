#!/usr/bin/env python3
import datetime

def main():
    now = datetime.datetime.utcnow().isoformat()
    idea = f"{now}: Check status.log for high load or low disk and propose a fix."
    with open("ideas.log", "a") as f:
        f.write(idea + "\n")
    print(idea)

if __name__ == "__main__":
    main()
