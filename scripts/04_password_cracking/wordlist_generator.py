#!/usr/bin/env python3
"""
Custom Wordlist Generator
Generates context-specific wordlists for password cracking
"""

import sys
import itertools
from typing import List

class WordlistGenerator:
    def __init__(self):
        self.wordlist = set()
    
    def add_base_words(self, words: List[str]):
        """Add base words to wordlist"""
        for word in words:
            self.wordlist.add(word)
            self.wordlist.add(word.lower())
            self.wordlist.add(word.upper())
            self.wordlist.add(word.capitalize())
    
    def add_with_numbers(self, word: str, number_range: range = range(0, 10000)):
        """Add word with number variations"""
        # Common patterns
        self.wordlist.add(word)
        
        # Add single digits
        for i in range(10):
            self.wordlist.add(f"{word}{i}")
            self.wordlist.add(f"{i}{word}")
        
        # Add common years
        for year in [1900, 1906, 1950, 2000, 2020, 2021, 2022, 2023, 2024, 2025]:
            self.wordlist.add(f"{word}{year}")
            self.wordlist.add(f"{word}-{year}")
            self.wordlist.add(f"{word}_{year}")
        
        # Add three-digit patterns
        for i in range(100, 1000, 111):  # 111, 222, 333, etc.
            self.wordlist.add(f"{word}{i}")
    
    def add_with_special_chars(self, word: str):
        """Add word with special character variations"""
        special_chars = ['!', '@', '#', '$', '%', '&', '*', '-', '_']
        
        for char in special_chars:
            self.wordlist.add(f"{word}{char}")
            self.wordlist.add(f"{char}{word}")
            self.wordlist.add(f"{word}{char}{word}")
    
    def add_leet_speak(self, word: str):
        """Add leet speak variations"""
        leet_map = {
            'a': ['a', '4', '@'],
            'e': ['e', '3'],
            'i': ['i', '1', '!'],
            'o': ['o', '0'],
            's': ['s', '5', '$'],
            't': ['t', '7'],
            'l': ['l', '1'],
            'g': ['g', '9']
        }
        
        # Simple leet variations
        leet_word = word.lower()
        for original, replacements in leet_map.items():
            for replacement in replacements[1:]:  # Skip the original letter
                self.wordlist.add(leet_word.replace(original, replacement))
    
    def add_keyboard_patterns(self):
        """Add common keyboard patterns"""
        patterns = [
            'qwerty', 'asdfgh', 'zxcvbn',
            'qwertyuiop', 'asdfghjkl', 'zxcvbnm',
            '123456', '1234567890',
            'password', 'Password', 'PASSWORD',
            'admin', 'Admin', 'ADMIN',
            'root', 'Root', 'ROOT'
        ]
        
        for pattern in patterns:
            self.wordlist.add(pattern)
    
    def add_common_passwords(self):
        """Add commonly used passwords"""
        common = [
            'password', 'Password', 'PASSWORD', 'password123',
            '123456', '12345678', '1234567890',
            'qwerty', 'abc123', 'password1',
            'admin', 'letmein', 'welcome',
            'monkey', 'dragon', 'master',
            'sunshine', 'princess', 'login',
            'passw0rd', 'P@ssw0rd', 'P@ssword'
        ]
        
        for pwd in common:
            self.wordlist.add(pwd)
    
    def generate_competition_wordlist(self, 
                                     institution: str = "suffolk",
                                     team_name: str = "",
                                     year: int = 1906):
        """Generate wordlist specific to competition"""
        
        print("[*] Generating competition-specific wordlist...")
        
        # Institution-based words
        base_words = [
            institution,
            institution.capitalize(),
            institution.upper(),
            "university",
            "college",
            "cyber", "security", "competition",
            "sargent", "captain", "lieutenant",
            "admin", "administrator", "user"
        ]
        
        if team_name:
            base_words.extend([team_name, team_name.lower(), team_name.upper()])
        
        # Add base words and variations
        for word in base_words:
            self.add_base_words([word])
            self.add_with_numbers(word)
            self.add_with_special_chars(word)
            self.add_leet_speak(word)
        
        # Add keyboard patterns
        self.add_keyboard_patterns()
        
        # Add common passwords
        self.add_common_passwords()
        
        # Add institution + year combinations
        self.wordlist.add(f"{institution}{year}")
        self.wordlist.add(f"{institution}-{year}")
        self.wordlist.add(f"{institution}_{year}")
        self.wordlist.add(f"{institution.capitalize()}{year}")
        
        print(f"[✓] Generated {len(self.wordlist)} passwords")
    
    def save_wordlist(self, filename: str = "custom_wordlist.txt"):
        """Save wordlist to file"""
        sorted_list = sorted(self.wordlist)
        
        with open(filename, 'w') as f:
            for word in sorted_list:
                f.write(word + '\\n')
        
        print(f"[✓] Wordlist saved to: {filename}")
        print(f"[✓] Total passwords: {len(sorted_list)}")
    
    def print_statistics(self):
        """Print wordlist statistics"""
        print("\\n" + "="*60)
        print("  WORDLIST STATISTICS")
        print("="*60)
        print(f"Total passwords:     {len(self.wordlist)}")
        
        # Length distribution
        lengths = {}
        for word in self.wordlist:
            length = len(word)
            lengths[length] = lengths.get(length, 0) + 1
        
        print("\\nLength distribution:")
        for length in sorted(lengths.keys())[:10]:  # Show first 10
            print(f"  {length} chars: {lengths[length]} passwords")
        
        print("="*60 + "\\n")

def main():
    print("""
╔═══════════════════════════════════════════════════════════╗
║      CUSTOM WORDLIST GENERATOR - Competition Tool         ║
╚═══════════════════════════════════════════════════════════╝
    """)
    
    generator = WordlistGenerator()
    
    # Get parameters
    if len(sys.argv) > 1:
        institution = sys.argv[1]
    else:
        institution = input("Enter institution name (default: suffolk): ").strip() or "suffolk"
    
    if len(sys.argv) > 2:
        team_name = sys.argv[2]
    else:
        team_name = input("Enter team name (optional): ").strip()
    
    if len(sys.argv) > 3:
        year = int(sys.argv[3])
    else:
        year_input = input("Enter year (default: 1906): ").strip()
        year = int(year_input) if year_input else 1906
    
    # Generate wordlist
    generator.generate_competition_wordlist(institution, team_name, year)
    
    # Print statistics
    generator.print_statistics()
    
    # Save to file
    output_file = f"{institution}_wordlist.txt"
    generator.save_wordlist(output_file)
    
    print(f"\\n[✓] Use this wordlist with John the Ripper:")
    print(f"    john --wordlist={output_file} hash.txt")

if __name__ == "__main__":
    main()
