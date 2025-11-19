#!/usr/bin/env python3
"""
Task Tracker
Tracks progress through competition tasks
"""

import json
from datetime import datetime
from typing import List, Dict

class Task:
    def __init__(self, number: int, name: str, points: int, category: str):
        self.number = number
        self.name = name
        self.points = points
        self.category = category
        self.completed = False
        self.completion_time = None
        self.notes = ""
    
    def complete(self, notes: str = ""):
        """Mark task as completed"""
        self.completed = True
        self.completion_time = datetime.now().isoformat()
        self.notes = notes
    
    def to_dict(self) -> Dict:
        """Convert task to dictionary"""
        return {
            "number": self.number,
            "name": self.name,
            "points": self.points,
            "category": self.category,
            "completed": self.completed,
            "completion_time": self.completion_time,
            "notes": self.notes
        }
    
    @staticmethod
    def from_dict(data: Dict) -> 'Task':
        """Create task from dictionary"""
        task = Task(
            data['number'],
            data['name'],
            data['points'],
            data['category']
        )
        task.completed = data.get('completed', False)
        task.completion_time = data.get('completion_time')
        task.notes = data.get('notes', '')
        return task

class TaskTracker:
    def __init__(self, save_file: str = "task_progress.json"):
        self.save_file = save_file
        self.tasks = []
        self.team_name = ""
        self.initialize_tasks()
        self.load_progress()
    
    def initialize_tasks(self):
        """Initialize all competition tasks"""
        tasks_data = [
            (1, "Remote Connect to SYSTEM-A", 10, "Initial Access"),
            (2, "Find and Rename Team Folder", 20, "Initial Access"),
            (3, "Find IP Address and Save", 20, "Initial Access"),
            (4, "Find 6-Digit Number", 30, "Initial Access"),
            (5, "Connect to SYSTEM-B", 10, "Lateral Movement"),
            (6, "Network Mapping", 10, "Reconnaissance"),
            (7, "Crack 'Cyber' File", 15, "Password Cracking"),
            (8, "Crack 'Security' File", 15, "Password Cracking"),
            (9, "Password Validation", 10, "Validation"),
            (10, "Final Submission", 10, "Completion")
        ]
        
        self.tasks = [Task(num, name, pts, cat) for num, name, pts, cat in tasks_data]
    
    def load_progress(self):
        """Load saved progress"""
        try:
            with open(self.save_file, 'r') as f:
                data = json.load(f)
                self.team_name = data.get('team_name', '')
                
                # Load task states
                for task_data in data.get('tasks', []):
                    task_num = task_data['number']
                    if 0 < task_num <= len(self.tasks):
                        self.tasks[task_num - 1] = Task.from_dict(task_data)
                
                print(f"[✓] Loaded progress for team: {self.team_name}")
        except FileNotFoundError:
            print("[*] No saved progress found, starting fresh")
        except Exception as e:
            print(f"[!] Error loading progress: {e}")
    
    def save_progress(self):
        """Save current progress"""
        data = {
            "team_name": self.team_name,
            "last_updated": datetime.now().isoformat(),
            "tasks": [task.to_dict() for task in self.tasks]
        }
        
        try:
            with open(self.save_file, 'w') as f:
                json.dump(data, f, indent=4)
            print(f"[✓] Progress saved")
        except Exception as e:
            print(f"[!] Error saving progress: {e}")
    
    def mark_complete(self, task_number: int, notes: str = ""):
        """Mark a task as complete"""
        if 0 < task_number <= len(self.tasks):
            task = self.tasks[task_number - 1]
            task.complete(notes)
            self.save_progress()
            print(f"[✓] Task {task_number} completed: {task.name} (+{task.points} points)")
        else:
            print(f"[!] Invalid task number: {task_number}")
    
    def add_note(self, task_number: int, note: str):
        """Add a note to a task"""
        if 0 < task_number <= len(self.tasks):
            task = self.tasks[task_number - 1]
            if task.notes:
                task.notes += "\\n" + note
            else:
                task.notes = note
            self.save_progress()
            print(f"[✓] Note added to Task {task_number}")
        else:
            print(f"[!] Invalid task number: {task_number}")
    
    def get_progress(self) -> Dict:
        """Get progress statistics"""
        total_tasks = len(self.tasks)
        completed_tasks = sum(1 for task in self.tasks if task.completed)
        total_points = sum(task.points for task in self.tasks)
        earned_points = sum(task.points for task in self.tasks if task.completed)
        
        return {
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "remaining_tasks": total_tasks - completed_tasks,
            "total_points": total_points,
            "earned_points": earned_points,
            "remaining_points": total_points - earned_points,
            "completion_percentage": (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
        }
    
    def print_status(self):
        """Print current status"""
        progress = self.get_progress()
        
        print("\\n" + "="*80)
        print("  COMPETITION PROGRESS TRACKER")
        if self.team_name:
            print(f"  Team: {self.team_name}")
        print("="*80)
        
        print(f"\\nOverall Progress: {progress['completed_tasks']}/{progress['total_tasks']} tasks " +
              f"({progress['completion_percentage']:.1f}%)")
        print(f"Points Earned: {progress['earned_points']}/{progress['total_points']}")
        
        # Progress bar
        bar_length = 50
        filled = int(bar_length * progress['completion_percentage'] / 100)
        bar = "█" * filled + "░" * (bar_length - filled)
        print(f"\\n[{bar}] {progress['completion_percentage']:.1f}%")
        
        # Tasks by category
        print("\\n" + "-"*80)
        print("TASKS BY CATEGORY:")
        print("-"*80)
        
        current_category = None
        for task in self.tasks:
            if task.category != current_category:
                current_category = task.category
                print(f"\\n{current_category}:")
            
            status = "✓" if task.completed else "○"
            time_str = ""
            if task.completed and task.completion_time:
                time = datetime.fromisoformat(task.completion_time).strftime("%H:%M:%S")
                time_str = f" (completed at {time})"
            
            print(f"  [{status}] Task {task.number}: {task.name} ({task.points} pts){time_str}")
            
            if task.notes:
                for line in task.notes.split('\\n'):
                    print(f"      Note: {line}")
        
        print("\\n" + "="*80 + "\\n")
    
    def print_next_tasks(self):
        """Print next uncompleted tasks"""
        uncompleted = [task for task in self.tasks if not task.completed]
        
        if not uncompleted:
            print("\\n🎉 All tasks completed! Great job!")
            return
        
        print("\\n" + "="*80)
        print("  NEXT TASKS TO COMPLETE")
        print("="*80 + "\\n")
        
        for task in uncompleted[:3]:  # Show next 3 tasks
            print(f"Task {task.number}: {task.name}")
            print(f"  Category: {task.category}")
            print(f"  Points: {task.points}")
            print()
        
        if len(uncompleted) > 3:
            print(f"... and {len(uncompleted) - 3} more task(s)")
        
        print("="*80 + "\\n")
    
    def export_report(self, filename: str = "progress_report.txt"):
        """Export progress report"""
        progress = self.get_progress()
        
        with open(filename, 'w') as f:
            f.write("COMPETITION PROGRESS REPORT\\n")
            f.write("="*80 + "\\n")
            f.write(f"Team: {self.team_name}\\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\\n")
            f.write("="*80 + "\\n\\n")
            
            f.write("SUMMARY\\n")
            f.write("-"*80 + "\\n")
            f.write(f"Tasks Completed: {progress['completed_tasks']}/{progress['total_tasks']}\\n")
            f.write(f"Points Earned: {progress['earned_points']}/{progress['total_points']}\\n")
            f.write(f"Completion: {progress['completion_percentage']:.1f}%\\n\\n")
            
            f.write("DETAILED TASK LIST\\n")
            f.write("-"*80 + "\\n\\n")
            
            for task in self.tasks:
                status = "COMPLETED" if task.completed else "PENDING"
                f.write(f"Task {task.number}: {task.name}\\n")
                f.write(f"  Category: {task.category}\\n")
                f.write(f"  Points: {task.points}\\n")
                f.write(f"  Status: {status}\\n")
                
                if task.completed and task.completion_time:
                    time = datetime.fromisoformat(task.completion_time).strftime("%Y-%m-%d %H:%M:%S")
                    f.write(f"  Completed: {time}\\n")
                
                if task.notes:
                    f.write(f"  Notes: {task.notes}\\n")
                
                f.write("\\n")
        
        print(f"[✓] Report exported to: {filename}")

def main():
    print("""
╔═══════════════════════════════════════════════════════════╗
║         TASK TRACKER - Competition Progress Tool          ║
╚═══════════════════════════════════════════════════════════╝
    """)
    
    tracker = TaskTracker()
    
    # Interactive menu
    while True:
        print("\\nOptions:")
        print("1. View status")
        print("2. Mark task complete")
        print("3. Add note to task")
        print("4. View next tasks")
        print("5. Export report")
        print("6. Set team name")
        print("7. Exit")
        
        choice = input("\\nSelect option: ").strip()
        
        if choice == "1":
            tracker.print_status()
        
        elif choice == "2":
            task_num = int(input("Task number: "))
            notes = input("Notes (optional): ").strip()
            tracker.mark_complete(task_num, notes)
        
        elif choice == "3":
            task_num = int(input("Task number: "))
            note = input("Note: ").strip()
            tracker.add_note(task_num, note)
        
        elif choice == "4":
            tracker.print_next_tasks()
        
        elif choice == "5":
            tracker.export_report()
        
        elif choice == "6":
            team_name = input("Team name: ").strip()
            tracker.team_name = team_name
            tracker.save_progress()
            print(f"[✓] Team name set to: {team_name}")
        
        elif choice == "7":
            tracker.save_progress()
            print("\\n[✓] Progress saved. Goodbye!")
            break
        
        else:
            print("[!] Invalid option")

if __name__ == "__main__":
    main()
