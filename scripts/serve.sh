#!/usr/bin/env bash
# Build + (re)start the REZSABM container. Canonical address: http://localhost:8112/
# Works from the host OR from inside a claude container (docker talks to the host daemon;
# the -v path below must be the HOST path of this project).
set -euo pipefail
HOST_DIR="/root/claude-sandbox/workspaces/REZSABM"
DIR="$(cd "$(dirname "$0")/.." && pwd)"
docker build -t rezsabm-serve:latest "$DIR"
docker rm -f rezsabm-serve 2>/dev/null || true
docker run -d --name rezsabm-serve --restart unless-stopped \
  -p 8112:8112 -u 1000:1000 \
  -v "$HOST_DIR":/app \
  rezsabm-serve:latest
echo "REZSABM: http://localhost:8112/"
