#!/usr/bin/env bash
# Gera dist/architecture-audit-111.zip no formato aceito pelo Claude.ai
# (a pasta do skill como raiz do ZIP; casos de teste ficam de fora).
set -eu
cd "$(dirname "$0")/../skills"
mkdir -p ../dist
rm -f ../dist/architecture-audit-111.zip
zip -qr ../dist/architecture-audit-111.zip architecture-audit-111 \
  -x "architecture-audit-111/evals/*" "*/__pycache__/*" "*.pyc" "*.DS_Store"
echo "OK: dist/architecture-audit-111.zip"
