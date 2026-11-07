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
