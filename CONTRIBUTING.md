# Contributing to CTF Toolkit

Thank you for contributing to the CTF Toolkit! This guide will help you add new tools or improve existing ones.

## Design Principles

1. **Minimal**: Keep tools small and focused
2. **Clean**: Write simple, readable code
3. **Portable**: Use standard libraries when possible
4. **No Bloat**: Avoid unnecessary dependencies

## Adding New Tools

### Structure

Each category directory should contain:
- Simple CLI tools (Python `.py` or shell `.sh` files)
- A `README.md` with usage examples
- Minimal, clear code

### Python Tools

```python
#!/usr/bin/env python3
"""Brief description of what the tool does"""

import sys

def main():
    """Main function"""
    if len(sys.argv) < 2:
        print("Usage: python tool.py <args>")
        sys.exit(1)
    
    # Tool logic here
    pass

if __name__ == "__main__":
    main()
```

**Guidelines:**
- Use standard library when possible
- Document optional dependencies clearly
- Handle errors gracefully
- Provide helpful usage messages
- Keep code under 100 lines if possible

### Shell Tools

```bash
#!/bin/bash
# Brief description of what the tool does

if [ -z "$1" ]; then
    echo "Usage: $0 <args>"
    exit 1
fi

# Tool logic here
```

**Guidelines:**
- Use POSIX-compliant shell when possible
- Test on both Ubuntu and Kali
- Use standard Unix tools (grep, awk, sed, etc.)
- Handle missing tools gracefully

## Adding Dependencies

### Core Dependencies
Add to `pyproject.toml` under `[project.dependencies]`:
```toml
dependencies = [
    "package>=version",
]
```

### Optional Dependencies
Add to `[project.optional-dependencies]`:
```toml
[project.optional-dependencies]
category = [
    "optional-package>=version",
]
```

### System Dependencies
Add to both setup scripts:
- `setup-ubuntu.sh`
- `setup-kali.sh`

## Category Guidelines

### Web
- HTTP/HTTPS analysis
- Web vulnerability scanning
- Header/cookie analysis
- Directory/endpoint discovery

### PWN
- Binary exploitation
- Buffer overflow analysis
- ROP gadget finding
- Memory corruption

### Reverse Engineering
- Disassembly
- Decompilation
- Binary analysis
- Obfuscation removal

### Cryptography
- Cipher analysis
- Encoding/decoding
- Frequency analysis
- Hash operations

### Forensics
- File analysis
- Metadata extraction
- Data recovery
- Log analysis

### Steganography
- Image analysis
- LSB extraction
- Metadata hiding
- Audio steganography

### Miscellaneous
- Hash cracking
- Format conversion
- QR codes
- Puzzles

### Mobile
- APK/IPA analysis
- App decompilation
- Resource extraction
- String analysis

### Network
- PCAP analysis
- Traffic reconstruction
- Protocol analysis
- Packet inspection

### Patching
- Binary modification
- Instruction patching
- Control flow changes
- Anti-debug removal

## Testing

Before submitting:

1. **Test your tool**:
   ```bash
   ./category/tool.sh <test-args>
   python category/tool.py <test-args>
   ```

2. **Update README**:
   Add usage example to category README.md

3. **Check permissions**:
   ```bash
   chmod +x category/*.sh
   ```

4. **Verify clean code**:
   - No unnecessary comments
   - Clear variable names
   - Minimal dependencies

## AI Agents

When adding tools to a category, consider updating the corresponding agent in `.github/agents/<category>` if:
- New flag patterns are introduced
- New attack vectors are relevant
- New analysis techniques are added

## Pull Request Guidelines

1. One tool per PR when possible
2. Test on Ubuntu or Kali
3. Update relevant documentation
4. Follow existing code style
5. Keep changes minimal

## Code Style

### Python
- Follow PEP 8 loosely
- Use docstrings for functions
- Handle errors with try/except
- Print to stderr for errors

### Shell
- Use lowercase variables
- Quote all variables
- Check for command existence
- Provide helpful error messages

## Examples

See existing tools in each category for reference:
- `web/headers.py` - Simple HTTP tool
- `crypto/decode.sh` - Shell script wrapper
- `forensics/file-info.py` - File analysis
- `misc/hash.py` - Utility tool

## Questions?

Open an issue or discussion on GitHub.
