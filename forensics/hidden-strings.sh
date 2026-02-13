#!/bin/bash
# Search for hidden strings in files

if [ -z "$1" ]; then
    echo "Usage: $0 <file> [pattern]"
    exit 1
fi

FILE=$1
PATTERN=${2:-flag}

echo "Searching for '$PATTERN' in $FILE..."
strings "$FILE" | grep -i "$PATTERN" || echo "Pattern not found"
