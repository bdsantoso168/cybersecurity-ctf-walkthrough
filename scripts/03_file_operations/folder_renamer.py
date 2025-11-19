#!/usr/bin/env python3
"""
Automated Folder Renaming Tool
Renames team folders according to competition requirements
"""

import os
import sys
import re
from pathlib import Path
from datetime import datetime

class FolderRenamer:
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        self.rename_log = []
    
    def find_team_folders(self, pattern: str = "Team.*RENAME") -> list:
        """Find folders matching the rename pattern"""
        folders = []
        
        print(f"[*] Searching for folders matching: {pattern}")
        print(f"[*] Base path: {self.base_path.absolute()}\\n")
        
        for item in self.base_path.iterdir():
            if item.is_dir() and re.search(pattern, item.name, re.IGNORECASE):
                folders.append(item)
                print(f"    Found: {item.name}")
        
        return folders
    
    def rename_folder(self, folder_path: Path, old_text: str, new_text: str) -> bool:
        """Rename a folder by replacing text"""
        try:
            old_name = folder_path.name
            new_name = old_name.replace(old_text, new_text)
            new_path = folder_path.parent / new_name
            
            # Check if destination already exists
            if new_path.exists():
                print(f"[!] Destination already exists: {new_name}")
                return False
            
            # Perform rename
            folder_path.rename(new_path)
            
            # Log the action
            log_entry = {
                "timestamp": datetime.now().isoformat(),
                "old_name": old_name,
                "new_name": new_name,
                "success": True
            }
            self.rename_log.append(log_entry)
            
            print(f"[✓] Renamed: {old_name} → {new_name}")
            return True
        
        except PermissionError:
            print(f"[!] Permission denied: {folder_path.name}")
            return False
        except Exception as e:
            print(f"[!] Error renaming {folder_path.name}: {e}")
            return False
    
    def batch_rename(self, old_text: str, new_text: str, pattern: str = "Team.*RENAME"):
        """Batch rename all matching folders"""
        folders = self.find_team_folders(pattern)
        
        if not folders:
            print("\\n[!] No folders found matching the pattern")
            return
        
        print(f"\\n[*] Found {len(folders)} folder(s) to rename")
        print(f"[*] Will replace '{old_text}' with '{new_text}'\\n")
        
        # Confirm action
        confirm = input("Proceed with renaming? (yes/no): ").strip().lower()
        if confirm != 'yes':
            print("[!] Operation cancelled")
            return
        
        print("\\n" + "="*60)
        success_count = 0
        
        for folder in folders:
            if self.rename_folder(folder, old_text, new_text):
                success_count += 1
        
        print("="*60)
        print(f"\\n[✓] Successfully renamed {success_count}/{len(folders)} folder(s)")
    
    def save_log(self, filename: str = "rename_log.txt"):
        """Save rename log to file"""
        if not self.rename_log:
            print("[!] No rename operations to log")
            return
        
        with open(filename, 'w') as f:
            f.write("FOLDER RENAME LOG\\n")
            f.write("="*60 + "\\n\\n")
            
            for entry in self.rename_log:
                f.write(f"Timestamp: {entry['timestamp']}\\n")
                f.write(f"Old Name:  {entry['old_name']}\\n")
                f.write(f"New Name:  {entry['new_name']}\\n")
                f.write(f"Status:    {'Success' if entry['success'] else 'Failed'}\\n")
                f.write("-"*60 + "\\n")
        
        print(f"[✓] Log saved to: {filename}")

def main():
    print("""
╔═══════════════════════════════════════════════════════════╗
║       FOLDER RENAMER - Competition Tool                   ║
╚═══════════════════════════════════════════════════════════╝
    """)
    
    # Parse command line arguments
    if len(sys.argv) < 3:
        print("Usage: python3 folder_renamer.py <OLD_TEXT> <NEW_TEXT> [BASE_PATH]")
        print("\\nExample:")
        print("  python3 folder_renamer.py RENAME Benz")
        print("  python3 folder_renamer.py RENAME Benz /path/to/folder")
        print("\\nThis will rename folders like 'Team 14 RENAME' to 'Team 14 Benz'")
        sys.exit(1)
    
    old_text = sys.argv[1]
    new_text = sys.argv[2]
    base_path = sys.argv[3] if len(sys.argv) > 3 else "."
    
    renamer = FolderRenamer(base_path)
    renamer.batch_rename(old_text, new_text)
    renamer.save_log()

if __name__ == "__main__":
    main()
'''
