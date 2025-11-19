#!/bin/bash
# Hash Extractor for 7z Files
# Extracts password hashes from encrypted archives

echo "═══════════════════════════════════════════════"
echo "  Hash Extractor for 7z Files"
echo "═══════════════════════════════════════════════"
echo ""

# Check if 7z2john is installed
if ! command -v 7z2john &> /dev/null; then
    echo "[!] 7z2john not found!"
    echo "[*] Install with: brew install john-jumbo"
    exit 1
fi

# Check if input file provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <7z_file> [output_file]"
    echo ""
    echo "Example:"
    echo "  $0 Security.7z"
    echo "  $0 Cyber.7z cyber_hash.txt"
    exit 1
fi

INPUT_FILE="$1"
OUTPUT_FILE="${2:-hash.txt}"

# Check if input file exists
if [ ! -f "$INPUT_FILE" ]; then
    echo "[!] Error: File not found: $INPUT_FILE"
    exit 1
fi

echo "[*] Input file:  $INPUT_FILE"
echo "[*] Output file: $OUTPUT_FILE"
echo ""

# Extract hash
echo "[*] Extracting hash from 7z file..."
if 7z2john "$INPUT_FILE" > "$OUTPUT_FILE" 2>&1; then
    echo "[✓] Hash extracted successfully!"
    echo ""
    
    # Display hash
    echo "─────────────────────────────────────────────"
    cat "$OUTPUT_FILE"
    echo "─────────────────────────────────────────────"
    echo ""
    
    # Get file size
    FILE_SIZE=$(wc -c < "$OUTPUT_FILE")
    echo "[✓] Hash saved to: $OUTPUT_FILE ($FILE_SIZE bytes)"
    echo ""
    
    # Next steps
    echo "Next steps:"
    echo "1. Crack with dictionary:"
    echo "   john --wordlist=wordlist.txt $OUTPUT_FILE"
    echo ""
    echo "2. Crack with default mode:"
    echo "   john $OUTPUT_FILE"
    echo ""
    echo "3. Show cracked password:"
    echo "   john --show $OUTPUT_FILE"
    
else
    echo "[!] Error extracting hash"
    exit 1
fi

echo ""
echo "═══════════════════════════════════════════════"
