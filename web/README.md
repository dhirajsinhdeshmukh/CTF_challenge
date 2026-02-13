# Web Tools

Simple CLI tools for web exploitation and analysis.

## Tools

### port-scan.sh
Scan common web ports on a target host.
```bash
./port-scan.sh example.com
./port-scan.sh example.com 1-1000
```

### headers.py
Analyze HTTP response headers.
```bash
python headers.py https://example.com
```

## Common Patterns
- Look for debug headers (X-Debug, X-Powered-By)
- Check for directory listings
- Test for SQL injection in parameters
- Analyze cookies and session tokens
