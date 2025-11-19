#!/bin/bash
# Real-time ARP cache monitoring

SUBNET="192.168.0"
INTERVAL=5

echo "═══════════════════════════════════════════════"
echo "  ARP Cache Monitor"
echo "═══════════════════════════════════════════════"
echo ""
echo "Monitoring subnet: ${SUBNET}.0/24"
echo "Update interval: ${INTERVAL} seconds"
echo "Press Ctrl+C to stop"
echo ""

while true; do
    clear
    echo "═══════════════════════════════════════════════"
    echo "  ARP Cache - $(date '+%Y-%m-%d %H:%M:%S')"
    echo "═══════════════════════════════════════════════"
    echo ""
    arp -a | grep ${SUBNET}
    echo ""
    echo "Next update in ${INTERVAL} seconds..."
    sleep ${INTERVAL}
done
