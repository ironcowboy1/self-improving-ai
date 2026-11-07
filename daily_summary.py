#!/usr/bin/env python3
import datetime

def main():
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    filename = f"summary-{now}.md"
    print(f"Writing to {filename}")
    with open("status.log", "r") as f:
        lines = f.readlines()[-15:]
    with open(filename, "w") as f:
        f.write(f"# Daily Summary {now}\n\n")
        f.write("".join(lines))
    print("Done")

if __name__ == "__main__":
    main()
