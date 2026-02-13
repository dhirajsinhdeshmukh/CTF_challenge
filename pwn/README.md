# PWN Tools

Simple CLI tools for binary exploitation analysis.

## Tools

### checksec.py
Check binary security features (RELRO, Canary, NX, PIE).
```bash
python checksec.py ./binary
```

### strings-grep.sh
Search for interesting strings in binaries.
```bash
./strings-grep.sh ./binary
./strings-grep.sh ./binary 8
```

## Common Patterns
- Buffer overflow vulnerabilities
- Format string bugs
- ROP chains
- Heap exploitation
- Integer overflows
