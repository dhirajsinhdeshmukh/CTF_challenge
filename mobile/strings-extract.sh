#!/bin/bash
# Extract strings from mobile app binaries

if [ -z "$1" ]; then
    echo "Usage: $0 <apk or binary>"
    exit 1
fi

FILE=$1

if [[ $FILE == *.apk ]]; then
    echo "Extracting strings from APK..."
    unzip -p "$FILE" classes.dex 2>/dev/null | strings | grep -E "(http|flag|key|secret|password|api)" -i | head -50
else
    echo "Extracting strings from binary..."
    strings "$FILE" | grep -E "(http|flag|key|secret|password|api)" -i | head -50
fi
