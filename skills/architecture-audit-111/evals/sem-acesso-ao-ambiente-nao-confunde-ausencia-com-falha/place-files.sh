#!/usr/bin/env bash
set -eu
cp -R "$(dirname "$0")/files/." .
# o arquivo de ambiente fictício é versionado como "dot-env" para não acionar detectores de segredo
find . -name dot-env -exec sh -c 'mv "$1" "$(dirname "$1")/.env"' _ {} \;
