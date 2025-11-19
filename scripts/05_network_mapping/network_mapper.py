#!/usr/bin/env python3
"""
Network Mapper
Creates comprehensive network topology maps from scan data
"""

import subprocess
import re
import json
from datetime import datetime
from typing import List, Dict

class NetworkMapper:
    def __init__(self, subnet: str = "192.168.0"):
        self.subnet = subnet
        self.devices = []
    
    def arp_scan(self) -> List[Dict]:
        """Perform ARP scan to discover devices"""
        print(f"[*] Scanning subnet: {self.subnet}.0/24")
        
        try:
            # Run ARP command
            result = subprocess.run(
                ["arp", "-a"],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            devices = []
            
            for line in result.stdout.split('\\n'):
                if self.subnet in line:
                    # Parse line for IP and MAC
                    ip_match = re.search(r'(\\d+\\.\\d+\\.\\d+\\.\\d+)', line)
                    mac_match = re.search(r'([0-9a-fA-F]{1,2}[:-]){5}[0-9a-fA-F]{1,2}', line)
                    
                    if ip_match:
                        ip = ip_match.group(1)
                        mac = mac_match.group(0) if mac_match else "Unknown"
                        
                        # Try to extract hostname
                        hostname_match = re.search(r'\\(([^)]+)\\)', line)
                        hostname = hostname_match.group(1) if hostname_match else self.reverse_dns_lookup(ip)
                        
                        device = {
                            "ip": ip,
                            "mac": mac,
                            "hostname": hostname,
                            "os": "Unknown",
                            "status": "Up",
                            "open_ports": [],
                            "vendor": self.lookup_vendor(mac)
                        }
                        
                        devices.append(device)
            
            self.devices = devices
            return devices
        
        except Exception as e:
            print(f"[!] Error during ARP scan: {e}")
            return []
    
    def reverse_dns_lookup(self, ip: str) -> str:
        """Attempt reverse DNS lookup for hostname"""
        try:
            result = subprocess.run(
                ["host", ip],
                capture_output=True,
                text=True,
                timeout=2
            )
            
            if "domain name pointer" in result.stdout:
                hostname = result.stdout.split("pointer")[1].strip().rstrip('.')
                return hostname
        except:
            pass
        
        return "Unknown"
    
    def lookup_vendor(self, mac: str) -> str:
        """Look up vendor from MAC address OUI"""
        oui_database = {
            "00:0c:29": "VMware",
            "00:50:56": "VMware",
            "00:1c:42": "Parallels",
            "08:00:27": "VirtualBox",
            "74:da:38": "Micro-Star International",
            "00:1b:21": "Intel",
            "00:1a:a0": "Dell",
        }
        
        if mac and mac != "Unknown":
            # Get first 3 octets (OUI)
            oui = ':'.join(mac.split(':')[:3]).lower()
            return oui_database.get(oui, "Unknown")
        
        return "Unknown"
    
    def ping_sweep(self):
        """Perform ping sweep to populate ARP cache"""
        print(f"[*] Performing ping sweep on {self.subnet}.0/24...")
        
        processes = []
        for i in range(1, 255):
            ip = f"{self.subnet}.{i}"
            proc = subprocess.Popen(
                ["ping", "-c", "1", "-W", "1", ip],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            processes.append(proc)
        
        # Wait for all pings to complete
        for proc in processes:
            proc.wait()
        
        print("[✓] Ping sweep complete")
    
    def detect_os(self, device: Dict) -> str:
        """Attempt to detect OS (basic detection)"""
        # This is a simplified OS detection
        # In real scenarios, you'd use tools like nmap
        
        vendor = device.get('vendor', '').lower()
        
        if 'vmware' in vendor or 'virtualbox' in vendor or 'parallels' in vendor:
            return "Virtual Machine"
        
        # Default assumption for competition environment
        return "Windows 10"
    
    def enrich_device_data(self):
        """Enrich device data with additional information"""
        print("[*] Enriching device data...")
        
        for device in self.devices:
            # Detect OS
            device['os'] = self.detect_os(device)
            
            # Add scan timestamp
            device['scan_time'] = datetime.now().isoformat()
        
        print(f"[✓] Enriched {len(self.devices)} device(s)")
    
    def export_json(self, filename: str = "network_map.json"):
        """Export network map to JSON"""
        data = {
            "scan_date": datetime.now().isoformat(),
            "subnet": self.subnet + ".0/24",
            "total_devices": len(self.devices),
            "devices": self.devices
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        
        print(f"[✓] Network map exported to: {filename}")
    
    def export_text(self, filename: str = "network_map.txt"):
        """Export network map to text format"""
        with open(filename, 'w') as f:
            f.write("NETWORK TOPOLOGY MAP\\n")
            f.write("="*80 + "\\n")
            f.write(f"Scan Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\\n")
            f.write(f"Subnet: {self.subnet}.0/24\\n")
            f.write(f"Total Devices: {len(self.devices)}\\n")
            f.write("="*80 + "\\n\\n")
            
            for i, device in enumerate(self.devices, 1):
                f.write(f"Device {i}:\\n")
                f.write(f"  IP Address:  {device['ip']}\\n")
                f.write(f"  MAC Address: {device['mac']}\\n")
                f.write(f"  Hostname:    {device['hostname']}\\n")
                f.write(f"  OS:          {device['os']}\\n")
                f.write(f"  Vendor:      {device['vendor']}\\n")
                f.write(f"  Status:      {device['status']}\\n")
                f.write("-"*80 + "\\n")
        
        print(f"[✓] Network map exported to: {filename}")
    
    def print_summary(self):
        """Print network map summary"""
        print("\\n" + "="*80)
        print("  NETWORK MAP SUMMARY")
        print("="*80)
        print(f"Subnet:        {self.subnet}.0/24")
        print(f"Scan Time:     {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Total Devices: {len(self.devices)}")
        print("="*80)
        print(f"{'#':<4} {'IP Address':<16} {'MAC Address':<20} {'Hostname':<25} {'OS':<15}")
        print("-"*80)
        
        for i, device in enumerate(self.devices, 1):
            print(f"{i:<4} {device['ip']:<16} {device['mac']:<20} {device['hostname']:<25} {device['os']:<15}")
        
        print("="*80 + "\\n")

def main():
    print("""
╔═══════════════════════════════════════════════════════════╗
║          NETWORK MAPPER - Competition Tool                ║
╚═══════════════════════════════════════════════════════════╝
    """)
    
    import sys
    
    subnet = sys.argv[1] if len(sys.argv) > 1 else "192.168.0"
    
    mapper = NetworkMapper(subnet)
    
    # Perform ping sweep to populate ARP cache
    mapper.ping_sweep()
    
    # Scan network
    devices = mapper.arp_scan()
    
    if not devices:
        print("[!] No devices found on network")
        return
    
    # Enrich data
    mapper.enrich_device_data()
    
    # Print summary
    mapper.print_summary()
    
    # Export to multiple formats
    mapper.export_json()
    mapper.export_text()
    
    print("[✓] Network mapping complete!")

if __name__ == "__main__":
    main()
