#!/bin/bash
# Simple port scanner for web services

if [ -z "$1" ]; then
    echo "Usage: $0 <host> [port-range]"
    echo "Example: $0 example.com 1-1000"
    exit 1
fi

HOST=$1
RANGE=${2:-80,443,8080,8443}

echo "Scanning $HOST on ports $RANGE..."
nmap -p $RANGE $HOST
