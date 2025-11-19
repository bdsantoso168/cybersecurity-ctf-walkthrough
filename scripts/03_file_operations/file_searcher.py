#!/usr/bin/env python3
"""
File Search Tool
Searches for specific files in directory structure
Useful for finding hidden files, credentials, and target files
"""

import os
import sys
from pathlib import Path
from datetime import datetime
import fnmatch

class FileSearcher:
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        self.found_files = []
    
    def search_by_name(self, pattern: str, recursive: bool = True) -> list:
        """Search for files by name pattern"""
        print(f"[*] Searching for files matching: {pattern}")
        print(f"[*] Base path: {self.base_path.absolute()}")
        print(f"[*] Recursive: {recursive}\\n")
        
        self.found_files = []
        
        if recursive:
            for root, dirs, files in os.walk(self.base_path):
                for filename in files:
                    if fnmatch.fnmatch(filename, pattern):
                        full_path = Path(root) / filename
                        self.found_files.append(full_path)
        else:
            for item in self.base_path.iterdir():
                if item.is_file() and fnmatch.fnmatch(item.name, pattern):
                    self.found_files.append(item)
        
        return self.found_files
    
    def search_by_extension(self, extension: str, recursive: bool = True) -> list:
        """Search for files by extension"""
        if not extension.startswith('.'):
            extension = '.' + extension
        
        pattern = f"*{extension}"
        return self.search_by_name(pattern, recursive)
    
    def search_hidden_files(self, recursive: bool = True) -> list:
        """Search for hidden files (starting with .)"""
        print(f"[*] Searching for hidden files")
        print(f"[*] Base path: {self.base_path.absolute()}\\n")
        
        self.found_files = []
        
        if recursive:
            for root, dirs, files in os.walk(self.base_path):
                for filename in files:
                    if filename.startswith('.') and filename not in ['.', '..']:
                        full_path = Path(root) / filename
                        self.found_files.append(full_path)
        else:
            for item in self.base_path.iterdir():
                if item.is_file() and item.name.startswith('.'):
                    self.found_files.append(item)
        
        return self.found_files
    
    def search_by_content(self, search_text: str, file_pattern: str = "*") -> list:
        """Search for files containing specific text"""
        print(f"[*] Searching file contents for: {search_text}")
        print(f"[*] File pattern: {file_pattern}\\n")
        
        matching_files = []
        
        # First find all files matching the pattern
        all_files = self.search_by_name(file_pattern)
        
        for file_path in all_files:
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    if search_text in content:
                        matching_files.append(file_path)
            except Exception:
                # Skip files that can't be read
                pass
        
        self.found_files = matching_files
        return matching_files
    
    def get_file_info(self, file_path: Path) -> dict:
        """Get detailed information about a file"""
        stat = file_path.stat()
        
        return {
            "name": file_path.name,
            "path": str(file_path.absolute()),
            "size": stat.st_size,
            "size_human": self.format_size(stat.st_size),
            "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
            "created": datetime.fromtimestamp(stat.st_ctime).isoformat(),
            "extension": file_path.suffix
        }
    
    def format_size(self, size: int) -> str:
        """Format file size in human-readable format"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024.0:
                return f"{size:.2f} {unit}"
            size /= 1024.0
        return f"{size:.2f} TB"
    
    def print_results(self, detailed: bool = False):
        """Print search results"""
        if not self.found_files:
            print("[!] No files found\\n")
            return
        
        print("="*80)
        print(f"  SEARCH RESULTS - {len(self.found_files)} file(s) found")
        print("="*80)
        
        if detailed:
            for file_path in self.found_files:
                info = self.get_file_info(file_path)
                print(f"\\nFile: {info['name']}")
                print(f"  Path:     {info['path']}")
                print(f"  Size:     {info['size_human']}")
                print(f"  Modified: {info['modified']}")
                print("-"*80)
        else:
            for file_path in self.found_files:
                relative_path = file_path.relative_to(self.base_path)
                print(f"  {relative_path}")
        
        print("="*80 + "\\n")
    
    def export_results(self, filename: str = "search_results.txt"):
        """Export search results to file"""
        if not self.found_files:
            print("[!] No results to export")
            return
        
        with open(filename, 'w') as f:
            f.write("FILE SEARCH RESULTS\\n")
            f.write(f"Search Date: {datetime.now().isoformat()}\\n")
            f.write(f"Base Path: {self.base_path.absolute()}\\n")
            f.write(f"Files Found: {len(self.found_files)}\\n")
            f.write("="*80 + "\\n\\n")
            
            for file_path in self.found_files:
                info = self.get_file_info(file_path)
                f.write(f"File: {info['name']}\\n")
                f.write(f"  Path:     {info['path']}\\n")
                f.write(f"  Size:     {info['size_human']}\\n")
                f.write(f"  Modified: {info['modified']}\\n")
                f.write("-"*80 + "\\n")
        
        print(f"[✓] Results exported to: {filename}")

def main():
    print("""
╔═══════════════════════════════════════════════════════════╗
║          FILE SEARCHER - Competition Tool                 ║
╚═══════════════════════════════════════════════════════════╝
    """)
    
    if len(sys.argv) < 2:
        print("Usage: python3 file_searcher.py <SEARCH_TYPE> <PATTERN> [BASE_PATH]")
        print("\\nSearch Types:")
        print("  name      - Search by filename pattern")
        print("  ext       - Search by file extension")
        print("  hidden    - Search for hidden files")
        print("  content   - Search file contents")
        print("\\nExamples:")
        print("  python3 file_searcher.py name 'secret*'")
        print("  python3 file_searcher.py ext txt")
        print("  python3 file_searcher.py hidden")
        print("  python3 file_searcher.py content 'password' /path/to/search")
        sys.exit(1)
    
    search_type = sys.argv[1].lower()
    pattern = sys.argv[2] if len(sys.argv) > 2 else "*"
    base_path = sys.argv[3] if len(sys.argv) > 3 else "."
    
    searcher = FileSearcher(base_path)
    
    if search_type == "name":
        searcher.search_by_name(pattern)
    elif search_type == "ext":
        searcher.search_by_extension(pattern)
    elif search_type == "hidden":
        searcher.search_hidden_files()
    elif search_type == "content":
        searcher.search_by_content(pattern)
    else:
        print(f"[!] Unknown search type: {search_type}")
        sys.exit(1)
    
    searcher.print_results(detailed=True)
    searcher.export_results()

if __name__ == "__main__":
    main()
'''
