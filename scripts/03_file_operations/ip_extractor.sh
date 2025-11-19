#!/bin/bash
# IP Address Extractor
# Extracts and saves IP configuration to file

echo "═══════════════════════════════════════════════"
echo "  IP Address Extractor"
echo "═══════════════════════════════════════════════"
echo ""

OUTPUT_FILE="IP_Address.txt"
DETAILED_OUTPUT="IP_Details.txt"

# Function to extract IP on macOS/Linux
extract_ip_unix() {
    echo "[*] Extracting IP address (Unix/macOS)..."
    
    # Get primary interface IP
    if command -v ifconfig &> /dev/null; then
        IP_ADDR=$(ifconfig | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}' | head -1)
    elif command -v ip &> /dev/null; then
        IP_ADDR=$(ip addr show | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}' | cut -d/ -f1 | head -1)
    fi
    
    if [ -z "$IP_ADDR" ]; then
        echo "[!] Could not determine IP address"
        return 1
    fi
    
    echo "[✓] IP Address: $IP_ADDR"
    
    # Save to file
    echo "$IP_ADDR" > "$OUTPUT_FILE"
    echo "[✓] Saved to: $OUTPUT_FILE"
    
    # Save detailed info
    echo "IP ADDRESS INFORMATION" > "$DETAILED_OUTPUT"
    echo "======================" >> "$DETAILED_OUTPUT"
    echo "" >> "$DETAILED_OUTPUT"
    echo "Primary IP: $IP_ADDR" >> "$DETAILED_OUTPUT"
    echo "Timestamp: $(date)" >> "$DETAILED_OUTPUT"
    echo "" >> "$DETAILED_OUTPUT"
    echo "Full Network Configuration:" >> "$DETAILED_OUTPUT"
    echo "--------------------------" >> "$DETAILED_OUTPUT"
    
    if command -v ifconfig &> /dev/null; then
        ifconfig >> "$DETAILED_OUTPUT"
    elif command -v ip &> /dev/null; then
        ip addr show >> "$DETAILED_OUTPUT"
    fi
    
    echo "[✓] Detailed info saved to: $DETAILED_OUTPUT"
}

# Function to extract IP on Windows (via Git Bash or WSL)
extract_ip_windows() {
    echo "[*] Extracting IP address (Windows)..."
    
    # Run ipconfig and extract IPv4
    IP_ADDR=$(ipconfig | grep -i "IPv4" | head -1 | awk '{print $NF}')
    
    if [ -z "$IP_ADDR" ]; then
        echo "[!] Could not determine IP address"
        return 1
    fi
    
    echo "[✓] IP Address: $IP_ADDR"
    
    # Save to file
    echo "$IP_ADDR" > "$OUTPUT_FILE"
    echo "[✓] Saved to: $OUTPUT_FILE"
    
    # Save detailed info
    echo "IP ADDRESS INFORMATION" > "$DETAILED_OUTPUT"
    echo "======================" >> "$DETAILED_OUTPUT"
    echo "" >> "$DETAILED_OUTPUT"
    echo "IPv4 Address: $IP_ADDR" >> "$DETAILED_OUTPUT"
    echo "Timestamp: $(date)" >> "$DETAILED_OUTPUT"
    echo "" >> "$DETAILED_OUTPUT"
    echo "Full Network Configuration:" >> "$DETAILED_OUTPUT"
    echo "--------------------------" >> "$DETAILED_OUTPUT"
    ipconfig >> "$DETAILED_OUTPUT"
    
    echo "[✓] Detailed info saved to: $DETAILED_OUTPUT"
}

# Detect OS and run appropriate function
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    extract_ip_windows
else
    extract_ip_unix
fi

echo ""
echo "═══════════════════════════════════════════════"
echo "Files created:"
echo "  - $OUTPUT_FILE (IP only)"
echo "  - $DETAILED_OUTPUT (Full details)"
echo "═══════════════════════════════════════════════"
'''

# ═══════════════════════════════════════════════════════════════════════
# SAVE INSTRUCTIONS
# ═══════════════════════════════════════════════════════════════════════

def print_save_instructions():
    """Print instructions for saving files"""
    print("""
╔═══════════════════════════════════════════════════════════════════════╗
║                    FILE SAVE INSTRUCTIONS                             ║
╚═══════════════════════════════════════════════════════════════════════╝

This file contains 3 scripts for the File Operations category.
To save them to your repository:

1. CREATE DIRECTORY:
   mkdir -p scripts/03_file_operations

2. SAVE EACH SCRIPT:

   Script 1: folder_renamer.py
   ─────────────────────────────
   Copy the content from FOLDER_RENAMER_PY variable and save to:
   scripts/03_file_operations/folder_renamer.py
   
   Then make it executable:
   chmod +x scripts/03_file_operations/folder_renamer.py

   Script 2: file_searcher.py
   ─────────────────────────────
   Copy the content from FILE_SEARCHER_PY variable and save to:
   scripts/03_file_operations/file_searcher.py
   
   Then make it executable:
   chmod +x scripts/03_file_operations/file_searcher.py

   Script 3: ip_extractor.sh
   ─────────────────────────────
   Copy the content from IP_EXTRACTOR_SH variable and save to:
   scripts/03_file_operations/ip_extractor.sh
   
   Then make it executable:
   chmod +x scripts/03_file_operations/ip_extractor.sh

3. TEST THE SCRIPTS:
   
   # Test folder renamer
   python3 scripts/03_file_operations/folder_renamer.py --help
   
   # Test file searcher
   python3 scripts/03_file_operations/file_searcher.py name "*.txt"
   
   # Test IP extractor
   bash scripts/03_file_operations/ip_extractor.sh

═══════════════════════════════════════════════════════════════════════

Next Parts Coming:
  ✓ Part 1: Network Discovery (COMPLETE)
  ✓ Part 2: Remote Access (COMPLETE)
  ✓ Part 3: File Operations (THIS FILE)
  ⏳ Part 4: Password Cracking
  ⏳ Part 5: Network Mapping
  ⏳ Part 6: Utilities
  ⏳ Part 7: Configuration Files
  ⏳ Part 8: Setup & Documentation

═══════════════════════════════════════════════════════════════════════
    """)

if __name__ == "__main__":
    print_save_instructions()
