#!/usr/bin/env python3
"""Calculate hash digests for files"""

import sys
import hashlib

def hash_file(filepath):
    """Calculate various hashes for a file"""
    try:
        with open(filepath, 'rb') as f:
            data = f.read()
        
        print(f"\nHashes for {filepath}:")
        print("-" * 50)
        print(f"MD5:    {hashlib.md5(data).hexdigest()}")
        print(f"SHA1:   {hashlib.sha1(data).hexdigest()}")
        print(f"SHA256: {hashlib.sha256(data).hexdigest()}")
        
    except FileNotFoundError:
        print(f"Error: File {filepath} not found", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python hash.py <file>")
        sys.exit(1)
    hash_file(sys.argv[1])
