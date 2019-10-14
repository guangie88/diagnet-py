#!/usr/bin/env bash
set -euo pipefail

if [ $# -ne 1 ]; then
    >&2 echo "You need to indicate to use server or client mode!"
    exit 1
fi

if [ "$1" = "server" ]; then
    python app.py
elif [ "$1" = "client" ]; then
    python client.py
else
    >&2 echo "Unknown mode \"$1\" given!"
    exit 1
fi
