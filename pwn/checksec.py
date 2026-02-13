#!/usr/bin/env python3
"""Simple checksec tool to check binary security features"""

import sys
import subprocess

def checksec(binary):
    """Check security features of a binary"""
    print(f"\nSecurity features for {binary}:")
    print("-" * 50)
    
    try:
        # Check for RELRO
        result = subprocess.run(['readelf', '-l', binary], capture_output=True, text=True)
        relro = 'GNU_RELRO' in result.stdout
        print(f"RELRO: {'Yes' if relro else 'No'}")
        
        # Check for stack canary
        result = subprocess.run(['readelf', '-s', binary], capture_output=True, text=True)
        canary = '__stack_chk_fail' in result.stdout
        print(f"Stack Canary: {'Yes' if canary else 'No'}")
        
        # Check for NX
        result = subprocess.run(['readelf', '-l', binary], capture_output=True, text=True)
        nx = 'GNU_STACK' in result.stdout
        print(f"NX: {'Yes' if nx else 'No'}")
        
        # Check for PIE
        result = subprocess.run(['readelf', '-h', binary], capture_output=True, text=True)
        pie = 'DYN' in result.stdout
        print(f"PIE: {'Yes' if pie else 'No'}")
        
    except FileNotFoundError:
        print("Error: readelf not found. Install binutils.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python checksec.py <binary>")
        sys.exit(1)
    checksec(sys.argv[1])
