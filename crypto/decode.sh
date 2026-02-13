#!/bin/bash
# Simple base64/hex decoder

if [ -z "$1" ]; then
    echo "Usage: $0 <encoded-string> [base64|hex]"
    exit 1
fi

INPUT=$1
TYPE=${2:-base64}

case $TYPE in
    base64)
        echo "$INPUT" | base64 -d
        ;;
    hex)
        echo "$INPUT" | xxd -r -p
        ;;
    *)
        echo "Unknown type: $TYPE"
        exit 1
        ;;
esac
