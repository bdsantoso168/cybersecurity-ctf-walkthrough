#!/usr/bin/env python3
"""
Competition Activity Logger
Logs all actions and findings during the competition
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List

class CompetitionLogger:
    def __init__(self, log_file: str = "competition_log.json"):
        self.log_file = log_file
        self.logs = []
        self.load_logs()
    
    def load_logs(self):
        """Load existing logs from file"""
        if Path(self.log_file).exists():
            try:
                with open(self.log_file, 'r') as f:
                    self.logs = json.load(f)
                print(f"[✓] Loaded {len(self.logs)} existing log(s)")
            except Exception as e:
                print(f"[!] Error loading logs: {e}")
                self.logs = []
        else:
            print("[*] Starting new log file")
    
    def log_action(self, task: str, action: str, status: str, details: str = ""):
        """Log a competition action"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "task": task,
            "action": action,
            "status": status,
            "details": details
        }
        
        self.logs.append(entry)
        self.save_logs()
        
        # Print to console
        print(f"[LOG] {task} - {action}: {status}")
        if details:
            print(f"      {details}")
    
    def log_discovery(self, discovery_type: str, value: str, context: str = ""):
        """Log a discovery (IP, password, file, etc.)"""
        self.log_action(
            task="Discovery",
            action=f"Found {discovery_type}",
            status="Success",
            details=f"{discovery_type}: {value}\\n{context}"
        )
    
    def log_connection(self, system: str, ip: str, success: bool, credentials: str = ""):
        """Log a connection attempt"""
        status = "Success" if success else "Failed"
        details = f"System: {system}\\nIP: {ip}"
        if credentials:
            details += f"\\nCredentials: {credentials}"
        
        self.log_action(
            task="Connection",
            action=f"Connect to {system}",
            status=status,
            details=details
        )
    
    def log_task_completion(self, task_number: int, task_name: str, points: int, completion_time: str = ""):
        """Log task completion"""
        if not completion_time:
            completion_time = datetime.now().strftime("%H:%M:%S")
        
        self.log_action(
            task=f"Task {task_number}",
            action=task_name,
            status="Completed",
            details=f"Points: {points}\\nCompleted at: {completion_time}"
        )
    
    def log_password_crack(self, file_name: str, password: str, method: str):
        """Log successful password crack"""
        self.log_action(
            task="Password Cracking",
            action=f"Cracked {file_name}",
            status="Success",
            details=f"Password: {password}\\nMethod: {method}"
        )
    
    def log_error(self, task: str, error_message: str):
        """Log an error"""
        self.log_action(
            task=task,
            action="Error occurred",
            status="Failed",
            details=error_message
        )
    
    def save_logs(self):
        """Save logs to file"""
        try:
            with open(self.log_file, 'w') as f:
                json.dump(self.logs, f, indent=4)
        except Exception as e:
            print(f"[!] Error saving logs: {e}")
    
    def get_logs_by_task(self, task: str) -> List[Dict]:
        """Get all logs for a specific task"""
        return [log for log in self.logs if log['task'] == task]
    
    def get_logs_by_status(self, status: str) -> List[Dict]:
        """Get all logs with a specific status"""
        return [log for log in self.logs if log['status'] == status]
    
    def export_timeline(self, filename: str = "timeline.txt"):
        """Export timeline of events"""
        with open(filename, 'w') as f:
            f.write("COMPETITION TIMELINE\\n")
            f.write("="*80 + "\\n\\n")
            
            for log in self.logs:
                timestamp = datetime.fromisoformat(log['timestamp']).strftime("%H:%M:%S")
                f.write(f"[{timestamp}] {log['task']} - {log['action']}\\n")
                f.write(f"           Status: {log['status']}\\n")
                if log['details']:
                    for line in log['details'].split('\\n'):
                        f.write(f"           {line}\\n")
                f.write("\\n")
        
        print(f"[✓] Timeline exported to: {filename}")
    
    def print_summary(self):
        """Print summary of all logged activities"""
        print("\\n" + "="*80)
        print("  COMPETITION LOG SUMMARY")
        print("="*80)
        print(f"Total Entries: {len(self.logs)}")
        
        # Count by status
        statuses = {}
        for log in self.logs:
            status = log['status']
            statuses[status] = statuses.get(status, 0) + 1
        
        print("\\nBy Status:")
        for status, count in statuses.items():
            print(f"  {status}: {count}")
        
        # Count by task
        tasks = {}
        for log in self.logs:
            task = log['task']
            tasks[task] = tasks.get(task, 0) + 1
        
        print("\\nBy Task:")
        for task, count in sorted(tasks.items()):
            print(f"  {task}: {count}")
        
        print("="*80 + "\\n")
    
    def print_recent(self, count: int = 10):
        """Print recent log entries"""
        print("\\n" + "="*80)
        print(f"  RECENT LOG ENTRIES (Last {count})")
        print("="*80 + "\\n")
        
        recent = self.logs[-count:] if len(self.logs) > count else self.logs
        
        for log in recent:
            timestamp = datetime.fromisoformat(log['timestamp']).strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{timestamp}]")
            print(f"  Task:   {log['task']}")
            print(f"  Action: {log['action']}")
            print(f"  Status: {log['status']}")
            if log['details']:
                print(f"  Details: {log['details'][:100]}...")
            print()
        
        print("="*80 + "\\n")

def main():
    print("""
╔═══════════════════════════════════════════════════════════╗
║       COMPETITION LOGGER - Activity Tracking Tool         ║
╚═══════════════════════════════════════════════════════════╝
    """)
    
    logger = CompetitionLogger()
    
    # Example usage
    print("\\nLogger initialized. Use the logger object in your scripts:")
    print("\\nExample commands:")
    print("  logger.log_discovery('IP Address', '192.168.0.154')")
    print("  logger.log_connection('SYSTEM-A', '192.168.0.154', True)")
    print("  logger.log_task_completion(1, 'Remote Connect', 10)")
    print("  logger.log_password_crack('Cyber.7z', 'password', 'Manual')")
    print("\\nView logs:")
    print("  logger.print_summary()")
    print("  logger.print_recent(5)")
    print("  logger.export_timeline()")
    
    # Show current summary
    if logger.logs:
        logger.print_summary()
        logger.print_recent(5)

if __name__ == "__main__":
    main()
