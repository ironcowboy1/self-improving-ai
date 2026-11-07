#!/usr/bin/env python3
import datetime
import glob

def main():
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    files = sorted(glob.glob("summary-*.md"))[-7:]
    with open("weekly-summary.md", "w") as out:
        out.write(f"# Weekly Summary (as of {now})\n\n")
        for f in files:
            out.write(f"## {f}\n")
            with open(f) as infile:
                out.write(infile.read())
            out.write("\n---\n")
        out.write("\n## Key observations\n- System running autonomously\n- Approval gates active\n")

if __name__ == "__main__":
    main()
