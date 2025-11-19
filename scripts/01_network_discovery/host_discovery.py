#!/usr/bin/env python3
"""
Host Discovery Tool
Discovers active hosts on the network using multiple methods
"""

import subprocess
import re
import json
from datetime import datetime
from typing import List, Dict

class HostDiscovery:
    def __init__(self, subnet: str = "192.168.0"):
        self.subnet = subnet
        self.discovered_hosts = []
    
    def arp_scan(self) -> List[Dict]:
        """Scan network using ARP cache"""
        print("[*] Running ARP scan...")
        
        try:
            result = subprocess.run(
                ["arp", "-a"],
                capture_output=True,
                text=True
            )
            
            hosts = []
            for line in result.stdout.split('\n'):
                if self.subnet in line:
                    # Parse ARP output
                    match = re.search(r'(\d+\.\d+\.\d+\.\d+).*?((?:[0-9a-f]{1,2}[:-]){5}[0-9a-f]{1,2})', line, re.IGNORECASE)
                    if match:
                        ip = match.group(1)
                        mac = match.group(2)
                        
                        # Try to get hostname
                        hostname = self.get_hostname(line)
                        
                        hosts.append({
                            "ip": ip,
                            "mac": mac,
                            "hostname": hostname,
                            "timestamp": datetime.now().isoformat()
                        })
            
            self.discovered_hosts = hosts
            return hosts
        
        except Exception as e:
            print(f"[!] Error during ARP scan: {e}")
            return []
    
    def get_hostname(self, arp_line: str) -> str:
        """Extract hostname from ARP line if available"""
        match = re.search(r'\((.*?)\)', arp_line)
        if match:
            return match.group(1)
        return "Unknown"
    
    def ping_sweep(self, start: int = 1, end: int = 254):
        """Perform ping sweep on subnet"""
        print(f"[*] Running ping sweep on {self.subnet}.{start}-{end}...")
        
        for i in range(start, end + 1):
            ip = f"{self.subnet}.{i}"
            try:
                subprocess.run(
                    ["ping", "-c", "1", "-W", "1", ip],
                    capture_output=True,
                    timeout=2
                )
            except:
                pass
        
        print("[*] Ping sweep complete. Run ARP scan to see results.")
    
    def export_json(self, filename: str = "discovered_hosts.json"):
        """Export discovered hosts to JSON"""
        with open(filename, 'w') as f:
            json.dump(self.discovered_hosts, f, indent=4)
        print(f"[✓] Results exported to: {filename}")
    
    def print_results(self):
        """Print discovered hosts in table format"""
        if not self.discovered_hosts:
            print("[!] No hosts discovered yet. Run a scan first.")
            return
        
        print("\n" + "="*70)
        print("  DISCOVERED HOSTS")
        print("="*70)
        print(f"{'IP Address':<18} {'MAC Address':<20} {'Hostname':<30}")
        print("-"*70)
        
        for host in self.discovered_hosts:
            print(f"{host['ip']:<18} {host['mac']:<20} {host['hostname']:<30}")
        
        print("="*70)
        print(f"Total hosts discovered: {len(self.discovered_hosts)}\n")

def main():
    print("""
╔═══════════════════════════════════════════════════════════╗
║          HOST DISCOVERY TOOL - Competition Edition        ║
╚═══════════════════════════════════════════════════════════╝
    """)
    
    scanner = HostDiscovery(subnet="192.168.0")
    
    # Perform ping sweep first to populate ARP cache
    scanner.ping_sweep()
    
    # Run ARP scan
    hosts = scanner.arp_scan()
    
    # Display results
    scanner.print_results()
    
    # Export to JSON
    scanner.export_json()

if __name__ == "__main__":
    main()
