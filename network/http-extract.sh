#!/bin/bash
# Extract HTTP traffic from PCAP

if [ -z "$1" ]; then
    echo "Usage: $0 <pcap-file>"
    exit 1
fi

if command -v tshark &> /dev/null; then
    echo "Extracting HTTP traffic with tshark..."
    tshark -r "$1" -Y "http" -T fields -e http.request.method -e http.request.uri -e http.response.code
else
    echo "tshark not found. Install wireshark/tshark for better analysis."
    echo "Basic strings analysis:"
    strings "$1" | grep -E "(GET|POST|HTTP)" | head -20
fi
