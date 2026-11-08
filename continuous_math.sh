#!/bin/bash
cd /home/opc/self-improving-ai
while true; do
  for i in 1 2 3 4 5 6 7 8; do
    python3 math_foundation.py &
  done
  wait
done
