#!/bin/bash
# Setup script for Kali Linux

set -e

echo "================================"
echo "CTF Toolkit Setup for Kali"
echo "================================"

# Update package list
echo "[+] Updating package list..."
sudo apt-get update

# Most tools are pre-installed on Kali, but ensure core ones exist
echo "[+] Ensuring core tools are installed..."
sudo apt-get install -y \
    build-essential \
    git \
    curl \
    nmap \
    netcat-traditional \
    binutils \
    gdb \
    strace \
    ltrace \
    python3 \
    python3-pip

# Install tools that might not be on Kali by default
echo "[+] Installing additional tools..."
sudo apt-get install -y \
    exiftool \
    foremost \
    steghide || echo "Some tools already installed"

# Install uv (fast Python package installer)
echo "[+] Installing uv..."
curl -LsSf https://astral.sh/uv/install.sh | sh

# Add uv to PATH for current session
export PATH="$HOME/.cargo/bin:$PATH"

# Create Python virtual environment with uv
echo "[+] Creating Python virtual environment..."
cd "$(dirname "$0")"
uv venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install minimal Python dependencies
echo "[+] Installing Python dependencies..."
uv pip install --quiet \
    requests \
    pycryptodome

echo ""
echo "================================"
echo "Setup Complete!"
echo "================================"
echo ""
echo "To activate the Python environment, run:"
echo "  source .venv/bin/activate"
echo ""
echo "Make shell scripts executable with:"
echo "  chmod +x */*.sh"
echo ""
