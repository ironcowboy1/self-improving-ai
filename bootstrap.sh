#!/bin/bash
# Basic bootstrap - version 0.1
echo "Self-improving AI bootstrap started at $(date)" >> ~/self-improving-ai/bootstrap.log
# Future modules will be added here

# Status report
echo "Status check at $(date)" >> ~/self-improving-ai/status.log
uptime >> ~/self-improving-ai/status.log
df -h / >> ~/self-improving-ai/status.log
echo "---" >> ~/self-improving-ai/status.log

# Commit status log
cd ~/self-improving-ai
git add status.log bootstrap.log 2>/dev/null
git commit -m "Hourly status $(date +%Y-%m-%d-%H)" --allow-empty 2>/dev/null
git push 2>/dev/null

# Run Python status module
python3 ~/self-improving-ai/status.py
python3 ~/self-improving-ai/ideas.py
python3 ~/self-improving-ai/generate_idea.py
python3 ~/self-improving-ai/track_idea.py
cat status.log | tail -10 > latest_status.md
python3 ~/self-improving-ai/improve.py
python3 ~/self-improving-ai/check_approvals.py
python3 ~/self-improving-ai/act_on_approval.py
python3 ~/self-improving-ai/disk_alert.py
python3 ~/self-improving-ai/daily_summary.py
python3 ~/self-improving-ai/self_check.py
python3 ~/self-improving-ai/propose_code_change.py
python3 ~/self-improving-ai/weekly_summary.py
python3 ~/self-improving-ai/next_proposal.py
python3 ~/self-improving-ai/resource_monitor.py
python3 ~/self-improving-ai/resource_trend.py
python3 ~/self-improving-ai/anomaly_check.py
python3 ~/self-improving-ai/propose_self_mod.py
python3 ~/self-improving-ai/task_queue.py

# Always pull before push to avoid conflicts
git pull --no-rebase --no-edit 2>/dev/null
python3 ~/self-improving-ai/auto_status.py
python3 ~/self-improving-ai/auto_ideas.py
python3 ~/self-improving-ai/auto_summary.py
git pull --no-rebase --no-edit 2>/dev/null
python3 ~/self-improving-ai/auto_progress.py
python3 ~/self-improving-ai/auto_health.py
python3 ~/self-improving-ai/auto_cleanup.py
python3 ~/self-improving-ai/capability_report.py
python3 /home/opc/self-improving-ai/act_on_self_mod.py
if [ $(date -u +%H) = 04 ]; then python3 /home/opc/self-improving-ai/email_send.py "Daily summary $(date +%Y-%m-%d)" "$(cat /home/opc/self-improving-ai/daily_log.md 2>/dev/null || echo No daily log yet)\n\n$(cat /home/opc/self-improving-ai/latest_status.md 2>/dev/null)"; fi
python3 /home/opc/self-improving-ai/resource_guard.py && python3 /home/opc/self-improving-ai/math_foundation.py && python3 /home/opc/self-improving-ai/code_scaffold.py && python3 /home/opc/self-improving-ai/knowledge_base.py && python3 /home/opc/self-improving-ai/capability_inventory.py && python3 /home/opc/self-improving-ai/progress_scale.py && python3 /home/opc/self-improving-ai/physics_basics.py && python3 /home/opc/self-improving-ai/language_pattern.py && python3 /home/opc/self-improving-ai/peer_bus.py
