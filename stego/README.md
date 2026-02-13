# Steganography Tools

Simple CLI tools for steganography analysis.

## Tools

### lsb-extract.py
Extract LSB (Least Significant Bit) data from images.
```bash
python lsb-extract.py image.png
python lsb-extract.py image.png output.bin
```

**Note**: Requires Pillow library (optional dependency).

### metadata.sh
Extract and display image metadata.
```bash
./metadata.sh image.jpg
```

## Common Patterns
- LSB steganography in images
- Hidden data in metadata
- Audio steganography
- Text encoding in images
- File appending
