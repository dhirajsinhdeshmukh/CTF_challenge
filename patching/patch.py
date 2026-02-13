#!/usr/bin/env python3
"""Simple binary patcher"""

import sys

def patch_binary(binary_path, offset, new_bytes):
    """Patch binary at specified offset"""
    try:
        offset_int = int(offset, 16) if offset.startswith('0x') else int(offset)
        patch_bytes = bytes.fromhex(new_bytes.replace(' ', ''))
        
        with open(binary_path, 'r+b') as f:
            f.seek(offset_int)
            original = f.read(len(patch_bytes))
            f.seek(offset_int)
            f.write(patch_bytes)
        
        print(f"\nPatched {binary_path}")
        print(f"Offset: {hex(offset_int)}")
        print(f"Original: {original.hex()}")
        print(f"Patched:  {patch_bytes.hex()}")
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python patch.py <binary> <offset> <hex-bytes>")
        print("Example: python patch.py binary 0x1234 '90 90 90'")
        sys.exit(1)
    
    patch_binary(sys.argv[1], sys.argv[2], sys.argv[3])
