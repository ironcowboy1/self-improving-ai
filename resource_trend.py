#!/usr/bin/env python3
import datetime

def main():
    now = datetime.datetime.utcnow().isoformat()
    try:
        with open("resource.log", "r") as f:
            lines = f.readlines()[-24:]
        loads = [float(l.split("load=")[1].split()[0]) for l in lines if "load=" in l]
        avg = sum(loads)/len(loads) if loads else 0
        with open("resource_trend.md", "w") as f:
            f.write(f"# Resource Trend ({now})\n\nLast {len(loads)} samples. Average load: {avg:.2f}\n")
    except Exception as e:
        with open("ideas.log", "a") as f:
            f.write(f"{now}: resource_trend error: {e}\n---\n")

if __name__ == "__main__":
    main()
