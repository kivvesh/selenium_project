#!/usr/bin/env bash
set -e

echo "Starting wait-for-it.sh"
TIMEOUT=15
WAITFORIT=0

while [[ $WAITFORIT -lt $TIMEOUT ]]; do
    echo "Attempting to connect to $1:$2..."
    nc -z $1 $2 && break
    sleep 1
    WAITFORIT=$((WAITFORIT + 1))
done

if [[ $WAITFORIT -eq $TIMEOUT ]]; then
    echo "Timeout waiting for $1:$2"
    exit 1
fi

echo "$1:$2 is up!"
echo "Executing command: ${@:3}"
exec "${@:3}"