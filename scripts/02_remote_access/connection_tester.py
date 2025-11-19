#!/usr/bin/env python3
"""
RDP Connection Tester
Tests connectivity and RDP availability for target systems
"""

import socket
import subprocess
import sys
from typing import Tuple

class ConnectionTester:
    def __init__(self, target_ip: str, rdp_port: int = 3389):
        self.target_ip = target_ip
        self.rdp_port = rdp_port
    
    def ping_test(self, count: int = 4) -> bool:
        """Test if host is reachable via ping"""
        print(f"[*] Pinging {self.target_ip}...")
        
        try:
            result = subprocess.run(
                ["ping", "-c", str(count), self.target_ip],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode == 0:
                # Parse ping statistics
                for line in result.stdout.split('\n'):
                    if 'packets transmitted' in line.lower():
                        print(f"    {line.strip()}")
                print("[✓] Host is reachable\n")
                return True
            else:
                print("[!] Host is not reachable\n")
                return False
        
        except subprocess.TimeoutExpired:
            print("[!] Ping timed out\n")
            return False
        except Exception as e:
            print(f"[!] Error during ping: {e}\n")
            return False
    
    def port_test(self, timeout: int = 5) -> bool:
        """Test if RDP port is open"""
        print(f"[*] Testing RDP port ({self.rdp_port})...")
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            
            result = sock.connect_ex((self.target_ip, self.rdp_port))
            sock.close()
            
            if result == 0:
                print(f"[✓] Port {self.rdp_port} is open\n")
                return True
            else:
                print(f"[!] Port {self.rdp_port} is closed or filtered\n")
                return False
        
        except socket.timeout:
            print(f"[!] Connection to port {self.rdp_port} timed out\n")
            return False
        except Exception as e:
            print(f"[!] Error during port test: {e}\n")
            return False
    
    def full_test(self) -> Tuple[bool, bool]:
        """Run full connectivity test"""
        print("="*60)
        print(f"  TESTING CONNECTION TO {self.target_ip}")
        print("="*60 + "\n")
        
        ping_ok = self.ping_test()
        port_ok = self.port_test()
        
        print("="*60)
        print("  TEST SUMMARY")
        print("="*60)
        print(f"Ping test:     {'✓ PASS' if ping_ok else '✗ FAIL'}")
        print(f"RDP port test: {'✓ PASS' if port_ok else '✗ FAIL'}")
        print("="*60 + "\n")
        
        if ping_ok and port_ok:
            print("[✓] System is ready for RDP connection!")
        elif ping_ok and not port_ok:
            print("[!] Host is reachable but RDP port is not accessible")
            print("    Check firewall settings or RDP service status")
        else:
            print("[!] System is not reachable")
        
        return ping_ok, port_ok

def main():
    print("""
╔═══════════════════════════════════════════════════════════╗
║         RDP CONNECTION TESTER - Competition Tool          ║
╚═══════════════════════════════════════════════════════════╝
    """)
    
    if len(sys.argv) < 2:
        print("Usage: python3 connection_tester.py <IP_ADDRESS> [RDP_PORT]")
        print("\nExample:")
        print("  python3 connection_tester.py 192.168.0.154")
        print("  python3 connection_tester.py 192.168.0.154 3389")
        sys.exit(1)
    
    target_ip = sys.argv[1]
    rdp_port = int(sys.argv[2]) if len(sys.argv) > 2 else 3389
    
    tester = ConnectionTester(target_ip, rdp_port)
    tester.full_test()

if __name__ == "__main__":
    main()
