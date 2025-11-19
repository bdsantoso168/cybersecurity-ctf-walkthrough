#!/bin/bash
# John the Ripper Automation Script
# Automates password cracking with multiple strategies

echo "═══════════════════════════════════════════════"
echo "  John the Ripper - Automated Cracking"
echo "═══════════════════════════════════════════════"
echo ""

# Check if john is installed
if ! command -v john &> /dev/null; then
    echo "[!] John the Ripper not found!"
    echo "[*] Install with: brew install john-jumbo"
    exit 1
fi

# Check arguments
if [ $# -eq 0 ]; then
    echo "Usage: $0 <hash_file> [wordlist]"
    echo ""
    echo "Example:"
    echo "  $0 hash.txt"
    echo "  $0 hash.txt custom_wordlist.txt"
    echo ""
    echo "This script will try multiple cracking strategies:"
    echo "  1. Default mode (fast)"
    echo "  2. Custom wordlist (if provided)"
    echo "  3. System dictionary"
    echo "  4. Incremental mode (slower)"
    exit 1
fi

HASH_FILE="$1"
CUSTOM_WORDLIST="$2"

# Check if hash file exists
if [ ! -f "$HASH_FILE" ]; then
    echo "[!] Error: Hash file not found: $HASH_FILE"
    exit 1
fi

echo "[*] Hash file: $HASH_FILE"
if [ -n "$CUSTOM_WORDLIST" ]; then
    echo "[*] Custom wordlist: $CUSTOM_WORDLIST"
fi
echo ""

# Function to check if password is cracked
check_cracked() {
    john --show "$HASH_FILE" 2>/dev/null | grep -q "1 password hash cracked"
    return $?
}

# Function to display cracked password
show_cracked() {
    echo ""
    echo "╔═══════════════════════════════════════════════╗"
    echo "║          🎉 PASSWORD CRACKED! 🎉              ║"
    echo "╚═══════════════════════════════════════════════╝"
    echo ""
    john --show "$HASH_FILE"
    echo ""
}

# Strategy 1: Try default mode (quick)
echo "═══════════════════════════════════════════════"
echo "  Strategy 1: Default Mode (Quick)"
echo "═══════════════════════════════════════════════"
echo ""
timeout 30 john "$HASH_FILE" 2>&1 | head -20

if check_cracked; then
    show_cracked
    exit 0
fi

# Strategy 2: Try custom wordlist if provided
if [ -n "$CUSTOM_WORDLIST" ] && [ -f "$CUSTOM_WORDLIST" ]; then
    echo ""
    echo "═══════════════════════════════════════════════"
    echo "  Strategy 2: Custom Wordlist"
    echo "═══════════════════════════════════════════════"
    echo ""
    
    WORDLIST_SIZE=$(wc -l < "$CUSTOM_WORDLIST")
    echo "[*] Wordlist size: $WORDLIST_SIZE passwords"
    echo "[*] This may take a while..."
    echo ""
    
    john --wordlist="$CUSTOM_WORDLIST" "$HASH_FILE"
    
    if check_cracked; then
        show_cracked
        exit 0
    fi
fi

# Strategy 3: Try system dictionary
echo ""
echo "═══════════════════════════════════════════════"
echo "  Strategy 3: System Dictionary"
echo "═══════════════════════════════════════════════"
echo ""

if [ -f "/usr/share/dict/words" ]; then
    echo "[*] Using /usr/share/dict/words"
    timeout 60 john --wordlist=/usr/share/dict/words "$HASH_FILE"
else
    echo "[!] System dictionary not found, skipping..."
fi

if check_cracked; then
    show_cracked
    exit 0
fi

# Strategy 4: Common passwords
echo ""
echo "═══════════════════════════════════════════════"
echo "  Strategy 4: Common Passwords"
echo "═══════════════════════════════════════════════"
echo ""

# Create temporary common password list
TMP_WORDLIST=$(mktemp)
cat > "$TMP_WORDLIST" << 'EOF'
password
Password
PASSWORD
123456
12345678
qwerty
admin
letmein
welcome
monkey
dragon
sunshine
princess
password1
password123
abc123
iloveyou
password!
admin123
root
EOF

echo "[*] Trying common passwords..."
john --wordlist="$TMP_WORDLIST" "$HASH_FILE"
rm "$TMP_WORDLIST"

if check_cracked; then
    show_cracked
    exit 0
fi

# Strategy 5: Incremental mode (brute force)
echo ""
echo "═══════════════════════════════════════════════"
echo "  Strategy 5: Incremental Mode (Brute Force)"
echo "═══════════════════════════════════════════════"
echo ""
echo "[!] WARNING: This can take a very long time!"
echo "[*] Starting brute force attack (Ctrl+C to stop)..."
echo "[*] Will run for maximum 5 minutes..."
echo ""

timeout 300 john --incremental "$HASH_FILE"

if check_cracked; then
    show_cracked
    exit 0
fi

# Check final status
echo ""
echo "═══════════════════════════════════════════════"
echo "  FINAL STATUS"
echo "═══════════════════════════════════════════════"
echo ""

if check_cracked; then
    show_cracked
else
    echo "[!] Password not cracked yet"
    echo ""
    echo "You can:"
    echo "1. Try a different wordlist"
    echo "2. Let incremental mode run longer (remove timeout)"
    echo "3. Create a more targeted wordlist"
    echo ""
    echo "Session saved. Resume with:"
    echo "  john --restore"
fi

echo ""
echo "═══════════════════════════════════════════════"
