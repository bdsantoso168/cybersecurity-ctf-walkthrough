#!/usr/bin/env python3
"""
Visual Network Mapper
Creates ASCII art network topology diagrams
"""

import json
import sys
from typing import List, Dict

class VisualMapper:
    def __init__(self):
        self.devices = []
        self.gateway = "192.168.0.1"
    
    def load_from_json(self, json_file: str):
        """Load network data from JSON"""
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
                self.devices = data.get('devices', [])
                
                # Try to determine gateway
                subnet = data.get('subnet', '192.168.0.0/24')
                self.gateway = subnet.split('/')[0].rsplit('.', 1)[0] + '.1'
            
            print(f"[✓] Loaded {len(self.devices)} device(s)")
        except Exception as e:
            print(f"[!] Error loading JSON: {e}")
    
    def generate_simple_diagram(self) -> str:
        """Generate simple network diagram"""
        lines = []
        
        lines.append("╔═══════════════════════════════════════════════════════════════╗")
        lines.append("║              NETWORK TOPOLOGY DIAGRAM                         ║")
        lines.append("╚═══════════════════════════════════════════════════════════════╝")
        lines.append("")
        
        # Gateway/Router
        lines.append("                    ┌─────────────────┐")
        lines.append("                    │   Gateway       │")
        lines.append(f"                    │   {self.gateway:<15} │")
        lines.append("                    └────────┬────────┘")
        lines.append("                             │")
        lines.append("                  ───────────┴───────────")
        lines.append("                 /                       \\\\")
        
        # Devices
        for i, device in enumerate(self.devices):
            if i % 2 == 0:
                lines.append("                /                         \\\\")
                lines.append("               /                           \\\\")
            
            hostname = device.get('hostname', 'Unknown')[:15]
            ip = device.get('ip', 'Unknown')
            
            if i % 2 == 0:
                lines.append(f"    ┌──────────────────┐              ┌──────────────────┐")
                lines.append(f"    │ {hostname:<16} │              │", end="")
            else:
                lines.append(f" {hostname:<16} │")
                lines.append(f"    │ {ip:<16} │              │ {device.get('ip', 'Unknown'):<16} │")
                lines.append(f"    └──────────────────┘              └──────────────────┘")
                lines.append("")
        
        # Handle odd number of devices
        if len(self.devices) % 2 == 1:
            lines.append("                 │")
            lines.append("    └──────────────────┘")
            lines.append("")
        
        return '\\n'.join(lines)
    
    def generate_detailed_diagram(self) -> str:
        """Generate detailed network diagram with more information"""
        lines = []
        
        lines.append("╔" + "═"*78 + "╗")
        lines.append("║" + " "*25 + "NETWORK TOPOLOGY MAP" + " "*33 + "║")
        lines.append("╚" + "═"*78 + "╝")
        lines.append("")
        lines.append("                          Internet/WAN")
        lines.append("                                │")
        lines.append("                                │")
        lines.append("                     ┌──────────┴──────────┐")
        lines.append("                     │     Gateway/Router   │")
        lines.append(f"                     │     {self.gateway:<15} │")
        lines.append("                     └──────────┬──────────┘")
        lines.append("                                │")
        lines.append("                                │ LAN")
        lines.append("          ──────────────────────┴──────────────────────")
        lines.append("         /              /               \\\\              \\\\")
        lines.append("")
        
        # Create rows of devices (3 per row)
        for i in range(0, len(self.devices), 3):
            batch = self.devices[i:i+3]
            
            # Top border
            top_line = "    "
            for _ in batch:
                top_line += "┌────────────────────┐  "
            lines.append(top_line)
            
            # Hostname
            name_line = "    "
            for device in batch:
                hostname = device.get('hostname', 'Unknown')[:18]
                name_line += f"│ {hostname:<18} │  "
            lines.append(name_line)
            
            # IP
            ip_line = "    "
            for device in batch:
                ip = device.get('ip', 'Unknown')[:18]
                ip_line += f"│ IP: {ip:<15} │  "
            lines.append(ip_line)
            
            # MAC
            mac_line = "    "
            for device in batch:
                mac = device.get('mac', 'Unknown')[:18]
                mac_line += f"│ MAC: {mac:<14} │  "
            lines.append(mac_line)
            
            # OS
            os_line = "    "
            for device in batch:
                os = device.get('os', 'Unknown')[:18]
                os_line += f"│ OS: {os:<15} │  "
            lines.append(os_line)
            
            # Bottom border
            bottom_line = "    "
            for _ in batch:
                bottom_line += "└────────────────────┘  "
            lines.append(bottom_line)
            lines.append("")
        
        return '\\n'.join(lines)
    
    def generate_tree_diagram(self) -> str:
        """Generate tree-style network diagram"""
        lines = []
        
        lines.append("NETWORK TREE")
        lines.append("═" * 60)
        lines.append("")
        lines.append(f"Gateway: {self.gateway}")
        lines.append("│")
        
        for i, device in enumerate(self.devices):
            is_last = (i == len(self.devices) - 1)
            prefix = "└── " if is_last else "├── "
            continuation = "    " if is_last else "│   "
            
            hostname = device.get('hostname', 'Unknown')
            ip = device.get('ip', 'Unknown')
            mac = device.get('mac', 'Unknown')
            os = device.get('os', 'Unknown')
            
            lines.append(f"{prefix}{hostname}")
            lines.append(f"{continuation}├─ IP:  {ip}")
            lines.append(f"{continuation}├─ MAC: {mac}")
            lines.append(f"{continuation}└─ OS:  {os}")
            
            if not is_last:
                lines.append("│")
        
        return '\\n'.join(lines)
    
    def save_diagram(self, diagram: str, filename: str):
        """Save diagram to file"""
        with open(filename, 'w') as f:
            f.write(diagram)
        print(f"[✓] Diagram saved to: {filename}")
    
    def print_diagram(self, diagram: str):
        """Print diagram to console"""
        print("\\n" + diagram + "\\n")

def main():
    print("""
╔═══════════════════════════════════════════════════════════╗
║       VISUAL NETWORK MAPPER - Competition Tool            ║
╚═══════════════════════════════════════════════════════════╝
    """)
    
    if len(sys.argv) < 2:
        print("Usage: python3 visual_mapper.py <network_map.json> [diagram_type]")
        print("\\nDiagram Types:")
        print("  simple   - Simple network diagram (default)")
        print("  detailed - Detailed diagram with all info")
        print("  tree     - Tree-style diagram")
        print("\\nExample:")
        print("  python3 visual_mapper.py network_map.json detailed")
        sys.exit(1)
    
    json_file = sys.argv[1]
    diagram_type = sys.argv[2] if len(sys.argv) > 2 else "simple"
    
    mapper = VisualMapper()
    mapper.load_from_json(json_file)
    
    if not mapper.devices:
        print("[!] No devices found in JSON file")
        return
    
    # Generate diagram based on type
    if diagram_type == "detailed":
        diagram = mapper.generate_detailed_diagram()
        filename = "network_diagram_detailed.txt"
    elif diagram_type == "tree":
        diagram = mapper.generate_tree_diagram()
        filename = "network_diagram_tree.txt"
    else:
        diagram = mapper.generate_simple_diagram()
        filename = "network_diagram.txt"
    
    # Print and save
    mapper.print_diagram(diagram)
    mapper.save_diagram(diagram, filename)
    
    print(f"[✓] Diagram type '{diagram_type}' generated successfully!")

if __name__ == "__main__":
    main()
