#!/bin/bash


## ref : https://github.com/Wh0am123/MCP-Kali-Server#example-solving-my-web-ctf-challenge-in-ramadanctf
## ref : extension : MCP Kali Workspace
## future : https://marketplace.visualstudio.com/items?itemName=sudoecho.anyrag-pilot



set -e

echo "[+] Stopping any running MCP server..."
pkill -f kali-server-mcp 2>/dev/null || true
pkill -f mcp-server 2>/dev/null || true

echo "[+] Removing mcp-kali-server package..."
sudo apt purge -y mcp-kali-server || true

echo "[+] Autoremoving unused dependencies..."
sudo apt autoremove -y

echo "[+] Removing systemd service (if present)..."
sudo systemctl disable kali-server-mcp 2>/dev/null || true
sudo rm -f /etc/systemd/system/kali-server-mcp.service 2>/dev/null || true
sudo systemctl daemon-reload 2>/dev/null || true

echo "[+] Removing user cache for VS Code MCP extension..."
rm -rf ~/.cache/mcp-kali-workspace

echo "[+] Removing workspace MCP configuration (if in current directory)..."
rm -rf .mcp-kali
rm -f .vscode/mcp.json

echo "[+] Cleanup complete."
