#!/bin/bash
# Automated RDP Connection Helper
# Simplifies Remote Desktop connections

echo "═══════════════════════════════════════════════"
echo "  RDP Connection Helper"
echo "═══════════════════════════════════════════════"
echo ""

# Function to test connectivity
test_connection() {
    local ip=$1
    echo "[*] Testing connectivity to ${ip}..."
    
    if ping -c 2 -W 2 ${ip} > /dev/null 2>&1; then
        echo "[✓] Host is reachable"
        return 0
    else
        echo "[!] Host is not reachable"
        return 1
    fi
}

# Function to check RDP port
check_rdp_port() {
    local ip=$1
    local port=3389
    
    echo "[*] Checking if RDP port (${port}) is open..."
    
    if nc -zv ${ip} ${port} 2>&1 | grep -q "succeeded"; then
        echo "[✓] RDP port is open"
        return 0
    else
        echo "[!] RDP port appears to be closed"
        return 1
    fi
}

# Main script
if [ $# -eq 0 ]; then
    echo "Usage: $0 <IP_ADDRESS> [USERNAME]"
    echo ""
    echo "Example:"
    echo "  $0 192.168.0.154"
    echo "  $0 192.168.0.154 administrator"
    exit 1
fi

TARGET_IP=$1
USERNAME=${2:-"user"}

echo "Target IP: ${TARGET_IP}"
echo "Username:  ${USERNAME}"
echo ""

# Test connection
if test_connection ${TARGET_IP}; then
    # Check RDP port (requires netcat)
    # check_rdp_port ${TARGET_IP}
    
    echo ""
    echo "[*] Opening Microsoft Remote Desktop..."
    echo ""
    echo "Connection Details:"
    echo "  PC Name:  ${TARGET_IP}"
    echo "  Username: ${USERNAME}"
    echo ""
    echo "Note: You will be prompted for password"
    echo "═══════════════════════════════════════════════"
    
    # On macOS, you would typically open RDP through GUI
    # This is a placeholder for documentation
    echo ""
    echo "To connect via Microsoft Remote Desktop:"
    echo "1. Open Microsoft Remote Desktop"
    echo "2. Click 'Add PC' or '+'"
    echo "3. Enter PC name: ${TARGET_IP}"
    echo "4. Enter username: ${USERNAME}"
    echo "5. Click 'Connect'"
fi
