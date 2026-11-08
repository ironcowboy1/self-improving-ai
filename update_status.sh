#!/bin/bash
while true; do
  cd /home/opc/self-improving-ai
  python3 status_report.py
  git add status.html math_state.json daily_log.md 2>/dev/null
  git commit -m "Live status" --allow-empty >/dev/null 2>&1
  git push >/dev/null 2>&1
  sleep 30
done
