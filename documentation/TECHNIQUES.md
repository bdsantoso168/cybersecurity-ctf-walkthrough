# Cybersecurity Techniques Reference

Detailed explanation of techniques used in the competition

## Table of Contents

1. [Network Reconnaissance](#network-reconnaissance)
2. [Authentication Techniques](#authentication-techniques)
3. [Password Cracking](#password-cracking)
4. [Network Mapping](#network-mapping)
5. [File Forensics](#file-forensics)

---

## Network Reconnaissance

### ARP Scanning

**Concept:** Address Resolution Protocol (ARP) maps IP addresses to MAC addresses

**How it works:**
Your computer maintains an ARP cache
When devices communicate, ARP entries are created
Scanning the cache reveals active devices
Ping sweeps populate the cache

**Implementation:**
```bash
# View ARP cache
arp -a

# Filter for subnet
arp -a | grep 192.168.0

# Populate cache first
for ip in {1..254}; do
    ping -c 1 -W 1 192.168.0.$ip > /dev/null 2>&1 &
done
wait

# Then scan
arp -a | grep 192.168.0
```

**Advantages:**
- Fast and stealthy
- No special privileges needed
- Works on local network
- Non-intrusive

**Limitations:**
- Only discovers local network devices
- May miss devices with strict firewalls
- Cache may be incomplete

---

### Ping Sweeps

**Concept:** Send ICMP echo requests to discover active hosts

**How it works:**
Send ping (ICMP echo request) to IP
Active host replies with echo response
No reply = host down or blocking ICMP
Populate ARP cache as side effect

**Implementation:**
```bash
# Single ping
ping -c 1 192.168.0.154

# Sweep range
for i in {1..254}; do
    ping -c 1 -W 1 192.168.0.$i > /dev/null 2>&1 && \
        echo "192.168.0.$i is up"
done
```

**Best Practices:**
- Use short timeout (-W 1)
- Run in parallel (&)
- Combine with ARP scan
- Log results

---

## Authentication Techniques

### Credential Rotation

**Concept:** Systematically try different combinations of authentication fields

**The "Revolve" Technique:**

When given multiple credential fields:
Field A: username1
Field B: email@domain
Field C: password1

Try all combinations:
Attempt 1: username=A, password=B
Attempt 2: username=A, password=C
Attempt 3: username=B, password=A
Attempt 4: username=B, password=C
Attempt 5: username=C, password=A
Attempt 6: username=C, password=B

**Implementation Pattern:**
```python
credentials = ['value1', 'value2', 'value3']

for username in credentials:
    for password in credentials:
        if username != password:
            attempt_login(username, password)
```

**Real-World Application:**
- Password reuse across systems
- Username/password confusion
- Email as username scenarios
- Testing credential validity

---

### Remote Desktop Protocol (RDP)

**Concept:** Microsoft protocol for remote Windows access

**Connection Details:**
- Default Port: 3389
- Protocol: TCP
- Requires: Username + Password
- GUI access to remote system

**Security Considerations:**
Strengths:
✓ Encrypted connection
✓ Built-in to Windows
✓ Full desktop access
Weaknesses:
✗ Brute-force target
✗ Version vulnerabilities
✗ Firewall must allow
✗ Account lockout risk

---

## Password Cracking

### Dictionary Attacks

**Concept:** Try passwords from a pre-compiled list

**How it works:**
1. Load wordlist (dictionary)
- For each word in list:

2. Hash the word
- Compare to target hash
- If match: password found

3. Continue until match or list exhausted

**Wordlist Strategy:**

**Generic Wordlist:**
password
123456
qwerty
admin
letmein

**Context-Specific:**
[institution-name]
[institution-name]1906
Security
cyber
[team-name]

**With Variations:**
```python
base_word = "security"
variations = [
    base_word.lower(),      # security
    base_word.upper(),      # SECURITY
    base_word.capitalize(), # Security
    base_word + "123",      # security123
    base_word + "1906",     # security1906
]
```

**Effectiveness Factors:**
- Wordlist quality
- Context awareness
- Common patterns
- Password complexity

---

### Hash Extraction

**Concept:** Extract password hash from encrypted container

**Process:**
┌─────────────┐
│  Encrypted  │
│   Archive   │
│ (file.7z)   │
└──────┬──────┘
│
▼
[7z2john]
│
▼
┌──────────────┐
│ Password Hash│
│  (crackable) │
└──────┬───────┘
│
▼
[John the
Ripper]
│
▼
┌──────────────┐
│   Plaintext  │
│   Password   │
└──────────────┘

**Implementation:**
```bash
# Step 1: Extract hash
7z2john file.7z > hash.txt

# Step 2: Crack hash
john --wordlist=wordlist.txt hash.txt

# Step 3: Show password
john --show hash.txt
```

---

### John the Ripper Modes

**1. Dictionary Mode:**
```bash
# Use wordlist
john --wordlist=words.txt hash.txt

# Faster, requires good wordlist
```

**2. Incremental Mode (Brute Force):**
```bash
# Try all combinations
john --incremental hash.txt

# Slower, but comprehensive
```

**3. Single Crack Mode:**
```bash
# Use known information
john --single hash.txt

# Fast, good first attempt
```

**4. Rules Mode:**
```bash
# Apply transformation rules
john --wordlist=words.txt --rules hash.txt

# Variations like: p@ssw0rd, PASSWORD123
```

---

## Network Mapping

### MAC Address Analysis

**Concept:** Use hardware addresses to identify devices

**MAC Address Structure:**
XX:XX:XX:YY:YY:YY
└─OUI──┘ └─NIC──┘
OUI = Organizationally Unique Identifier (Manufacturer)
NIC = Network Interface Controller (Device Serial)

**Vendor Identification:**
00:0C:29 → VMware
00:50:56 → VMware
08:00:27 → VirtualBox
00:1A:A0 → Dell
00:1B:21 → Intel

**Use Cases:**
- Identify virtual machines
- Detect device manufacturer
- Physical security tracking
- Network access control

---

### Topology Mapping

**Concept:** Document network structure and relationships

**Key Elements:**
1. Devices
  Hostnames
  IP addresses
  MAC addresses
  Operating systems

2. Connections
  Gateway/router
  Network segments
  Interconnections

3. Services
  Open ports
  Running services
  Protocols used

**Documentation Format:**
Gateway (192.168.0.1)
├── Device A (192.168.0.154)
│   ├── Hostname: SYSTEM-A
│   ├── MAC: XX:XX:XX:XX:XX:XX
│   └── OS: Windows 10
├── Device B (192.168.0.161)
│   ├── Hostname: SYSTEM-B
│   ├── MAC: YY:YY:YY:YY:YY:YY
│   └── OS: Windows 10

---

## File Forensics

### Hidden File Detection

**Common Hiding Techniques:**

**1. Hidden Attribute (Windows):**
```cmd
# View hidden files
attrib

# Show hidden files
dir /a:h

# Unhide file
attrib -h filename
```

**2. Dot Files (Unix):**
```bash
# Hidden files start with .
ls -la

# Show all files including hidden
ls -A
```

**3. Alternate Data Streams (Windows):**
```cmd
# View streams
dir /r

# Read stream
more < file.txt:stream
```

**Search Strategies:**
- Check common hiding locations
- Search by pattern
- Use file search tools
- Check file attributes
- Look in system folders

---

### Archive Extraction

**7-Zip Operations:**

**With Known Password:**
```bash
# Extract
7z x file.7z -pPASSWORD

# List contents
7z l file.7z
```

**Without Password:**
```bash
# Extract hash for cracking
7z2john file.7z > hash.txt

# Crack it
john hash.txt

# Then extract with found password
```

---

## Security Best Practices

### Defense Strategies

**Against Network Scanning:**
✓ Firewall rules
✓ IDS/IPS systems
✓ Network segmentation
✓ MAC filtering

**Against Password Attacks:**
✓ Strong passwords (16+ chars)
✓ Password complexity
✓ Account lockout policies
✓ Multi-factor authentication
✓ Password managers

**Against File Forensics:**
✓ Encryption
✓ Access controls
✓ Audit logging
✓ Secure deletion

---

## Ethical Considerations

### Legal Framework

**Authorized Testing Only:**
- Written permission required
- Clear scope definition
- Respect boundaries
- Follow rules of engagement

**This Competition:**
- Educational environment
- Controlled setting
- Supervised activity
- Documented permissions

**Never In Real World Without:**
- Explicit authorization
- Legal documentation
- Professional oversight
- Ethical guidelines

---

**Remember: These techniques are powerful. Use them responsibly and ethically!**
