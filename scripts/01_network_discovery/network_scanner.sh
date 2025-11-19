#!/bin/bash
# Automated network scanning script for competition
# Scans specified subnet and identifies active hosts

SUBNET="192.168.0"
OUTPUT_FILE="discovered_hosts.txt"

echo "═══════════════════════════════════════════════"
echo "  Network Scanner - Competition Tool"
echo "═══════════════════════════════════════════════"
echo ""

echo "[+] Scanning subnet: ${SUBNET}.0/24"
echo "[+] Output file: ${OUTPUT_FILE}"
echo ""

# Clear previous results
> ${OUTPUT_FILE}

# Scan using ARP
echo "[*] Running ARP scan..."
arp -a | grep ${SUBNET} | tee -a ${OUTPUT_FILE}

echo ""
echo "[*] Pinging hosts to populate ARP cache..."

# Ping sweep
for i in {1..254}; do
    ip="${SUBNET}.${i}"
    ping -c 1 -W 1 ${ip} > /dev/null 2>&1 &
done

# Wait for ping sweep to complete
wait

echo "[*] Updated ARP scan results:"
arp -a | grep ${SUBNET} | tee ${OUTPUT_FILE}

echo ""
echo "[✓] Scan complete! Results saved to: ${OUTPUT_FILE}"
echo "═══════════════════════════════════════════════"
