#!/bin/bash
# Check image metadata with exiftool

if [ -z "$1" ]; then
    echo "Usage: $0 <image-file>"
    exit 1
fi

if ! command -v exiftool &> /dev/null; then
    echo "Analyzing metadata with strings (exiftool not installed)..."
    strings "$1" | head -50
else
    echo "Analyzing metadata with exiftool..."
    exiftool "$1"
fi
