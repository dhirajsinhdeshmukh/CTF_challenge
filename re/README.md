# Reverse Engineering Tools

Simple CLI tools for reverse engineering binaries.

## Tools

### disasm.py
Disassemble binaries or specific functions.
```bash
python disasm.py ./binary
python disasm.py ./binary main
```

### functions.sh
List all functions and symbols in a binary.
```bash
./functions.sh ./binary
```

## Common Patterns
- Analyze control flow
- Find anti-debugging techniques
- Locate obfuscated code
- Identify encryption routines
- Search for hard-coded keys
