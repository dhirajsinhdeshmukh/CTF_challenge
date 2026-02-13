#!/usr/bin/env python3
"""Simple HTTP header analyzer"""

import sys
import urllib.request

def analyze_headers(url):
    """Fetch and display HTTP headers"""
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=10) as response:
            print(f"\nHeaders for {url}:")
            print("-" * 50)
            for header, value in response.headers.items():
                print(f"{header}: {value}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python headers.py <url>")
        sys.exit(1)
    analyze_headers(sys.argv[1])
