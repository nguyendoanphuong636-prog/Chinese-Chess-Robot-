#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

python3 -m venv "${PROJECT_ROOT}/.venv"
# shellcheck disable=SC1091
source "${PROJECT_ROOT}/.venv/bin/activate"
pip install --upgrade pip
pip install -r "${PROJECT_ROOT}/requirements.txt"

echo "Setup complete. Activate with: source ${PROJECT_ROOT}/.venv/bin/activate"
