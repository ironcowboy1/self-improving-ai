#!/usr/bin/env python3
import datetime
def main():
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d-%H")
    with open("status.log", "r") as f:
        lines = f.readlines()[-5:]
    with open(f"auto-summary-{now}.md", "w") as f:
        f.write(f"# Auto Summary {now}\n\n" + "".join(lines))
if __name__ == "__main__":
    main()
