# Tools & Commands Reference

Complete reference for all tools used in the competition

## Table of Contents

1. [Network Tools](#network-tools)
2. [Remote Access](#remote-access)
3. [Password Cracking](#password-cracking)
4. [File Operations](#file-operations)
5. [System Commands](#system-commands)

---

## Network Tools

### ARP (Address Resolution Protocol)

**Purpose:** View and manipulate ARP cache

**macOS/Linux:**
```bash
# View entire ARP cache
arp -a

# Filter for specific subnet
arp -a | grep 192.168.0

# Delete ARP entry
sudo arp -d 192.168.0.154

# Add static ARP entry
sudo arp -s 192.168.0.154 00:0c:29:46:d7:39
```

**Windows:**
```cmd
# View ARP cache
arp -a

# Delete entry
arp -d 192.168.0.154

# Add static entry
arp -s 192.168.0.154 00-0c-29-46-d7-39
```

---

### PING (ICMP Echo)

**Purpose:** Test network connectivity

**macOS/Linux:**
```bash
# Send 4 pings
ping -c 4 192.168.0.154

# Ping with timeout
ping -c 2 -W 2 192.168.0.154

# Flood ping (requires sudo)
sudo ping -f 192.168.0.154

# Ping sweep
for i in {1..254}; do
    ping -c 1 -W 1 192.168.0.$i > /dev/null 2>&1 && \
        echo "192.168.0.$i is up"
done
```

**Windows:**
```cmd
# Send 4 pings
ping -n 4 192.168.0.154

# Continuous ping
ping -t 192.168.0.154

# Ping with specific TTL
ping -i 64 192.168.0.154
```

---

### IPCONFIG / IFCONFIG

**Purpose:** Display network configuration

**Windows (ipconfig):**
```cmd
# Basic information
ipconfig

# Detailed information (includes MAC)
ipconfig /all

# Release DHCP lease
ipconfig /release

# Renew DHCP lease
ipconfig /renew

# Flush DNS cache
ipconfig /flushdns

# Display DNS cache
ipconfig /displaydns
```

**macOS/Linux (ifconfig):**
```bash
# All interfaces
ifconfig

# Specific interface
ifconfig en0

# Bring interface up
sudo ifconfig en0 up

# Bring interface down
sudo ifconfig en0 down

# Set IP address
sudo ifconfig en0 192.168.0.100 netmask 255.255.255.0
```

**macOS/Linux (ip command - modern):**
```bash
# Show all interfaces
ip addr show

# Show specific interface
ip addr show en0

# Show routing table
ip route show

# Add static route
sudo ip route add 192.168.1.0/24 via 192.168.0.1
```

---

## Remote Access

### Microsoft Remote Desktop

**Connection Setup:**
1. Open Microsoft Remote Desktop app
2. Click "Add PC" or "+" button
3. Enter configuration:
 - PC name: [IP address]
 - Username: [username]
 - (Password entered at connection)
4. Click "Add"
5. Double-click to connect

**Configuration Options:**
Display:

Resolution: Full screen / Custom
Optimize for: Retina / Standard

Devices & Audio:

Redirect audio
Redirect folders
Redirect printers

Advanced:

Connect to admin session
Swap mouse buttons
Use all monitors

**Keyboard Shortcuts:**
Command + Q        = Disconnect
Command + F        = Toggle full screen
Command + Option  = Windows key equivalent

---

## Password Cracking

### John the Ripper

**Purpose:** Password cracking tool

**Installation (macOS):**
```bash
# Using Homebrew
brew install john-jumbo

# Verify installation
john --help
which john
```

**Basic Usage:**
```bash
# Crack with default mode
john hash.txt

# Dictionary attack
john --wordlist=/path/to/wordlist.txt hash.txt

# Incremental (brute force)
john --incremental hash.txt

# Single crack mode
john --single hash.txt

# Show cracked passwords
john --show hash.txt

# Show formats
john --list=formats

# Specify format
john --format=Raw-MD5 hash.txt
```

**Session Management:**
```bash
# Start named session
john --session=mysession hash.txt

# Check status
john --status=mysession

# Restore session
john --restore=mysession

# List sessions
ls ~/.john/*.rec
```

**Custom Rules:**
```bash
# Apply rules to wordlist
john --wordlist=words.txt --rules hash.txt

# Specific rule
john --wordlist=words.txt --rules=Jumbo hash.txt
```

**Performance:**
```bash
# Show formats and speeds
john --test

# Use specific OpenCL device
john --devices=0 hash.txt

# Show progress
john --status
```

---

### 7z2john

**Purpose:** Extract password hash from 7z archives

**Usage:**
```bash
# Basic extraction
7z2john file.7z > hash.txt

# Multiple files
7z2john *.7z > hashes.txt

# View hash
cat hash.txt

# Format of output:
# filename:$7z$[parameters]$hash
```

**Then crack with John:**
```bash
# After extraction
john --wordlist=wordlist.txt hash.txt
john --show hash.txt
```

---

### 7-Zip (p7zip)

**Purpose:** Archive compression and extraction

**Installation (macOS):**
```bash
brew install p7zip
```

**Extraction:**
```bash
# Extract with password
7z x file.7z -pPASSWORD

# Extract without paths
7z e file.7z

# Extract to specific directory
7z x file.7z -o/path/to/output

# Test archive integrity
7z t file.7z
```

**Creation:**
```bash
# Create archive
7z a archive.7z files/

# Create with password
7z a -pPASSWORD secure.7z files/

# Create with encryption
7z a -mhe=on -pPASSWORD encrypted.7z files/

# Maximum compression
7z a -mx=9 compressed.7z files/
```

**Information:**
```bash
# List contents
7z l file.7z

# Show technical info
7z l -slt file.7z
```

---

## File Operations

### File Search

**Windows:**
```cmd
# Search by name
dir /s /b *secret*

# Search in specific directory
dir "C:\Users\*" /s /b *secret*

# Find hidden files
dir /a:h /s /b
```

**macOS/Linux:**
```bash
# Find by name
find . -name "*secret*"

# Find with case-insensitive
find . -iname "*secret*"

# Find hidden files
find . -name ".*"

# Find by extension
find . -name "*.txt"

# Find and execute command
find . -name "*.txt" -exec cat {} \;
```

---

### File Attributes

**Windows:**
```cmd
# Show attributes
attrib filename

# Set hidden
attrib +h filename

# Remove hidden
attrib -h filename

# Set read-only
attrib +r filename

# Show all files with attributes
attrib /s /d
```

**macOS/Linux:**
```bash
# List with details
ls -la

# Change permissions
chmod 755 file.sh

# Change owner
chown user:group file.txt

# Show file type
file filename
```

---

## System Commands

### Process Management

**Windows:**
```cmd
# List processes
tasklist

# Kill process by name
taskkill /IM process.exe /F

# Kill process by PID
taskkill /PID 1234 /F

# Task Manager
taskmgr
```

**macOS/Linux:**
```bash
# List processes
ps aux

# Kill process
kill -9 PID

# Kill by name
pkill processname

# Top processes
top

# Activity Monitor (macOS)
open -a "Activity Monitor"
```

---

### System Information

**Windows:**
```cmd
# System info
systeminfo

# Computer name
hostname

# User info
whoami

# Environment variables
set

# Network connections
netstat -an

# Routing table
route print
```

**macOS/Linux:**
```bash
# System info
uname -a

# Detailed info (macOS)
system_profiler SPHardwareDataType

# Hostname
hostname

# Current user
whoami

# Disk usage
df -h

# Memory usage
free -h  # Linux
vm_stat  # macOS

# Network connections
netstat -an

# Routing table
netstat -rn
```

---

## Scripting & Automation

### Bash Scripting

**Basic Script Structure:**
```bash
#!/bin/bash

# Variables
VAR="value"

# Functions
function my_function() {
    echo "Hello"
}

# Conditionals
if [ -f "file.txt" ]; then
    echo "File exists"
fi

# Loops
for i in {1..10}; do
    echo $i
done
```

**Useful Patterns:**
```bash
# Check if command exists
if command -v john &> /dev/null; then
    echo "John is installed"
fi

# Read file line by line
while IFS= read -r line; do
    echo "$line"
done < file.txt

# Parallel execution
for i in {1..254}; do
    ping -c 1 192.168.0.$i &
done
wait
```

---

### Python Scripting

**Basic Script Structure:**
```python
#!/usr/bin/env python3

import subprocess
import sys

def main():
    # Your code here
    pass

if __name__ == "__main__":
    main()
```

**Common Operations:**
```python
# Run system command
import subprocess
result = subprocess.run(['ls', '-la'], capture_output=True, text=True)
print(result.stdout)

# Read file
with open('file.txt', 'r') as f:
    content = f.read()

# Write file
with open('output.txt', 'w') as f:
    f.write("Hello\n")

# JSON handling
import json
data = {'key': 'value'}
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)
```

---

## Quick Reference Tables

### Common Ports

| Port | Service | Description |
|------|---------|-------------|
| 21   | FTP     | File Transfer |
| 22   | SSH     | Secure Shell |
| 23   | Telnet  | Remote Access (Insecure) |
| 80   | HTTP    | Web Traffic |
| 443  | HTTPS   | Secure Web |
| 3389 | RDP     | Remote Desktop |
| 445  | SMB     | File Sharing |

### IP Address Classes

| Class | Range | Default Mask | Private Range |
|-------|-------|--------------|---------------|
| A     | 1-126 | 255.0.0.0    | 10.0.0.0/8    |
| B     | 128-191 | 255.255.0.0 | 172.16.0.0/12 |
| C     | 192-223 | 255.255.255.0 | 192.168.0.0/16 |

### File Extensions

| Extension | Type | Purpose |
|-----------|------|---------|
| .7z

