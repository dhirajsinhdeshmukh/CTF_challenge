# Patching Tools

Simple CLI tools for binary patching and modification.

## Tools

### patch.py
Patch binary files at specific offsets.
```bash
python patch.py binary 0x1234 '90 90 90'
```

### read-offset.sh
Read and display bytes at specific offset.
```bash
./read-offset.sh binary 0x1000
./read-offset.sh binary 0x1000 32
```

## Common Patterns
- NOP instructions (0x90)
- Jump modifications
- License checks bypass
- Function hooking
- Anti-debug removal
