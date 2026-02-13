#!/usr/bin/env python3
"""Simple frequency analysis for ciphers"""

import sys
from collections import Counter

def analyze_frequency(text):
    """Analyze character frequency"""
    text = text.upper()
    letters = [c for c in text if c.isalpha()]
    
    if not letters:
        print("No letters found in text")
        return
    
    freq = Counter(letters)
    total = len(letters)
    
    print("\nFrequency Analysis:")
    print("-" * 50)
    for char, count in freq.most_common():
        pct = (count / total) * 100
        print(f"{char}: {count:4d} ({pct:5.2f}%) {'#' * int(pct)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python frequency.py <text or file>")
        sys.exit(1)
    
    try:
        with open(sys.argv[1], 'r') as f:
            text = f.read()
    except FileNotFoundError:
        text = sys.argv[1]
    
    analyze_frequency(text)
