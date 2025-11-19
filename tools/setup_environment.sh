!/bin/bash
# Setup script for competition environment
# Run this script to set up your system for the competition

echo "╔═══════════════════════════════════════════════════════════╗"
echo "║     Competition Environment Setup                         ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""

# Detect OS
if [[ "$OSTYPE" == "darwin"* ]]; then
    OS="macOS"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS="Linux"
else
    echo "[!] Unsupported operating system: $OSTYPE"
    exit 1
fi

echo "[*] Detected OS: $OS"
echo ""

# Create directory structure
echo "[*] Creating directory structure..."
mkdir -p scripts/{01_network_discovery,02_remote_access,03_file_operations,04_password_cracking,05_network_mapping,06_utilities}
mkdir -p configs/wordlists
mkdir -p tools
mkdir -p documentation
mkdir -p results/screenshots
mkdir -p notes

echo "[✓] Directory structure created"
echo ""

# Check for required tools
echo "[*] Checking for required tools..."

check_tool() {
    if command -v $1 &> /dev/null; then
        echo "  ✓ $1 found"
        return 0
    else
        echo "  ✗ $1 not found"
        return 1
    fi
}

# Essential tools
check_tool python3
check_tool bash
check_tool ping
check_tool arp

# Optional but recommended
echo ""
echo "[*] Checking optional tools..."
check_tool john || echo "    Install with: brew install john-jumbo"
check_tool 7z || echo "    Install with: brew install p7zip"

echo ""
echo "[*] Checking Python packages..."

python3 -c "import json" 2>/dev/null && echo "  ✓ json" || echo "  ✗ json"
python3 -c "import csv" 2>/dev/null && echo "  ✓ csv" || echo "  ✗ csv"

echo ""
echo "═══════════════════════════════════════════════════════════"
echo "Setup complete!"
echo ""
echo "Next steps:"
echo "1. Run: bash tools/install_dependencies.sh"
echo "2. Review: configs/network_config.yaml"
echo "3. Start competition with your scripts in scripts/ directory"
echo "═══════════════════════════════════════════════════════════"
