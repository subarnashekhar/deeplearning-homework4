#!/usr/bin/env bash
set -euo pipefail

WORKDIR="$(cd "$(dirname "$0")" && pwd)"
SCRIPT="$WORKDIR/part2_Q2_Scaled_Dot_Product_Attention.py"
VENV_DIR="$WORKDIR/.venv-part2-q2"
VENV_PY="$VENV_DIR/bin/python"

if [[ ! -x "$VENV_PY" ]]; then
  if [[ -x "$WORKDIR/.venv/bin/python" ]]; then
    BASE_PY="$WORKDIR/.venv/bin/python"
  elif command -v python3 >/dev/null 2>&1; then
    BASE_PY="$(command -v python3)"
  else
    echo "Python 3 not found in PATH." >&2
    exit 1
  fi
  "$BASE_PY" -m venv "$VENV_DIR"
fi

if ! "$VENV_PY" -c "import numpy" >/dev/null 2>&1; then
  echo "Installing NumPy in $VENV_DIR..."
  "$VENV_PY" -m pip install numpy
fi

exec "$VENV_PY" "$SCRIPT" "$@"
