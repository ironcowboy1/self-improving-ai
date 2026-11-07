#!/usr/bin/env python3
import datetime

def main():
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    with open("status.log", "r") as f:
        lines = f.readlines()[-15:]
    with open(f"summary-{now}.md", "w") as f:
        f.write(f"# Daily Summary {now}\n\n")
        f.write("".join(lines))
