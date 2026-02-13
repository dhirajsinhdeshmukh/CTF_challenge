# CTF Toolkit Quick Reference

## Setup
```bash
# Ubuntu/Debian
./setup-ubuntu.sh

# Kali Linux
./setup-kali.sh

# Activate environment
source .venv/bin/activate
```

## Quick Commands

### Web
```bash
./web/port-scan.sh target.com
python web/headers.py https://target.com
```

### PWN
```bash
python pwn/checksec.py ./binary
./pwn/strings-grep.sh ./binary
```

### Reverse Engineering
```bash
python re/disasm.py ./binary
./re/functions.sh ./binary
```

### Cryptography
```bash
python crypto/frequency.py "cipher text"
./crypto/decode.sh "SGVsbG8=" base64
```

### Forensics
```bash
python forensics/file-info.py suspicious.bin
./forensics/hidden-strings.sh file.dat "flag"
```

### Steganography
```bash
python stego/lsb-extract.py image.png
./stego/metadata.sh photo.jpg
```

### Miscellaneous
```bash
python misc/hash.py file.txt
./misc/convert.sh "data" hex
```

### Mobile
```bash
python mobile/apk-info.py app.apk
./mobile/strings-extract.sh app.apk
```

### Network
```bash
python network/pcap-analyze.py capture.pcap
./network/http-extract.sh traffic.pcap
```

### Patching
```bash
python patching/patch.py binary 0x1234 "90 90"
./patching/read-offset.sh binary 0x1000
```

## Common Flag Patterns
- `flag{...}` or `FLAG{...}`
- `ctf{...}` or `CTF{...}`
- Base64 encoded
- In comments/metadata
- Hidden in strings
- Result of operations

## AI Agents
Located in `.github/agents/<category>`
- Specialized knowledge per category
- Flag pattern recognition
- Common attack vectors
- Analysis techniques

## Optional Dependencies
```bash
# Steganography
uv pip install pillow

# Network analysis
uv pip install scapy

# All optional
uv pip install -e ".[all]"
```
