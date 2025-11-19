#!/usr/bin/env python3
"""
Excel Network Map Generator
Creates Excel spreadsheet with network mapping data
"""

import json
import csv
import sys
from datetime import datetime
from pathlib import Path

class ExcelGenerator:
    def __init__(self):
        self.devices = []
    
    def load_from_json(self, json_file: str):
        """Load network data from JSON file"""
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
                self.devices = data.get('devices', [])
            print(f"[✓] Loaded {len(self.devices)} device(s) from {json_file}")
        except FileNotFoundError:
            print(f"[!] File not found: {json_file}")
        except Exception as e:
            print(f"[!] Error loading JSON: {e}")
    
    def add_device(self, ip: str, mac: str, hostname: str, os: str):
        """Manually add a device"""
        device = {
            "ip": ip,
            "mac": mac,
            "hostname": hostname,
            "os": os
        }
        self.devices.append(device)
    
    def generate_csv(self, filename: str = "Network_Mapping.csv"):
        """Generate CSV file (Excel-compatible)"""
        if not self.devices:
            print("[!] No devices to export")
            return
        
        # Define headers
        headers = ["Computer Name", "IP Address", "MAC Address", "Operating System"]
        
        try:
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                
                # Write header
                writer.writerow(headers)
                
                # Write device data
                for device in self.devices:
                    row = [
                        device.get('hostname', 'Unknown'),
                        device.get('ip', 'Unknown'),
                        device.get('mac', 'Unknown'),
                        device.get('os', 'Unknown')
                    ]
                    writer.writerow(row)
            
            print(f"[✓] CSV file created: {filename}")
            print(f"[✓] Total rows: {len(self.devices) + 1} (including header)")
        
        except Exception as e:
            print(f"[!] Error creating CSV: {e}")
    
    def generate_detailed_csv(self, filename: str = "Network_Mapping_Detailed.csv"):
        """Generate detailed CSV with all available information"""
        if not self.devices:
            print("[!] No devices to export")
            return
        
        # Get all possible keys from devices
        all_keys = set()
        for device in self.devices:
            all_keys.update(device.keys())
        
        headers = sorted(list(all_keys))
        
        try:
            with open(filename, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=headers)
                
                # Write header
                writer.writeheader()
                
                # Write device data
                for device in self.devices:
                    writer.writerow(device)
            
            print(f"[✓] Detailed CSV file created: {filename}")
        
        except Exception as e:
            print(f"[!] Error creating detailed CSV: {e}")
    
    def generate_formatted_text(self, filename: str = "Network_Mapping.txt"):
        """Generate formatted text file that looks like Excel"""
        if not self.devices:
            print("[!] No devices to export")
            return
        
        try:
            with open(filename, 'w') as f:
                # Title
                f.write("NETWORK MAPPING - COMPETITION RESULTS\\n")
                f.write("="*100 + "\\n")
                f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\\n")
                f.write(f"Total Devices: {len(self.devices)}\\n")
                f.write("="*100 + "\\n\\n")
                
                # Table header
                f.write(f"{'Computer Name':<30} {'IP Address':<18} {'MAC Address':<20} {'Operating System':<20}\\n")
                f.write("-"*100 + "\\n")
                
                # Table rows
                for device in self.devices:
                    hostname = device.get('hostname', 'Unknown')[:29]
                    ip = device.get('ip', 'Unknown')[:17]
                    mac = device.get('mac', 'Unknown')[:19]
                    os = device.get('os', 'Unknown')[:19]
                    
                    f.write(f"{hostname:<30} {ip:<18} {mac:<20} {os:<20}\\n")
                
                f.write("="*100 + "\\n")
            
            print(f"[✓] Formatted text file created: {filename}")
        
        except Exception as e:
            print(f"[!] Error creating text file: {e}")
    
    def print_preview(self):
        """Print preview of the data"""
        if not self.devices:
            print("[!] No devices to preview")
            return
        
        print("\\n" + "="*100)
        print("  DATA PREVIEW")
        print("="*100)
        print(f"{'Computer Name':<30} {'IP Address':<18} {'MAC Address':<20} {'Operating System':<20}")
        print("-"*100)
        
        for device in self.devices[:10]:  # Show first 10
            hostname = device.get('hostname', 'Unknown')[:29]
            ip = device.get('ip', 'Unknown')[:17]
            mac = device.get('mac', 'Unknown')[:19]
            os = device.get('os', 'Unknown')[:19]
            
            print(f"{hostname:<30} {ip:<18} {mac:<20} {os:<20}")
        
        if len(self.devices) > 10:
            print(f"... and {len(self.devices) - 10} more device(s)")
        
        print("="*100 + "\\n")

def main():
    print("""
╔═══════════════════════════════════════════════════════════╗
║       EXCEL GENERATOR - Competition Tool                  ║
╚═══════════════════════════════════════════════════════════╝
    """)
    
    generator = ExcelGenerator()
    
    if len(sys.argv) > 1:
        # Load from JSON file
        json_file = sys.argv[1]
        generator.load_from_json(json_file)
    else:
        # Interactive mode
        print("No JSON file provided. Enter devices manually.")
        print("(Press Enter with empty IP to finish)\\n")
        
        while True:
            ip = input("IP Address: ").strip()
            if not ip:
                break
            
            mac = input("MAC Address: ").strip()
            hostname = input("Hostname: ").strip()
            os = input("Operating System: ").strip()
            
            generator.add_device(ip, mac, hostname, os)
            print("[✓] Device added\\n")
    
    if not generator.devices:
        print("[!] No devices to export")
        return
    
    # Preview data
    generator.print_preview()
    
    # Generate files
    generator.generate_csv("Network_Mapping.csv")
    generator.generate_detailed_csv("Network_Mapping_Detailed.csv")
    generator.generate_formatted_text("Network_Mapping.txt")
    
    print("\\n[✓] All files generated successfully!")
    print("\\nGenerated files:")
    print("  • Network_Mapping.csv (Excel-compatible)")
    print("  • Network_Mapping_Detailed.csv (All fields)")
    print("  • Network_Mapping.txt (Formatted text)")

if __name__ == "__main__":
    main()
