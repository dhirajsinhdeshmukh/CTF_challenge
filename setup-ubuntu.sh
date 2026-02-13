#!/bin/bash
# Setup script for Ubuntu/Debian-based systems

set -e

echo "================================"
echo "CTF Toolkit Setup for Ubuntu"
echo "================================"

# Update package list
echo "[+] Updating package list..."
sudo apt-get update

# Install core tools
echo "[+] Installing core tools..."
sudo apt-get install -y \
    build-essential \
    git \
    curl \
    wget \
    nmap \
    netcat \
    binutils \
    gdb \
    strace \
    ltrace \
    file \
    strings \
    xxd \
    hexedit \
    vim \
    python3 \
    python3-pip

# Install optional tools
echo "[+] Installing optional CTF tools..."
sudo apt-get install -y \
    wireshark \
    tshark \
    tcpdump \
    exiftool \
    foremost \
    steghide \
    john \
    hashcat \
    sqlmap \
    nikto \
    gobuster \
    hydra || echo "Some optional tools not available"

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
