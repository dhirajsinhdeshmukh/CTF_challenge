#!/bin/bash
# Convert between different formats

if [ -z "$2" ]; then
    echo "Usage: $0 <input> <format>"
    echo "Formats: hex, base64, ascii, binary"
    exit 1
fi

INPUT=$1
FORMAT=$2

case $FORMAT in
    hex)
        echo -n "$INPUT" | xxd -p
        ;;
    base64)
        echo -n "$INPUT" | base64
        ;;
    ascii)
        echo -n "$INPUT" | od -A n -t d1
        ;;
    binary)
        echo -n "$INPUT" | xxd -b
        ;;
    *)
        echo "Unknown format: $FORMAT"
        exit 1
        ;;
esac
