#!/usr/bin/env bash
set -euo pipefail

if [ ! -v MODE ]; then
    >&2 echo "You need to indicate to use server or client mode by env var MODE!"
    exit 1
fi

if [ "${MODE}" = "server" ]; then
    python app.py
elif [ "${MODE}" = "client" ]; then
    python client.py
else
    >&2 echo "Unknown mode \"${MODE}\" given!"
    exit 1
fi
