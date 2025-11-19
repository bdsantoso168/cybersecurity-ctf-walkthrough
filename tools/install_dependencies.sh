!/bin/bash
# Install all required dependencies for competition tools

echo "╔═══════════════════════════════════════════════════════════╗"
echo "║     Competition Tools - Dependency Installer              ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""

# Check if running on macOS
if [[ "$OSTYPE" != "darwin"* ]]; then
    echo "[!] This script is designed for macOS"
    echo "[*] For Linux, please install packages manually"
    exit 1
fi

echo "[*] Installing dependencies for macOS..."
echo ""

# Check if Homebrew is installed
if ! command -v brew &> /dev/null; then
    echo "[!] Homebrew not found. Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    
    if [ $? -eq 0 ]; then
        echo "[✓] Homebrew installed successfully"
    else
        echo "[!] Failed to install Homebrew"
        exit 1
    fi
else
    echo "[✓] Homebrew already installed"
fi

echo ""
echo "[*] Updating Homebrew..."
brew update

echo ""
echo "[*] Installing required packages..."

# Install packages
packages=(
    "p7zip"           # 7-Zip for archive handling
    "john-jumbo"      # John the Ripper for password cracking
    "wget"            # Download utility
    "nmap"            # Network scanner (optional)
)

for package in "${packages[@]}"; do
    echo ""
    echo "[*] Installing $package..."
    
    if brew list "$package" &>/dev/null; then
        echo "  [✓] $package already installed"
    else
        brew install "$package"
        
        if [ $? -eq 0 ]; then
            echo "  [✓] $package installed successfully"
        else
            echo "  [!] Failed to install $package"
        fi
    fi
done

echo ""
echo "[*] Installing Python packages..."

# Python packages (if needed)
pip3 install --upgrade pip 2>/dev/null

echo ""
echo "═══════════════════════════════════════════════════════════"
echo "Installation complete!"
echo ""
echo "Installed tools:"
echo "  ✓ p7zip (7z command)"
echo "  ✓ john-jumbo (John the Ripper)"
echo "  ✓ wget"
echo "  ✓ nmap (optional)"
echo ""
echo "Verify installation:"
echo "  7z --help"
echo "  john --help"
echo "  nmap --version"
echo "═══════════════════════════════════════════════════════════"
