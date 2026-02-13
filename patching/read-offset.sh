#!/bin/bash
# Find and display bytes at specific offset

if [ -z "$2" ]; then
    echo "Usage: $0 <binary> <offset> [length]"
    echo "Example: $0 binary 0x1000 16"
    exit 1
fi

BINARY=$1
OFFSET=$2
LENGTH=${3:-16}

echo "Reading $LENGTH bytes from $BINARY at offset $OFFSET"
xxd -s "$OFFSET" -l "$LENGTH" "$BINARY"
