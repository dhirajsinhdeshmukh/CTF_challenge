#!/bin/bash
# Find strings in a binary that might be useful

if [ -z "$1" ]; then
    echo "Usage: $0 <binary> [min-length]"
    exit 1
fi

BINARY=$1
MIN_LEN=${2:-4}

echo "Searching for strings (min length: $MIN_LEN) in $BINARY..."
strings -n $MIN_LEN "$BINARY" | grep -E "(flag|password|key|secret|user|admin|root)" -i || echo "No common patterns found"
