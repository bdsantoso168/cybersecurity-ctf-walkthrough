#!/usr/bin/env python3
"""
Competition Report Generator
Generates comprehensive competition reports
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List

class ReportGenerator:
    def __init__(self):
        self.team_name = ""
        self.team_members = []
        self.competition_date = datetime.now().strftime("%Y-%m-%d")
        self.tasks = []
        self.discoveries = []
        self.network_data = []
        self.total_points = 0
    
    def load_task_data(self, task_file: str = "task_progress.json"):
        """Load task completion data"""
        try:
            with open(task_file, 'r') as f:
                data = json.load(f)
                self.team_name = data.get('team_name', 'Unknown')
                self.tasks = data.get('tasks', [])
                self.total_points = sum(t['points'] for t in self.tasks if t.get('completed'))
            print(f"[✓] Loaded task data: {len(self.tasks)} tasks")
        except Exception as e:
            print(f"[!] Error loading task data: {e}")
    
    def load_network_data(self, network_file: str = "network_map.json"):
        """Load network mapping data"""
        try:
            with open(network_file, 'r') as f:
                data = json.load(f)
                self.network_data = data.get('devices', [])
            print(f"[✓] Loaded network data: {len(self.network_data)} devices")
        except Exception as e:
            print(f"[!] Error loading network data: {e}")
    
    def load_log_data(self, log_file: str = "competition_log.json"):
        """Load competition log data"""
        try:
            with open(log_file, 'r') as f:
                logs = json.load(f)
                # Extract discoveries
                self.discoveries = [
                    log for log in logs 
                    if log.get('task') == 'Discovery'
                ]
            print(f"[✓] Loaded log data: {len(self.discoveries)} discoveries")
        except Exception as e:
            print(f"[!] Error loading log data: {e}")
    
    def generate_executive_summary(self) -> str:
        """Generate executive summary"""
        completed_tasks = sum(1 for t in self.tasks if t.get('completed'))
        total_tasks = len(self.tasks)
        completion_rate = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
        
        summary = f"""EXECUTIVE SUMMARY
{"="*80}

Team: {self.team_name}
Competition Date: {self.competition_date}
Report Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

PERFORMANCE METRICS
{"-"*80}
Tasks Completed: {completed_tasks} / {total_tasks} ({completion_rate:.1f}%)
Total Points Earned: {self.total_points}
Network Devices Mapped: {len(self.network_data)}
Key Discoveries: {len(self.discoveries)}

COMPETITION OBJECTIVES
{"-"*80}
✓ Network reconnaissance and mapping
✓ Remote system access and lateral movement
✓ Password cracking and cryptanalysis
✓ File system forensics and data extraction
✓ Documentation and reporting

"""
        return summary
    
    def generate_task_details(self) -> str:
        """Generate detailed task breakdown"""
        details = f"""TASK COMPLETION DETAILS
{"="*80}

"""
        
        for task in self.tasks:
            status = "✓ COMPLETED" if task.get('completed') else "○ PENDING"
            details += f"Task {task['number']}: {task['name']}\\n"
            details += f"  Category: {task['category']}\\n"
            details += f"  Points: {task['points']}\\n"
            details += f"  Status: {status}\\n"
            
            if task.get('completed') and task.get('completion_time'):
                time = datetime.fromisoformat(task['completion_time']).strftime("%H:%M:%S")
                details += f"  Completed: {time}\\n"
            
            if task.get('notes'):
                details += f"  Notes: {task['notes']}\\n"
            
            details += "\\n"
        
        return details
    
    def generate_network_section(self) -> str:
        """Generate network mapping section"""
        section = f"""NETWORK MAPPING RESULTS
{"="*80}

Total Devices Discovered: {len(self.network_data)}

NETWORK TOPOLOGY
{"-"*80}

"""
        
        for i, device in enumerate(self.network_data, 1):
            section += f"Device {i}:\\n"
            section += f"  Hostname:    {device.get('hostname', 'Unknown')}\\n"
            section += f"  IP Address:  {device.get('ip', 'Unknown')}\\n"
            section += f"  MAC Address: {device.get('mac', 'Unknown')}\\n"
            section += f"  OS:          {device.get('os', 'Unknown')}\\n"
            section += f"  Vendor:      {device.get('vendor', 'Unknown')}\\n"
            section += "\\n"
        
        return section
    
    def generate_discoveries_section(self) -> str:
        """Generate key discoveries section"""
        section = f"""KEY DISCOVERIES
{"="*80}

"""
        
        if not self.discoveries:
            section += "No discoveries logged.\\n\\n"
        else:
            for discovery in self.discoveries:
                timestamp = datetime.fromisoformat(discovery['timestamp']).strftime("%H:%M:%S")
                section += f"[{timestamp}] {discovery['action']}\\n"
                if discovery.get('details'):
                    section += f"  {discovery['details']}\\n"
                section += "\\n"
        
        return section
    
    def generate_methodology_section(self) -> str:
        """Generate methodology section"""
        return f"""METHODOLOGY
{"="*80}

TOOLS USED
{"-"*80}
• Network Scanning: ARP, ping, ifconfig/ipconfig
• Remote Access: Microsoft Remote Desktop (RDP)
• Password Cracking: John the Ripper, 7z2john
• File Operations: 7-Zip, text editors
• Scripting: Python, Bash

TECHNIQUES EMPLOYED
{"-"*80}
1. Network Discovery
   - ARP cache analysis for device enumeration
   - Ping sweeps for host discovery
   - MAC address vendor identification

2. Authentication & Access
   - Credential testing and validation
   - Credential rotation/transformation
   - Remote Desktop Protocol (RDP) connections

3. Password Cracking
   - Dictionary attacks with custom wordlists
   - Hash extraction from encrypted archives
   - Context-aware password generation

4. Network Mapping
   - Complete topology documentation
   - Device identification and categorization
   - Data export in multiple formats

"""
    
    def generate_lessons_learned(self) -> str:
        """Generate lessons learned section"""
        return f"""LESSONS LEARNED
{"="*80}

TECHNICAL SKILLS DEVELOPED
{"-"*80}
• Network reconnaissance and enumeration
• Remote system access and management
• Password security analysis and cracking
• File forensics and data extraction
• Documentation and reporting

KEY INSIGHTS
{"-"*80}
1. Password Security
   - Weak passwords can be cracked quickly
   - Common patterns make passwords vulnerable
   - Importance of password complexity and length

2. Network Security
   - Network segmentation importance
   - Access control significance
   - Monitoring and logging necessity

3. Operational Security
   - Documentation is crucial
   - Systematic approach yields better results
   - Time management is essential

RECOMMENDATIONS
{"-"*80}
• Implement strong password policies (16+ characters, mixed case, symbols)
• Use multi-factor authentication where possible
• Regular security audits and penetration testing
• Network segmentation and access controls
• Comprehensive logging and monitoring

"""
    
    def generate_full_report(self, filename: str = "competition_report.txt"):
        """Generate complete competition report"""
        report = ""
        
        # Add all sections
        report += self.generate_executive_summary()
        report += "\\n\\n"
        report += self.generate_task_details()
        report += "\\n"
        report += self.generate_network_section()
        report += "\\n"
        report += self.generate_discoveries_section()
        report += "\\n"
        report += self.generate_methodology_section()
        report += "\\n"
        report += self.generate_lessons_learned()
        
        # Add footer
        report += f"""
{"="*80}
END OF REPORT
Generated by Competition Report Generator
{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
{"="*80}
"""
        
        # Save to file
        with open(filename, 'w
