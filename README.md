# 🔐 Cybersecurity Competition 2025 - Educational Documentation

> **⚠️ DISCLAIMER**: This repository is for **educational and personal project purposes only**. All sensitive information has been anonymized. This documentation demonstrates cybersecurity concepts and techniques learned during an academic competition.
<img width="2747" height="1372" alt="CyberSecurity Competition" src="https://github.com/user-attachments/assets/55cd6cf4-e77f-4e28-815a-539758e947c0" />

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Competition Structure](#-competition-structure)
- [Technical Environment](#-technical-environment)
- [Task Breakdown](#-task-breakdown)
  - [Phase 1: Initial Access (Tasks 1-4)](#phase-1-initial-access-tasks-1-4)
  - [Phase 2: Network Reconnaissance (Tasks 5-6)](#phase-2-network-reconnaissance-tasks-5-6)
  - [Phase 3: Password Cracking (Tasks 7-8)](#phase-3-password-cracking-tasks-7-8)
  - [Phase 4: Validation & Submission (Tasks 9-10)](#phase-4-validation--submission-tasks-9-10)
- [Tools & Technologies](#-tools--technologies)
- [Key Techniques](#-key-techniques)
- [Lessons Learned](#-lessons-learned)
- [Commands Reference](#-commands-reference)

---

## 🎯 Overview

This documentation covers a comprehensive cybersecurity competition that tested various practical skills including:

- **Network Discovery & Scanning**
- **Remote Access & Authentication**
- **Password Cracking & Cryptanalysis**
- **Network Mapping & Documentation**
- **File System Forensics**
- **Critical Thinking & Problem Solving**

**Competition Format:**
- **Total Points:** 150
- **Tasks:** 10 progressive challenges
- **Duration:** Single session
- **Environment:** Multi-computer network scenario
- **Platform:** Windows systems accessed via Remote Desktop from macOS

---

## 🏗️ Competition Structure

```
┌─────────────────────────────────────────────────────────────┐
│  Competition Network Architecture                           │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────┐         ┌──────────┐         ┌──────────┐    │
│  │ SYSTEM-A │◄───────►│ SYSTEM-B │◄───────►│ SYSTEM-C │    │
│  │ (80 pts) │         │ (50 pts) │         │ (20 pts) │    │
│  └──────────┘         └──────────┘         └──────────┘    │
│       ▲                     ▲                     ▲         │
│       │                     │                     │         │
│       └─────────────────────┴─────────────────────┘         │
│                             │                               │
│                    ┌────────┴────────┐                      │
│                    │   Attack Box    │                      │
│                    │  (macOS Client) │                      │
│                    └─────────────────┘                      │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Point Distribution

| Phase | Tasks | Points | Focus Area |
|-------|-------|--------|------------|
| Phase 1 | 1-4 | 80 | Initial Access & Reconnaissance |
| Phase 2 | 5-6 | 20 | Network Mapping & Lateral Movement |
| Phase 3 | 7-8 | 30 | Password Cracking & File Forensics |
| Phase 4 | 9-10 | 20 | Validation & Documentation |

---

## 💻 Technical Environment

### Attack Platform (Local Machine)
- **OS:** macOS
- **Tools:** Microsoft Remote Desktop, Terminal, Homebrew
- **Network:** Competition WiFi (Isolated Lab Network)

### Target Systems
- **Operating System:** Windows 10
- **Access Method:** Remote Desktop Protocol (RDP)
- **Network Range:** `192.168.0.0/24` (Private Class C)
- **Authentication:** Username/Password

### Network Topology
```
IP Range: 192.168.0.0/24
Gateway: 192.168.0.1
DNS: Competition Network DNS

Target Systems:
├── SYSTEM-A: 192.168.0.XXX
├── SYSTEM-B: 192.168.0.XXX
└── Additional devices discovered via scanning
```

---

## 📝 Task Breakdown

### Phase 1: Initial Access (Tasks 1-4)

#### Task 1: Remote Connection Establishment (10 points)
**Objective:** Establish initial RDP connection to primary target system

**Steps:**
1. **Network Discovery**
   ```bash
   # Scan local network for active hosts
   arp -a | grep 192.168.0
   
   # Ping potential targets
   ping -c 4 192.168.0.XXX
   ```

2. **RDP Connection**
   - Tool: Microsoft Remote Desktop
   - Configuration:
     - PC Name: `192.168.0.XXX`
     - Username: `[REDACTED]`
     - Password: `[REDACTED]`

**Success Criteria:** Successful desktop access to SYSTEM-A

---

#### Task 2: File System Reconnaissance (20 points)
**Objective:** Locate and rename team-specific folder

**Methodology:**
```
File System Navigation
├── Search for team-specific folders
├── Identify naming pattern: "Team [NUMBER] RENAME"
├── Rename folder to match team identifier
└── Document completion timestamp
```

**Skills Demonstrated:**
- File system navigation in Windows
- Understanding of access permissions
- Documentation practices

---

#### Task 3: IP Address Discovery & Documentation (20 points)
**Objective:** Extract and document network configuration

**Windows Command Prompt Commands:**
```cmd
# Launch Command Prompt
Windows Key + R → cmd → Enter

# Display network configuration
ipconfig

# Output Analysis
IPv4 Address: 192.168.0.XXX
Subnet Mask: 255.255.255.0
Default Gateway: 192.168.0.1
```

**Deliverable:**
- Create `IP_Address.txt`
- Document IPv4 address
- Save in team folder

**Key Learning:** Understanding network interface configuration and documentation standards

---

#### Task 4: File Forensics & Credential Discovery (30 points)
**Objective:** Locate hidden credentials for lateral movement

**Investigation Process:**
```
Forensics Workflow
├── Search for hidden/protected files
├── Examine file attributes
├── Locate "secret" text file
└── Extract embedded data
```

**File Contents Discovered:**
```
╔════════════════════════════════════╗
║  DISCOVERED CREDENTIALS            ║
╠════════════════════════════════════╣
║  Numeric Code: [6-DIGIT NUMBER]    ║
║  Username: [REDACTED]              ║
║  Email: [REDACTED]                 ║
║  Password: [REDACTED]              ║
╚════════════════════════════════════╝
```

**Critical Note:** These credentials are essential for Phase 2 lateral movement

---

### Phase 2: Network Reconnaissance (Tasks 5-6)

#### Task 5: Lateral Movement to SYSTEM-B (10 points)
**Objective:** Use discovered credentials to access secondary system

**Challenge:** Credential Transformation
```
🔐 CREDENTIAL ROTATION PUZZLE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Hint from instructor: "Revolve the credentials"

Original Set (from Task 4):
├── Field 1: [REDACTED]
├── Field 2: [REDACTED]
└── Field 3: [REDACTED]

Solution: Rotate which fields are used for username vs. password
```

**Network Discovery:**
```bash
# Identify SYSTEM-B on network
arp -a | grep 192.168.0

# Look for hostname patterns
# Result: system-b at 192.168.0.XXX
```

**Successful Connection:**
- IP: `192.168.0.XXX`
- Username: `[REDACTED]`
- Password: `[REDACTED]` (rotated from Task 4)

---

#### Task 6: Complete Network Mapping (10 points)
**Objective:** Create comprehensive network topology map

**Reconnaissance Techniques:**

**Method 1: ARP Cache Analysis (Primary)**
```bash
# Full network scan
arp -a | grep 192.168.0

# Target-specific queries
ping -c 2 192.168.0.XXX
arp -a | grep 192.168.0.XXX
```

**Method 2: Direct System Query (Secondary)**
```cmd
# On each Windows system
ipconfig /all

# Extract Physical Address (MAC Address)
# Format: XX-XX-XX-XX-XX-XX
```

**MAC Address Background:**
```
┌─────────────────────────────────────────────────┐
│ MAC Address = Media Access Control Address     │
├─────────────────────────────────────────────────┤
│ • Unique hardware identifier                   │
│ • 48-bit address (6 octets)                    │
│ • Assigned by manufacturer                     │
│ • Format: XX:XX:XX:XX:XX:XX or XX-XX-XX-XX-XX-XX│
│ • First 3 octets = Manufacturer (OUI)          │
│ • Last 3 octets = Device Serial                │
└─────────────────────────────────────────────────┘
```

**Network Mapping Results:**

| System ID | IP Address | MAC Address | OS | Status |
|-----------|------------|-------------|-----|--------|
| SYSTEM-A | 192.168.0.XXX | [REDACTED] | Windows 10 | Active |
| SYSTEM-B | 192.168.0.XXX | [REDACTED] | Windows 10 | Active |
| DEVICE-1 | 192.168.0.XXX | [REDACTED] | Unknown | Detected |
| DEVICE-2 | 192.168.0.XXX | [REDACTED] | Unknown | Detected |

**Deliverable:** `Network_Mapping.xls` with complete device inventory

---

### Phase 3: Password Cracking (Tasks 7-8)

#### Task 7: Basic Password Cracking (15 points)
**Objective:** Decrypt password-protected archive (moderate difficulty)

**Target:** `Cyber.7z` (7-Zip compressed archive)

**Attack Methodology:**
```
Password Cracking Strategy - Level 1
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Manual Testing
   ├── Common passwords
   ├── Competition-related terms
   └── Default passwords

2. Success Vector
   └── Password: "password" (classic weak password)
```

**Successful Extraction:**
```bash
# 7-Zip extraction with password
7z x Cyber.7z -p[password]
```

**File Contents:**
- Required to document: Team name, completion timestamp
- Hidden data: **3-digit number** (required for Task 9)

**Security Lesson:** Demonstrates importance of strong passwords vs. common/default credentials

---

#### Task 8: Advanced Password Cracking (15 points)
**Objective:** Crack stronger password using automated tools

**Target:** `Security.7z` (hardened archive)

**Tools Used:**
```
┌─────────────────────────────────────┐
│  John the Ripper                    │
│  "The Swiss Army Knife of          │
│   Password Cracking"                │
├─────────────────────────────────────┤
│  • Dictionary attacks               │
│  • Brute force                      │
│  • Hybrid attacks                   │
│  • Custom wordlists                 │
└─────────────────────────────────────┘
```

**Installation (macOS):**
```bash
# Install Homebrew (if needed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install required tools
brew install p7zip john-jumbo
```

**Attack Process:**

**Step 1: Hash Extraction**
```bash
# Extract password hash from archive
7z2john Security.7z > security_hash.txt

# View hash format
cat security_hash.txt
```

**Step 2: Create Custom Wordlist**
```bash
# Build context-specific wordlist
cat > passwords.txt << EOF
password
Password
PASSWORD
[institution-name]
[institution-name]1906
security
Security
cyber
Cyber
EOF
```

**Step 3: Execute Cracking Attack**
```bash
# Dictionary attack with custom wordlist
john --wordlist=passwords.txt security_hash.txt

# Alternative: Use system dictionary
john --wordlist=/usr/share/dict/words security_hash.txt

# View cracked password
john --show security_hash.txt
```

**Step 4: Decrypt and Extract**
```bash
# Use cracked password to extract
7z x Security.7z -p[CRACKED_PASSWORD]
```

**File Contents:**
- Required documentation: Team name, timestamp
- Hidden data: **4-digit number** (required for Task 9)

**Advanced Techniques Learned:**
- Hash extraction from encrypted containers
- Custom wordlist generation
- Context-aware password guessing
- John the Ripper configuration

---

### Phase 4: Validation & Submission (Tasks 9-10)

#### Task 9: Password Validation Code (10 points)
**Objective:** Combine discovered numbers to create validation code

**Algorithm:**
```
Validation Code Generation
━━━━━━━━━━━━━━━━━━━━━━━━━

Input:
├── Task 7 Result: [3-digit number]
└── Task 8 Result: [4-digit number]

Process:
Concatenate: [3-digit] + [4-digit]

Output:
└── 7-digit validation code
```

**Example:**
```
If Task 7 = 123 and Task 8 = 4567
Then Validation Code = 1234567
```

**Submission:** Enter validation code in competition portal

---

#### Task 10: Final Documentation & Submission (10 points)
**Objective:** Ensure all deliverables are properly documented and submitted

**Submission Checklist:**
```
✅ DELIVERABLES VERIFICATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━

Required Files:
├── ✓ IP_Address.txt (Task 3)
├── ✓ Network_Mapping.xls (Task 6)
├── ✓ Cyber_[extracted] (Task 7)
├── ✓ Security_[extracted] (Task 8)
└── ✓ Validation code submitted (Task 9)

Metadata Requirements:
├── ✓ Team identification on all files
├── ✓ Completion timestamps recorded
└── ✓ All files in designated team folder

System Cleanup:
├── ✓ Proper logoff from all systems
├── ✓ No sensitive data on local machine
└── ✓ Competition portal submission confirmed
```

---

## 🛠️ Tools & Technologies

### Network Reconnaissance
```
┌─────────────────────────────────────────┐
│  ARP (Address Resolution Protocol)      │
├─────────────────────────────────────────┤
│  Command: arp -a                        │
│  Purpose: Map IP to MAC addresses       │
│  Use Case: Network device discovery     │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│  PING (ICMP Echo)                       │
├─────────────────────────────────────────┤
│  Command: ping -c [count] [IP]          │
│  Purpose: Test host reachability        │
│  Use Case: Validate active targets      │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│  IPCONFIG / IFCONFIG                    │
├─────────────────────────────────────────┤
│  Command: ipconfig /all (Windows)       │
│  Purpose: Network interface details     │
│  Use Case: Configuration documentation  │
└─────────────────────────────────────────┘
```

### Remote Access
```
┌─────────────────────────────────────────┐
│  Microsoft Remote Desktop (RDP)         │
├─────────────────────────────────────────┤
│  Protocol: RDP (Port 3389)              │
│  Platform: macOS → Windows              │
│  Authentication: Username/Password      │
│  Use Case: Remote system access         │
└─────────────────────────────────────────┘
```

### Password Cracking
```
┌─────────────────────────────────────────┐
│  John the Ripper                        │
├─────────────────────────────────────────┤
│  Type: Password cracker                 │
│  Attacks: Dictionary, brute force       │
│  Version: john-jumbo (community)        │
│  Use Case: Encrypted archive cracking   │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│  7z2john                                │
├─────────────────────────────────────────┤
│  Type: Hash extraction utility          │
│  Purpose: Convert 7z to John format     │
│  Input: Encrypted .7z file              │
│  Output: Crackable hash                 │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│  p7zip                                  │
├─────────────────────────────────────────┤
│  Type: Archive manager                  │
│  Purpose: Extract 7z files              │
│  Command: 7z x [file] -p[password]      │
│  Use Case: Archive extraction           │
└─────────────────────────────────────────┘
```

---

## 🔑 Key Techniques

### 1. Network Scanning & Enumeration
**Concept:** Discover active hosts and services on a network

**Implementation:**
```bash
# Passive reconnaissance
arp -a | grep [subnet]

# Active scanning
for ip in {1..254}; do
    ping -c 1 192.168.0.$ip &
done
wait

# Enumerate discovered hosts
arp -a | grep 192.168.0
```

**Applications:**
- Asset discovery
- Network mapping
- Security assessment
- Penetration testing

---

### 2. Credential Rotation/Transformation
**Concept:** Systematically trying different credential combinations

**Strategy:**
```
Original Credentials:
├── Field A: [value1]
├── Field B: [value2]
└── Field C: [value3]

Rotation Attempts:
├── Combination 1: username=[A], password=[B]
├── Combination 2: username=[B], password=[C]
├── Combination 3: username=[A], password=[C]
└── Continue until successful
```

**Real-World Relevance:**
- Password reuse patterns
- Multi-factor authentication testing
- Social engineering defenses

---

### 3. Dictionary Attack
**Concept:** Automated password guessing using wordlists

**Effectiveness Factors:**
```
Success Rate Depends On:
├── Wordlist quality (context-specific terms)
├── Target password complexity
├── Password length
└── Character set used
```

**Wordlist Strategy:**
```bash
# Generic dictionary
john --wordlist=/usr/share/dict/words hash.txt

# Custom contextual wordlist
cat > custom.txt << EOF
[organization-name]
[common-terms]
[date-variations]
EOF

john --wordlist=custom.txt hash.txt
```

---

### 4. MAC Address Analysis
**Concept:** Using hardware addresses for device identification

**MAC Address Structure:**
```
XX:XX:XX:XX:XX:XX
└─┬─┘ └────┬────┘
  │        │
  │        └─ Device Serial (NIC-specific)
  └─ OUI (Organizationally Unique Identifier)
     Identifies manufacturer
```

**Use Cases:**
- Device fingerprinting
- Network access control (MAC filtering)
- Physical security tracking
- Vendor identification

**OUI Lookup Example:**
```
MAC: 00:0C:29:XX:XX:XX
OUI: 00:0C:29 → VMware, Inc.
Conclusion: Virtual machine detected
```

---

### 5. Hash Extraction & Cracking
**Concept:** Convert encrypted data to crackable format

**Process Flow:**
```
┌──────────────┐     ┌───────────┐     ┌──────────────┐
│  Encrypted   │────>│  Extract  │────>│   Crackable  │
│  Container   │     │   Hash    │     │   Hash File  │
└──────────────┘     └───────────┘     └──────────────┘
                                              │
                                              ▼
                                       ┌─────────────┐
                                       │   Cracking  │
                                       │   Attack    │
                                       └─────────────┘
                                              │
                                              ▼
                                       ┌─────────────┐
                                       │  Plaintext  │
                                       │  Password   │
                                       └─────────────┘
```

**Common Hash Types:**
- MD5 (weak, legacy)
- SHA-1 (deprecated)
- SHA-256 (modern)
- bcrypt (recommended)
- PBKDF2 (password storage)

---

## 💡 Lessons Learned

### Security Insights

#### 1. **Password Security**
```
❌ WEAK PRACTICES                ✅ STRONG PRACTICES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• password                      • xK9$mP2#vQ8@wL5!nF3
• [name]123                     • Unique per service
• [organization-name]           • 16+ characters
• Dictionary words              • Multi-factor authentication
• Common patterns               • Password manager
```

**Recommendations:**
- Minimum 16 characters
- Mix of uppercase, lowercase, numbers, symbols
- No dictionary words or personal information
- Unique password per service
- Enable MFA wherever possible

---

#### 2. **Network Security**
```
DEFENSE IN DEPTH LAYERS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Layer 1: Perimeter Security
├── Firewall rules
├── IDS/IPS
└── Network segmentation

Layer 2: Access Control
├── Strong authentication
├── Principle of least privilege
└── Multi-factor authentication

Layer 3: Monitoring & Detection
├── SIEM (Security Information & Event Management)
├── Log analysis
└── Anomaly detection

Layer 4: Response & Recovery
├── Incident response plan
├── Regular backups
└── Disaster recovery procedures
```

---

#### 3. **Operational Security (OPSEC)**

**What We Learned:**
```
DO:
✓ Document all actions with timestamps
✓ Maintain detailed network maps
✓ Secure credential storage
✓ Follow proper disconnection procedures
✓ Clean up after operations

DON'T:
✗ Leave credentials in plaintext
✗ Forget to log activities
✗ Share sensitive data insecurely
✗ Skip verification steps
✗ Rush through security controls
```

---

#### 4. **Reconnaissance Best Practices**

**Reconnaissance Pyramid:**
```
        ┌───────────────┐
        │   Exploitation │  ← Use discovered info
        ├───────────────┤
        │  Enumeration   │  ← Deep dive on targets
        ├───────────────┤
        │   Discovery    │  ← Find what's out there
        ├───────────────┤
        │   Planning     │  ← Define scope & goals
        └───────────────┘
```

**Key Principles:**
1. Start broad, then narrow focus
2. Document everything immediately
3. Verify findings before acting
4. Understand the environment before exploiting

---

### Technical Skills Developed

```
┌─────────────────────────────────────────────────┐
│  SKILL MATRIX                                   │
├──────────────────────┬──────────────────────────┤
│  Network Analysis    │  ████████████░░  80%     │
│  Password Cracking   │  ███████████░░░  75%     │
│  Remote Access       │  ██████████████  95%     │
│  File Forensics      │  ████████░░░░░░  70%     │
│  Documentation       │  ██████████████  90%     │
│  Problem Solving     │  ███████████░░░  85%     │
└──────────────────────┴──────────────────────────┘
```

**Practical Applications:**
- **System Administration:** Remote management, network configuration
- **Security Auditing:** Penetration testing, vulnerability assessment
- **Incident Response:** Forensics, log analysis
- **Network Engineering:** Topology mapping, device management

---

## 📚 Commands Reference

### macOS Terminal Commands

#### Network Discovery
```bash
# Display ARP cache (all entries)
arp -a

# Filter ARP cache for specific subnet
arp -a | grep 192.168.0

# Ping with count limit
ping -c 4 192.168.0.XXX

# Ping and update ARP cache in one command
ping -c 2 192.168.0.XXX && arp -a | grep 192.168.0.XXX

# Scan entire subnet (loop)
for ip in {1..254}; do ping -c 1 -W 1 192.168.0.$ip > /dev/null && echo "192.168.0.$ip is up"; done
```

#### Package Management (Homebrew)
```bash
# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install 7-Zip utilities
brew install p7zip

# Install John the Ripper (community version)
brew install john-jumbo

# Update Homebrew
brew update

# Upgrade installed packages
brew upgrade
```

#### Password Cracking
```bash
# Extract hash from 7z archive
7z2john file.7z > hash.txt

# Basic crack (default mode)
john hash.txt

# Dictionary attack with custom wordlist
john --wordlist=custom.txt hash.txt

# Dictionary attack with system dictionary
john --wordlist=/usr/share/dict/words hash.txt

# Show cracked passwords
john --show hash.txt

# Incremental mode (brute force)
john --incremental hash.txt

# Session management
john --session=mysession hash.txt        # Start named session
john --restore=mysession                 # Resume session
```

#### File Operations
```bash
# Extract 7z with password
7z x file.7z -p[password]

# List archive contents
7z l file.7z

# Extract with output directory
7z x file.7z -o/path/to/output

# Create password-protected archive
7z a -p[password] archive.7z files/
```

---

### Windows Command Prompt Commands

#### Network Configuration
```cmd
REM Display IP configuration
ipconfig

REM Display detailed network information
ipconfig /all

REM Display DNS cache
ipconfig /displaydns

REM Clear DNS cache
ipconfig /flushdns

REM Renew DHCP lease
ipconfig /renew

REM Release DHCP lease
ipconfig /release
```

#### Network Diagnostics
```cmd
REM Ping with count
ping -n 4 192.168.0.XXX

REM Continuous ping
ping -t 192.168.0.XXX

REM Display ARP cache
arp -a

REM Add static ARP entry
arp -s 192.168.0.XXX XX-XX-XX-XX-XX-XX

REM Delete ARP entry
arp -d 192.168.0.XXX

REM Trace route to destination
tracert google.com

REM Display routing table
route print
```

#### System Information
```cmd
REM Display system information
systeminfo

REM Display network connections
netstat -an

REM Display active connections with process ID
netstat -ano

REM Display network statistics
netstat -s

REM Display hostname
hostname

REM Display user information
whoami

REM Display environment variables
set
```

---

### Quick Command Cheatsheet

#### One-Liners for Common Tasks

**Find all devices on network (macOS):**
```bash
arp -a | grep 192.168.0
```

**Test if host is reachable (macOS):**
```bash
ping -c 1 192.168.0.XXX > /dev/null && echo "UP" || echo "DOWN"
```

**Get IP and MAC in one command (Windows):**
```cmd
ipconfig /all | findstr /i "IPv4 Physical"
```

**Quick password crack (if easy):**
```bash
7z2john file.7z | john --stdin
```

**Extract archive with password:**
```bash
7z x file.7z -ppassword
```

---

## 🎓 Educational Value

### Cybersecurity Concepts Covered

```
┌─────────────────────────────────────────────────────────┐
│  CIA TRIAD IN PRACTICE                                  │
├─────────────────────────────────────────────────────────┤
│                                                          │
│     ┌───────────────┐                                   │
│     │ CONFIDENTIALITY│                                   │
│     └───────┬───────┘                                   │
│             │                                            │
│   ┌─────────┼─────────┐                                │
│   │                   │                                 │
│   ▼                   ▼                                 │
│ ┌─────────┐     ┌──────────┐                           │
│ │INTEGRITY│     │AVAILABILITY│                          │
│ └─────────┘     └──────────┘                           │
│                                                          │
│  Competition demonstrated:                              │
│  • Confidentiality: Password protection, encryption     │
│  • Integrity: File verification, documentation          │
│  • Availability: System access, network connectivity    │
└─────────────────────────────────────────────────────────┘
```

### Real-World Applications
