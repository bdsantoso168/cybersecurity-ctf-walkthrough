# Cybersecurity CTF Competition - Complete Walkthrough

> 🎓 Educational documentation of a hands-on cybersecurity capture-the-flag competition demonstrating network reconnaissance, authentication techniques, password cracking, and system administration skills.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS-blue)]()

---

## 📋 Table of Contents

- [Overview](#overview)
- [Competition Structure](#competition-structure)
- [Skills Demonstrated](#skills-demonstrated)
- [Tools & Technologies](#tools--technologies)
- [Challenge Walkthrough](#challenge-walkthrough)
- [Key Learnings](#key-learnings)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Security & Ethics](#security--ethics)
- [Resources](#resources)

---

## 🎯 Overview

This repository documents my methodology and problem-solving approach during a university cybersecurity CTF competition. The competition involved multiple phases of increasing difficulty, requiring both technical skills and creative problem-solving.

**Competition Scope:**
- Network reconnaissance and device discovery
- Remote access via RDP to Windows machines
- Credential discovery through file analysis
- Password cracking using automated tools
- Network mapping and comprehensive documentation
- System administration on remote Windows systems

**My Results:**
- ✅ Completed all 10 tasks successfully
- 🏆 Successfully cracked passwords using John the Ripper
- 📊 Mapped entire network topology with IP/MAC addresses
- ⏱️ Finished within competition time limit

---

## 🏗️ Competition Structure

The competition consisted of 4 progressive phases:

### Phase 1: Initial Access (Tasks 1-4)
- Discover target computers on local network
- Establish remote desktop connections
- Navigate Windows file systems
- Extract hidden credential information

### Phase 2: Lateral Movement (Task 5-6)
- Access additional systems with discovered credentials
- Apply creative authentication techniques
- Map entire network infrastructure
- Document all discovered devices

### Phase 3: Password Cracking (Tasks 7-8)
- Crack easy password-protected archives
- Use advanced tools for difficult passwords
- Create custom wordlists
- Extract sensitive information from secured files

### Phase 4: Validation (Tasks 9-10)
- Combine discovered information
- Generate validation codes
- Complete documentation
- Submit final results

---

## 💪 Skills Demonstrated

### Technical Competencies

**Network Security:**
- ✅ ARP cache analysis for device discovery
- ✅ Ping sweeps and connectivity testing
- ✅ MAC address identification and tracking
- ✅ Network topology mapping

**System Administration:**
- ✅ Windows command-line proficiency
- ✅ macOS Terminal expertise
- ✅ Remote Desktop Protocol (RDP) configuration
- ✅ System information extraction (`ipconfig`, `ifconfig`)

**Offensive Security:**
- ✅ Password cracking with John the Ripper
- ✅ Hash extraction from archives
- ✅ Custom wordlist creation
- ✅ Dictionary and brute-force attacks

**Documentation:**
- ✅ Technical writing and process documentation
- ✅ Network diagrams and mapping
- ✅ Command reference creation
- ✅ Knowledge base development

### Security Concepts Learned

- 🔐 **ARP (Address Resolution Protocol)** - Mapping IP to MAC addresses
- 🔐 **MAC Addresses** - Hardware identification on networks
- 🔐 **Password Hashing** - One-way cryptographic functions
- 🔐 **Lateral Movement** - Moving between systems in a network
- 🔐 **OSINT Techniques** - Information gathering from available sources
- 🔐 **Authentication Bypass** - Creative credential usage patterns

---

## 🛠️ Tools & Technologies

| Tool | Purpose | Platform |
|------|---------|----------|
| **Microsoft Remote Desktop** | Remote Windows access | macOS |
| **ARP** | Network device discovery | macOS/Windows |
| **John the Ripper** | Password hash cracking | macOS |
| **7-Zip (p7zip)** | Archive extraction and manipulation | macOS/Windows |
| **ipconfig / ifconfig** | Network configuration queries | Windows/macOS |
| **ping** | Network connectivity testing | Both |
| **Homebrew** | Package management | macOS |
| **Command Prompt** | Windows system administration | Windows |
| **Terminal** | macOS command-line interface | macOS |

---

## 🚀 Challenge Walkthrough

### 🔹 Tasks 1-4: Initial System Access

**Challenge:** Discover and connect to first target computer without prior knowledge of IP address.

**Approach:**

1. **Network Discovery**
   ```bash
   # Scan local network using ARP
   arp -a | grep 192.168.1
   
   # Test connectivity
   ping -c 2 [TARGET_IP]
