# CTF Toolkit

A minimal, organized collection of CLI tools and AI agents for Capture The Flag (CTF) competitions.

## Overview

This repository provides simple, focused tools organized by category, along with AI agents that can analyze files and systems for common CTF patterns and flags.

## Structure

```
.
├── web/              # Web exploitation tools
├── pwn/              # Binary exploitation tools
├── re/               # Reverse engineering tools
├── crypto/           # Cryptography analysis tools
├── forensics/        # Digital forensics tools
├── stego/            # Steganography tools
├── misc/             # Miscellaneous utilities
├── mobile/           # Mobile app analysis tools
├── network/          # Network traffic analysis tools
├── patching/         # Binary patching tools
└── .github/agents/   # AI agents for automated analysis
```

## Quick Start

### 1. Setup

**For Ubuntu/Debian:**
```bash
chmod +x setup-ubuntu.sh
./setup-ubuntu.sh
```

**For Kali Linux:**
```bash
chmod +x setup-kali.sh
./setup-kali.sh
```

### 2. Activate Python Environment

```bash
source .venv/bin/activate
```

### 3. Make Scripts Executable

```bash
chmod +x */*.sh
```

## Tools by Category

### Web (`web/`)
- **port-scan.sh**: Scan common web ports
- **headers.py**: Analyze HTTP headers

### PWN (`pwn/`)
- **checksec.py**: Check binary security features
- **strings-grep.sh**: Find interesting strings

### Reverse Engineering (`re/`)
- **disasm.py**: Disassemble binaries
- **functions.sh**: List functions and symbols

### Cryptography (`crypto/`)
- **frequency.py**: Frequency analysis for ciphers
- **decode.sh**: Decode base64/hex strings

### Forensics (`forensics/`)
- **file-info.py**: Analyze file metadata
- **hidden-strings.sh**: Search for hidden patterns

### Steganography (`stego/`)
- **lsb-extract.py**: Extract LSB data from images
- **metadata.sh**: Extract image metadata

### Miscellaneous (`misc/`)
- **hash.py**: Calculate file hashes
- **convert.sh**: Convert between formats

### Mobile (`mobile/`)
- **apk-info.py**: Analyze APK files
- **strings-extract.sh**: Extract strings from apps

### Network (`network/`)
- **pcap-analyze.py**: Analyze PCAP files
- **http-extract.sh**: Extract HTTP traffic

### Patching (`patching/`)
- **patch.py**: Patch binaries at offsets
- **read-offset.sh**: Read bytes at offset

## AI Agents

The `.github/agents/` directory contains specialized AI agent instructions for each category. These agents are designed to:
- Scan files and systems for flags
- Identify common CTF patterns
- Suggest exploitation techniques
- Automate initial analysis

Each agent specializes in its category (web, pwn, crypto, etc.) and knows common flag formats, attack vectors, and analysis techniques.

## Python Dependencies

### Core (always installed)
- `requests`: HTTP library
- `pycryptodome`: Cryptography primitives

### Optional (install as needed)
```bash
# For steganography
uv pip install pillow

# For network analysis
uv pip install scapy

# All optional dependencies
uv pip install -e ".[all]"
```

## Usage Examples

### Web Analysis
```bash
python web/headers.py https://example.com
./web/port-scan.sh target.com 1-1000
```

### Binary Analysis
```bash
python pwn/checksec.py ./binary
./pwn/strings-grep.sh ./binary
```

### Cryptography
```bash
python crypto/frequency.py ciphertext.txt
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

### Network Analysis
```bash
python network/pcap-analyze.py capture.pcap
./network/http-extract.sh traffic.pcap
```

## Design Philosophy

This toolkit follows these principles:
- **Minimal**: Small, focused tools doing one thing well
- **Clean**: Simple code, easy to understand and modify
- **Organized**: Clear category structure
- **Portable**: Standard tools, minimal dependencies
- **Extensible**: Easy to add new tools

## Contributing

Each category should have:
1. Simple CLI tools (Python or shell)
2. A README.md with usage examples
3. Clear, minimal code
4. No unnecessary dependencies

## License

See [LICENSE](LICENSE) file for details. 
