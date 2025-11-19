#!/usr/bin/env python3
"""
MAC Address Vendor Lookup
Identifies device manufacturers from MAC addresses
"""
 
import re
import requests
import json
from typing import Optional

class MACLookup:
    def __init__(self):
        # Common OUI (Organizationally Unique Identifier) database
        self.oui_database = {
            "00:0c:29": "VMware, Inc.",
            "00:50:56": "VMware, Inc.",
            "00:1c:42": "Parallels, Inc.",
            "08:00:27": "Oracle VirtualBox",
            "52:54:00": "QEMU Virtual NIC",
            "74:da:38": "Micro-Star International",
            "00:1b:21": "Intel Corporation",
            "00:1a:a0": "Dell Inc.",
            "00:23:ae": "PEGATRON CORPORATION",
        }
    
    def normalize_mac(self, mac: str) -> str:
        """Normalize MAC address format"""
        # Remove all separators and convert to lowercase
        mac = re.sub(r'[:-]', '', mac).lower()
        # Add colons every 2 characters
        return ':'.join(mac[i:i+2] for i in range(0, len(mac), 2))
    
    def get_oui(self, mac: str) -> str:
        """Extract OUI (first 3 octets) from MAC address"""
        normalized = self.normalize_mac(mac)
        return ':'.join(normalized.split(':')[:3])
    
    def lookup_vendor(self, mac: str) -> Optional[str]:
        """Look up vendor from MAC address"""
        oui = self.get_oui(mac)
        
        # Check local database
        if oui in self.oui_database:
            return self.oui_database[oui]
        
        # Could add API lookup here for unknown vendors
        return "Unknown Vendor"
    
    def analyze_mac(self, mac: str):
        """Analyze MAC address and print details"""
        normalized = self.normalize_mac(mac)
        oui = self.get_oui(mac)
        vendor = self.lookup_vendor(mac)
        
        print("\n" + "="*60)
        print("  MAC ADDRESS ANALYSIS")
        print("="*60)
        print(f"Original MAC:     {mac}")
        print(f"Normalized MAC:   {normalized}")
        print(f"OUI:              {oui}")
        print(f"Vendor:           {vendor}")
        print("="*60 + "\n")
        
        # Determine if virtual machine
        if any(vm in vendor.lower() for vm in ['vmware', 'virtualbox', 'qemu', 'parallels']):
            print("[!] This appears to be a virtual machine")
        
        return {
            "mac": normalized,
            "oui": oui,
            "vendor": vendor
        }

def main():
    lookup = MACLookup()
    
    # Example MAC addresses from competition
    test_macs = [
        "000C2946D739",
        "74:da:38:da:de:b2",
        "0:c:29:c2:65:2a"
    ]
    
    print("""
╔═══════════════════════════════════════════════════════════╗
║        MAC ADDRESS VENDOR LOOKUP - Competition Tool       ║
╚═══════════════════════════════════════════════════════════╝
    """)
    
    for mac in test_macs:
        lookup.analyze_mac(mac)

if __name__ == "__main__":
    main()
