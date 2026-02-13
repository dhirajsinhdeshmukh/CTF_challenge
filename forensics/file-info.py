#!/usr/bin/env python3
"""File metadata and magic number analyzer"""

import sys
import os

MAGIC_NUMBERS = {
    b'\x89PNG': 'PNG image',
    b'GIF8': 'GIF image',
    b'\xff\xd8\xff': 'JPEG image',
    b'PK\x03\x04': 'ZIP archive',
    b'PK\x05\x06': 'ZIP archive (empty)',
    b'\x1f\x8b': 'GZIP compressed',
    b'BM': 'BMP image',
    b'%PDF': 'PDF document',
    b'\x7fELF': 'ELF binary',
    b'MZ': 'PE executable',
}

def analyze_file(filepath):
    """Analyze file metadata and magic numbers"""
    if not os.path.exists(filepath):
        print(f"Error: File {filepath} not found", file=sys.stderr)
        sys.exit(1)
    
    print(f"\nFile Analysis: {filepath}")
    print("-" * 50)
    print(f"Size: {os.path.getsize(filepath)} bytes")
    
    with open(filepath, 'rb') as f:
        header = f.read(16)
    
    print(f"Header (hex): {header.hex()}")
    
    # Check magic numbers
    file_type = "Unknown"
    for magic, desc in MAGIC_NUMBERS.items():
        if header.startswith(magic):
            file_type = desc
            break
    
    print(f"Type: {file_type}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python file-info.py <file>")
        sys.exit(1)
    analyze_file(sys.argv[1])
