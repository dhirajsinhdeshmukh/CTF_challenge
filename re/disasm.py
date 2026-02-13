#!/usr/bin/env python3
"""Simple disassembler wrapper"""

import sys
import subprocess

def disassemble(binary, func=None):
    """Disassemble a binary or specific function"""
    cmd = ['objdump', '-d', binary]
    if func:
        cmd.extend(['-M', 'intel'])
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if func:
            # Filter for specific function
            lines = result.stdout.split('\n')
            in_func = False
            for line in lines:
                if f'<{func}>' in line:
                    in_func = True
                if in_func:
                    print(line)
                    if line.strip() == '':
                        break
        else:
            print(result.stdout)
    except FileNotFoundError:
        print("Error: objdump not found. Install binutils.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python disasm.py <binary> [function]")
        sys.exit(1)
    
    binary = sys.argv[1]
    func = sys.argv[2] if len(sys.argv) > 2 else None
    disassemble(binary, func)
