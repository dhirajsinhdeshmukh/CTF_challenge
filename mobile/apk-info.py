#!/usr/bin/env python3
"""Simple APK analyzer"""

import sys
import zipfile
import os

def analyze_apk(apk_path):
    """Analyze APK file structure"""
    if not os.path.exists(apk_path):
        print(f"Error: {apk_path} not found", file=sys.stderr)
        sys.exit(1)
    
    try:
        with zipfile.ZipFile(apk_path, 'r') as apk:
            print(f"\nAPK Analysis: {apk_path}")
            print("-" * 50)
            print(f"Total files: {len(apk.namelist())}")
            
            print("\nKey files:")
            key_files = ['AndroidManifest.xml', 'classes.dex', 'resources.arsc']
            for name in apk.namelist():
                if any(key in name for key in key_files):
                    print(f"  {name}")
            
            print("\nAssets:")
            for name in apk.namelist():
                if name.startswith('assets/'):
                    print(f"  {name}")
            
            print("\nLibraries:")
            for name in apk.namelist():
                if name.startswith('lib/') and name.endswith('.so'):
                    print(f"  {name}")
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python apk-info.py <apk-file>")
        sys.exit(1)
    analyze_apk(sys.argv[1])
