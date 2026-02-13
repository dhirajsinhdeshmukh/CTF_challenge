#!/bin/bash
# List functions and symbols in a binary

if [ -z "$1" ]; then
    echo "Usage: $0 <binary>"
    exit 1
fi

echo "Functions in $1:"
echo "================"
nm -D "$1" 2>/dev/null || nm "$1"
