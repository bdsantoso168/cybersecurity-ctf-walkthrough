# Competition Walkthrough Guide

Complete step-by-step guide for the Cybersecurity Competition 2025

## Table of Contents

1. [Overview](#overview)
2. [Phase 1: Initial Access](#phase-1-initial-access)
3. [Phase 2: Lateral Movement](#phase-2-lateral-movement)
4. [Phase 3: Password Cracking](#phase-3-password-cracking)
5. [Phase 4: Final Validation](#phase-4-final-validation)

---

## Overview

**Competition Structure:**
- 10 progressive tasks
- 150 total points
- Multiple target systems
- Time-based completion

**Required Tools:**
- Microsoft Remote Desktop
- Terminal/Command Prompt
- Network scanning tools
- Password cracking utilities

---

## Phase 1: Initial Access (80 points)

### Task 1: Remote Connection (10 points)

**Objective:** Establish RDP connection to primary target

**Steps:**

1. **Discover Target IP**
```bash
   # Scan network
   arp -a | grep 192.168.0
   
   # Ping target
   ping -c 2 192.168.0.XXX
```

2. **Connect via RDP**
   - Open Microsoft Remote Desktop
   - Add PC: `192.168.0.XXX`
   - Enter credentials
   - Connect

**Success Criteria:** Desktop access achieved

---

### Task 2: Folder Renaming (20 points)

**Objective:** Find and rename team folder

**Steps:**

1. Navigate to designated folder location
2. Find folder matching pattern: "Team XX RENAME"
3. Right-click → Rename
4. Change to: "Team XX [YourTeamName]"
5. Note completion time

**Tips:**
- Use file search if needed
- Document exact timestamp
- Verify correct folder before renaming

---

### Task 3: IP Documentation (20 points)

**Objective:** Extract and save IP configuration

**Windows Commands:**
```cmd
# Open Command Prompt
Windows + R → cmd → Enter

# Get IP configuration
ipconfig

# Note IPv4 Address
```

**Deliverable:**
- Create `IP_Address.txt`
- Write IP address
- Save in team folder

---

### Task 4: Credential Discovery (30 points)

**Objective:** Find hidden 6-digit number and credentials

**Search Strategy:**

1. **Search for hidden files**
   - Look for text files
   - Check protected/hidden attributes
   - Search for pattern: "secret*"

2. **Document findings**
Expected format:
  - 6-digit number
  - Username
  - Email
  - Password

3. **Save information securely**
   - Will be needed for next phase!

---

## Phase 2: Lateral Movement (20 points)

### Task 5: Secondary System Access (10 points)

**Objective:** Connect to SYSTEM-B using discovered credentials

**Challenge:** Credential Rotation

The hint "revolve" means: **swap which credential is username vs password**

**Process:**

1. **Discover SYSTEM-B IP**
```bash
   arp -a | grep 192.168.0
   # Look for hostname pattern
```

2. **Try credential combinations**
   - Original: user1 / pass1
   - Rotated: pass1 / user1
   - Continue rotating until success

3. **Connect via RDP**

---

### Task 6: Network Mapping (10 points)

**Objective:** Document complete network topology

**Collection Methods:**

**Method 1: ARP Scanning**
```bash
# Run comprehensive scan
arp -a | grep 192.168.0

# Populate ARP cache
for i in {1..254}; do
    ping -c 1 192.168.0.$i &
done
wait

# Re-scan
arp -a | grep 192.168.0
```

**Method 2: Direct System Query**
```cmd
# On each Windows system
ipconfig /all

# Note "Physical Address" (MAC)
```

**Required Data:**
| Computer Name | IP Address | MAC Address | OS |
|---------------|------------|-------------|-----|
| SYSTEM-A      | X.X.X.X    | XX:XX:XX... | Windows 10 |
| SYSTEM-B      | X.X.X.X    | XX:XX:XX... | Windows 10 |

**Deliverable:** `Network_Mapping.xls`

---

## Phase 3: Password Cracking (30 points)

### Task 7: Basic Password Crack (15 points)

**Target:** `Cyber.7z` (password-protected archive)

**Approach: Manual Testing**

**Common passwords to try:**
password
Password
PASSWORD
admin
[institution-name]
[year]

**Success Steps:**
1. Extract archive: `7z x Cyber.7z -p[password]`
2. Open extracted file
3. Write: Team name + completion time
4. Find and note 3-digit number

---

### Task 8: Advanced Password Crack (15 points)

**Target:** `Security.7z` (stronger password)

**Tool: John the Ripper**

**Complete Process:**

1. **Install Tools (macOS)**
```bash
   # Install Homebrew (if needed)
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   
   # Install tools
   brew install p7zip john-jumbo
```

2. **Extract Hash**
```bash
   7z2john Security.7z > security_hash.txt
```

3. **Create Custom Wordlist**
```bash
   cat > custom_wordlist.txt << EOF
   password
   [institution]
   [institution]1906
   Security
   security
   cyber
   EOF
```

4. **Crack Password**
```bash
   # Try custom wordlist
   john --wordlist=custom_wordlist.txt security_hash.txt
   
   # Show result
   john --show security_hash.txt
```

5. **Extract Archive**
```bash
   7z x Security.7z -p[cracked_password]
```

6. **Complete Task**
   - Write team name + time
   - Find and note 4-digit number

---

## Phase 4: Final Validation (20 points)

### Task 9: Validation Code (10 points)

**Objective:** Combine discovered numbers

**Formula:**
Validation Code = [3-digit from Task 7] + [4-digit from Task 8]
Example: 123 + 4567 = 1234567

**Submit:** Enter 7-digit code in competition portal

---

### Task 10: Final Submission (10 points)

**Checklist:**
✅ Required Files in Team Folder:
□ IP_Address.txt (Task 3)
□ Network_Mapping.xls (Task 6)
□ Completed Cyber file (Task 7)
□ Completed Security file (Task 8)
✅ Verification:
□ All files have team name
□ All files have completion times
□ Validation code submitted
□ Professor notified
✅ System Cleanup:
□ Logged off from all systems
□ Notes saved locally
□ Screenshots captured (optional)

---

## Quick Reference Commands

### macOS Terminal

**Network Scanning:**
```bash
# ARP scan
arp -a | grep 192.168.0

# Ping sweep
for i in {1..254}; do ping -c 1 192.168.0.$i & done; wait

# Single ping
ping -c 2 192.168.0.XXX
```

**Password Cracking:**
```bash
# Extract hash
7z2john file.7z > hash.txt

# Crack with wordlist
john --wordlist=wordlist.txt hash.txt

# Show cracked password
john --show hash.txt
```

### Windows Command Prompt

**Network Configuration:**
```cmd
# Basic IP info
ipconfig

# Detailed info (includes MAC)
ipconfig /all

# ARP cache
arp -a

# Test connection
ping 192.168.0.XXX
```

---

## Success Strategies

### Time Management
1. Start with quick wins (Task 1, 2, 3)
2. Document as you go
3. Don't get stuck - move on and return
4. Ask for hints when needed

### Organization
- Keep credentials in secure notes
- Screenshot important findings
- Save files immediately
- Use consistent naming

### Problem Solving
- Try obvious solutions first
- Read hints carefully ("revolve" = rotate)
- Listen to other teams (carefully)
- Use available tools efficiently

---

## Troubleshooting

### Can't Connect via RDP
- Verify correct IP address
- Check credentials (case-sensitive)
- Ensure on correct network
- Try ping test first

### Password Not Cracking
- Verify hash extraction
- Try simpler passwords first
- Check wordlist format
- Increase timeout/attempts

### Can't Find Files
- Use Windows search
- Check hidden files
- Look in team folder first
- Ask for hint on location

---

## Post-Competition

### Documentation
- Export network map
- Save all notes
- Document lessons learned
- Create timeline of events

### Analysis
- What worked well?
- What could improve?
- Which techniques were most effective?
- How to prepare better next time?

---

**Good luck! Remember: Document everything, work systematically, and don't hesitate to ask for help!**
