# Mobile Tools

Simple CLI tools for mobile app analysis.

## Tools

### apk-info.py
Analyze APK file structure and contents.
```bash
python apk-info.py app.apk
```

### strings-extract.sh
Extract interesting strings from APK or mobile binaries.
```bash
./strings-extract.sh app.apk
./strings-extract.sh libapp.so
```

## Common Patterns
- Hardcoded API keys
- Debug flags
- Hidden URLs
- Native library analysis
- Certificate pinning bypass
