#!/usr/bin/env python3
"""LSB steganography extractor"""

import sys

def extract_lsb(image_path, output_path=None):
    """Extract LSB data from image"""
    try:
        from PIL import Image
    except ImportError:
        print("Error: PIL/Pillow required. Install with: pip install pillow", file=sys.stderr)
        sys.exit(1)
    
    try:
        img = Image.open(image_path)
        pixels = list(img.getdata())
        
        # Extract LSBs
        bits = []
        for pixel in pixels:
            if isinstance(pixel, int):
                bits.append(pixel & 1)
            else:
                for val in pixel[:3]:  # RGB only
                    bits.append(val & 1)
        
        # Convert bits to bytes
        data = bytearray()
        for i in range(0, len(bits), 8):
            byte = 0
            for j in range(8):
                if i + j < len(bits):
                    byte = (byte << 1) | bits[i + j]
            data.append(byte)
        
        # Try to find printable data
        text = data.decode('latin-1', errors='ignore')
        printable = ''.join(c for c in text if c.isprintable())
        
        if output_path:
            with open(output_path, 'wb') as f:
                f.write(data)
            print(f"LSB data saved to {output_path}")
        
        # Show first 500 chars of printable data
        if printable:
            print("\nPrintable LSB data (first 500 chars):")
            print(printable[:500])
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python lsb-extract.py <image> [output]")
        sys.exit(1)
    
    output = sys.argv[2] if len(sys.argv) > 2 else None
    extract_lsb(sys.argv[1], output)
