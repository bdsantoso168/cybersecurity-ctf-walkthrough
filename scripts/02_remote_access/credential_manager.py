#!/usr/bin/env python3
"""
Secure Credential Manager
Stores and retrieves credentials for competition systems
NOTE: For educational purposes only. In production, use proper secret management.
"""

import json
import getpass
from base64 import b64encode, b64decode
from typing import Dict, Optional

class CredentialManager:
    def __init__(self, credentials_file: str = "credentials.enc"):
        self.credentials_file = credentials_file
        self.credentials = {}
        self.load_credentials()
    
    def add_credential(self, system_name: str, username: str, password: str, ip: str = ""):
        """Add or update credentials for a system"""
        self.credentials[system_name] = {
            "username": username,
            "password": b64encode(password.encode()).decode(),  # Basic encoding (not encryption!)
            "ip": ip
        }
        print(f"[✓] Credentials stored for: {system_name}")
    
    def get_credential(self, system_name: str) -> Optional[Dict]:
        """Retrieve credentials for a system"""
        if system_name in self.credentials:
            cred = self.credentials[system_name].copy()
            cred['password'] = b64decode(cred['password']).decode()
            return cred
        return None
    
    def list_systems(self):
        """List all stored systems"""
        if not self.credentials:
            print("[!] No credentials stored")
            return
        
        print("\n" + "="*60)
        print("  STORED SYSTEMS")
        print("="*60)
        print(f"{'System Name':<20} {'IP Address':<18} {'Username':<20}")
        print("-"*60)
        
        for system, cred in self.credentials.items():
            print(f"{system:<20} {cred.get('ip', 'N/A'):<18} {cred.get('username', 'N/A'):<20}")
        
        print("="*60 + "\n")
    
    def save_credentials(self):
        """Save credentials to file"""
        with open(self.credentials_file, 'w') as f:
            json.dump(self.credentials, f, indent=4)
        print(f"[✓] Credentials saved to: {self.credentials_file}")
    
    def load_credentials(self):
        """Load credentials from file"""
        try:
            with open(self.credentials_file, 'r') as f:
                self.credentials = json.load(f)
            print(f"[✓] Loaded {len(self.credentials)} credential(s)")
        except FileNotFoundError:
            print("[*] No existing credentials file found")
        except Exception as e:
            print(f"[!] Error loading credentials: {e}")

def main():
    print("""
╔═══════════════════════════════════════════════════════════╗
║         CREDENTIAL MANAGER - Competition Tool             ║
║         ⚠️  FOR EDUCATIONAL USE ONLY                      ║
╚═══════════════════════════════════════════════════════════╝
    """)
    
    manager = CredentialManager()
    
    while True:
        print("\nOptions:")
        print("1. Add credential")
        print("2. Get credential")
        print("3. List all systems")
        print("4. Save and exit")
        print("5. Exit without saving")
        
        choice = input("\nSelect option: ").strip()
        
        if choice == "1":
            system = input("System name: ").strip()
            ip = input("IP address: ").strip()
            username = input("Username: ").strip()
            password = getpass.getpass("Password: ")
            manager.add_credential(system, username, password, ip)
        
        elif choice == "2":
            system = input("System name: ").strip()
            cred = manager.get_credential(system)
            if cred:
                print(f"\nCredentials for {system}:")
                print(f"  IP:       {cred.get('ip', 'N/A')}")
                print(f"  Username: {cred['username']}")
                print(f"  Password: {cred['password']}")
            else:
                print(f"[!] No credentials found for: {system}")
        
        elif choice == "3":
            manager.list_systems()
        
        elif choice == "4":
            manager.save_credentials()
            break
        
        elif choice == "5":
            break
        
        else:
            print("[!] Invalid option")

if __name__ == "__main__":
    main()
