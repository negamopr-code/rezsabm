#!/usr/bin/env bash
# Build + (re)start the REZSABM container. Canonical address: http://localhost:8112/
# Works from the host OR from inside a claude container (docker talks to the host daemon;
# the -v paths below must be HOST paths).
set -euo pipefail
HOST_DIR="/root/claude-sandbox/workspaces/REZSABM"
# The exit advisor needs three things the lab itself doesn't:
#   docker.sock  → run the nlm CLI inside awf-monitor-runner (work4 cookies live there)
#   NLM_WORK     → shared dir: /nlmwork here == /app there, how the chart PDF crosses over
#   /seed:ro     → Claude Code OAuth token, only used by the optional "precise mode"
NLM_WORK="/root/claude-sandbox/workspaces/need collecting from customers comments"
DIR="$(cd "$(dirname "$0")/.." && pwd)"
docker build -t rezsabm-serve:latest "$DIR"
docker rm -f rezsabm-serve 2>/dev/null || true
docker run -d --name rezsabm-serve --restart unless-stopped \
  -p 8112:8112 -u 1000:1000 \
  -v "$HOST_DIR":/app \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v "$NLM_WORK":/nlmwork \
  -v /root/.claude:/seed:ro \
  rezsabm-serve:latest
echo "REZSABM: http://localhost:8112/"
