```
 __     ______  _   _    ____ ___  _   _ _____ ____   ___  _     _     _____ ____  
 \ \   / /  _ \| \ | |  / ___/ _ \| \ | |_   _|  _ \ / _ \| |   | |   | ____|  _ \ 
  \ \ / /| |_) |  \| | | |  | | | |  \| | | | | |_) | | | | |   | |   |  _| | |_) |
   \ V / |  __/| |\  | | |__| |_| | |\  | | | |  _ <| |_| | |___| |___| |___|  _ < 
    \_/  |_|   |_| \_|  \____\___/|_| \_| |_| |_| \_\\___/|_____|_____|_____|_| \_\
```
VPN-CONTROLLER (IPSEC SCANNER)
A specialized Python automation tool designed to audit IPsec VPN endpoints. 
It automates the discovery of VPN servers using 'ike-scan', performing both 
Main Mode and Aggressive Mode tests to identify handshake vulnerabilities 
and capture pre-shared key (PSK) hashes for offline cracking.

**Features**
* **Dual-Mode Scanning:** Automatically performs both Main Mode and Aggressive Mode IKE scans.
* **Handshake Analysis:** Detects supported encryption and authentication transforms.
* **Automated PSK Cracking:** If a hash is captured in Aggressive Mode, it automatically attempts to crack it using 'psk-crack'.
* **Security Focused:** Uses `shlex` to safely handle target IP inputs against injection.
* **Interactive Interface:** Easy-to-use loop for scanning multiple targets in one session.

**Prerequisites**
The following tools are required for the script to function correctly:
* Python 3.x
* ike-scan: The primary IKE discovery and fingerprinting tool.
* psk-crack: Used for brute-forcing captured VPN hashes.
* Figlet: (The script attempts to install this automatically via apt).

**Installation**

Clone the repository:
   * git clone https://github.com/Tde99/VPN-Controller.git

Navigate to the directory:
   * cd VPN-Controller

Make the script executable:
   * chmod +x vpn_controller.py

**Usage**
VPN scanning requires low-level network socket access. Run with sudo:

sudo python3 vpn_controller.py

**How it Works:**
1. **Main Mode Scan:** Checks if the VPN gateway is alive and lists basic security parameters.
2. **Aggressive Mode Scan:** Attempts to force the server to send its authentication hash.

3. **Hash Capture:** If the server is misconfigured (Aggressive Mode enabled), the handshake hash is saved.
4. **Cracking:** The script triggers `psk-crack` to reveal the pre-shared password of the VPN tunnel.

**Important Notes:**
* **Root Privileges:** Required for packet manipulation and tool installation.
* **Misconfigurations:** Finding a VPN in Aggressive Mode is a high-risk finding in a security audit.
* **Ethics:** Use only for authorized testing. Unauthorized VPN scanning can trigger network alerts.
