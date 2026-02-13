# Forensics Tools

Simple CLI tools for file and data forensics.

## Tools

### file-info.py
Analyze file metadata and identify file types by magic numbers.
```bash
python file-info.py suspicious.bin
```

### hidden-strings.sh
Search for hidden strings or patterns in files.
```bash
./hidden-strings.sh file.dat
./hidden-strings.sh file.dat "password"
```

## Common Patterns
- Hidden data in images
- Deleted file recovery
- Memory dumps analysis
- Log file analysis
- File carving
