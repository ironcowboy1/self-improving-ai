#!/usr/bin/env python3
import datetime, os, glob
def main():
    now = datetime.datetime.utcnow().isoformat()
    old = glob.glob("auto-summary-*.md")
    if len(old) > 48:
        for f in sorted(old)[:-48]:
            os.remove(f)
    with open("ideas.log", "a") as f:
        f.write(f"{now}: Cleanup check complete.\n---\n")
if __name__ == "__main__":
    main()
