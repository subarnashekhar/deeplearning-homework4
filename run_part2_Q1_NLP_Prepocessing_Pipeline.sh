#!/usr/bin/env bash
set -euo pipefail

WORKDIR="$(cd "$(dirname "$0")" && pwd)"
SCRIPT="$WORKDIR/part2_Q1_NLP_Prepocessing_Pipeline.py"
VENV_DIR="$WORKDIR/.venv-part2-q1"
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

if ! "$VENV_PY" -c "import nltk" >/dev/null 2>&1; then
  echo "Installing NLTK in $VENV_DIR..."
  "$VENV_PY" -m pip install nltk
fi

exec "$VENV_PY" "$SCRIPT" "$@"
