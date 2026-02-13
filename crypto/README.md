# Cryptography Tools

Simple CLI tools for cryptographic analysis.

## Tools

### frequency.py
Perform frequency analysis on text or ciphertext.
```bash
python frequency.py "encrypted text"
python frequency.py cipher.txt
```

### decode.sh
Decode base64 or hex encoded strings.
```bash
./decode.sh "SGVsbG8gV29ybGQ=" base64
./decode.sh "48656c6c6f" hex
```

## Common Patterns
- Caesar cipher
- XOR encryption
- Base64/hex encoding
- ROT13
- Substitution ciphers
