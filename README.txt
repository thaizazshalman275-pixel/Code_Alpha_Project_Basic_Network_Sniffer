
==============================================================
          NETWORK PACKET SNIFFER (Scapy-Based)
       Real-Time HTTP/HTTPS Traffic Analyzer
==============================================================
  Author   : 
  Program  : 
  Platform : Windows (PowerShell)
  Level    : Beginner to Intermediate
  Purpose  : Cybersecurity Learning Project
==============================================================


--------------------------------------------------------------
  OVERVIEW
--------------------------------------------------------------

  Network Packet Sniffer is a Python-based cybersecurity
  project that captures and analyzes live network traffic
  in real time.

  Using the Scapy library, this tool:
    - Filters only HTTP (port 80) and HTTPS (port 443) traffic
    - Displays live packet logs directly in your terminal
    - Tracks which IP addresses are most active
    - Automatically stops after a set number of packets
    - Prints a final network analysis report on exit

  This project is designed to help you understand how network
  traffic flows at the packet level — similar to how tools
  like Wireshark work under the hood.


--------------------------------------------------------------
  FEATURES
--------------------------------------------------------------

    [+] Live packet capture using Scapy's sniffing engine
    [+] Filters only HTTP (port 80) and HTTPS (port 443)
    [+] Real-time terminal logs — structured and readable
    [+] Per-packet details displayed:
          - Timestamp
          - Source IP and Port
          - Destination IP and Port
          - Protocol (HTTP or HTTPS)
    [+] Total packet counter
    [+] Most active IP address tracker
    [+] Auto-stops after 50 packets (configurable)
    [+] Final network report printed on completion


--------------------------------------------------------------
  SAMPLE OUTPUT
--------------------------------------------------------------

  ============================================================
         NETWORK PACKET SNIFFER — Starting Capture
  ============================================================

  2026-06-04 23:18:39 | Packet  1 | 192.168.1.5:443 → 8.8.8.8:54017    | HTTPS
  2026-06-04 23:18:40 | Packet  2 | 192.168.1.5:80  → 142.250.4.99:512 | HTTP
  2026-06-04 23:18:41 | Packet  3 | 192.168.1.5:443 → 172.217.0.14:443 | HTTPS
  ...

  ============================================================
                FINAL NETWORK ANALYSIS REPORT
  ============================================================
    Total Packets Captured : 50
    HTTP  Packets           : 12
    HTTPS Packets           : 38

    Most Active IPs:
      192.168.1.5     →  50 packets
      8.8.8.8         →  14 packets
      172.217.0.14    →   9 packets
  ============================================================


--------------------------------------------------------------
  REQUIREMENTS
--------------------------------------------------------------

  Before you begin, make sure you have the following:

    - Python 3.10 or higher
        Download: https://www.python.org/downloads/
        (Check "Add Python to PATH" during installation)

    - Scapy library
        Installed via pip (see Installation steps below)

    - Npcap (REQUIRED for Scapy to work on Windows)
        Download: https://npcap.com/#download
        Install with default settings.
        (Without Npcap, Scapy cannot capture packets on Windows)

    - Windows OS with PowerShell
        Windows 10 or Windows 11 recommended

    - Virtual environment (venv)
        Keeps your project dependencies isolated and clean


--------------------------------------------------------------
  PROJECT STRUCTURE
--------------------------------------------------------------

  network-packet-sniffer/
  |
  |-- sniffer.py          <- Main script (run this)
  |-- requirements.txt    <- Dependency list
  |-- README.txt          <- This file
  |-- venv/               <- Virtual environment (do not commit)


--------------------------------------------------------------
  INSTALLATION — STEP BY STEP
--------------------------------------------------------------

  Follow these steps carefully in order.
  Open PowerShell and navigate to your project folder first.

  ............................................................
  STEP 1 — Download or clone the project
  ............................................................

    If using Git:
      git clone https://github.com/your-username/network-packet-sniffer.git
      cd network-packet-sniffer

    Or manually download and extract the ZIP, then open
    PowerShell inside the project folder.

  ............................................................
  STEP 2 — Create a virtual environment
  ............................................................

    Run this command:

      python -m venv venv

    This creates a folder called "venv" in your project.
    It keeps Scapy and other packages contained here only.

  ............................................................
  STEP 3 — Activate the virtual environment
  ............................................................

    Run this command in PowerShell:

      .\venv\Scripts\Activate.ps1

    If successful, your terminal prompt will change to:

      (venv) PS C:\your-project-folder>

    NOTE: If you see a "cannot be loaded" error, see the
    Troubleshooting section below before continuing.

  ............................................................
  STEP 4 — Install Scapy
  ............................................................

    With the venv active, run:

      pip install scapy

    Wait for the installation to finish.
    You should see "Successfully installed scapy-..." at the end.

  ............................................................
  STEP 5 — Install Npcap (if not already installed)
  ............................................................

    Scapy needs Npcap to access your network interface on Windows.

    1. Go to: https://npcap.com/#download
    2. Download the latest Npcap installer
    3. Run the installer and keep all default settings
    4. Restart your computer if prompted


--------------------------------------------------------------
  HOW TO RUN
--------------------------------------------------------------

  IMPORTANT: You must run PowerShell as Administrator.
  Scapy requires admin-level access to capture packets.

  Step 1 — Open PowerShell as Administrator
    Right-click the PowerShell icon → "Run as administrator"

  Step 2 — Navigate to your project folder
    cd C:\path\to\network-packet-sniffer

  Step 3 — Activate the virtual environment
    .\venv\Scripts\Activate.ps1

  Step 4 — Run the sniffer
    python sniffer.py

  The program will start capturing packets immediately.
  It will auto-stop at 50 packets and print the final report.

  To stop manually before the limit, press:
    Ctrl + C


--------------------------------------------------------------
  CONFIGURATION
--------------------------------------------------------------

  You can change these settings at the top of sniffer.py:

    PACKET_LIMIT = 50
      How many packets to capture before auto-stopping.
      Change to any number you prefer.

    TARGET_PORTS = [80, 443]
      Ports to filter. 80 = HTTP, 443 = HTTPS.
      Keep these unless you want to monitor other ports.


--------------------------------------------------------------
  TROUBLESHOOTING
--------------------------------------------------------------

  ............................................................
  PROBLEM 1 — PowerShell script cannot be loaded
  ............................................................

    Error message:
      "Activate.ps1 cannot be loaded because running scripts
       is disabled on this system."

    Fix:
      Open PowerShell as Administrator and run:

        Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

      Press Y and hit Enter. Then try activating again:

        .\venv\Scripts\Activate.ps1

  ............................................................
  PROBLEM 2 — Scapy says "No match found" or cannot sniff
  ............................................................

    This usually means Npcap is not installed.

    Fix:
      1. Download Npcap from: https://npcap.com/#download
      2. Install it with default settings
      3. Restart your computer
      4. Run the sniffer again as Administrator

  ............................................................
  PROBLEM 3 — "Permission denied" or no packets captured
  ............................................................

    Scapy must be run with administrator privileges on Windows.

    Fix:
      Close your current PowerShell window.
      Right-click PowerShell → "Run as administrator"
      Navigate back to your project folder and try again.

  ............................................................
  PROBLEM 4 — "Python is not recognized" error
  ............................................................

    Python is not added to your system PATH.

    Fix:
      Reinstall Python from https://www.python.org/downloads/
      During installation, check the box:
        "Add Python to PATH"
      Then restart PowerShell and try again.

  ............................................................
  PROBLEM 5 — pip install scapy fails
  ............................................................

    Make sure your virtual environment is active first.
    Your prompt should show (venv) before the path.

    If the venv is active and pip still fails, try:

      python -m pip install --upgrade pip
      pip install scapy


--------------------------------------------------------------
  LEARNING OBJECTIVES
--------------------------------------------------------------

  After completing this project, you will understand:

    - How network packets are structured (IP and TCP layers)
    - What port numbers represent (HTTP vs HTTPS)
    - How packet sniffers like Wireshark work internally
    - How Python interacts with low-level network operations
    - Basic concepts in network monitoring and traffic analysis


--------------------------------------------------------------
  FUTURE IMPROVEMENTS (Planned)
--------------------------------------------------------------

    [ ] Export captured packets to a .csv or .pcap file
    [ ] Add DNS traffic filtering
    [ ] Build a simple GUI dashboard using Tkinter
    [ ] Add packet payload inspection for HTTP requests
    [ ] Add support for Linux and macOS


--------------------------------------------------------------
  !! LEGAL AND ETHICAL NOTICE !!
--------------------------------------------------------------

  THIS TOOL IS FOR EDUCATIONAL PURPOSES ONLY.

  - Only use this tool on YOUR OWN NETWORK or on a network
    where you have EXPLICIT WRITTEN PERMISSION.

  - Packet sniffing on networks without authorization is
    ILLEGAL in most countries and can result in criminal
    charges under computer crime and privacy laws.

  - The author is NOT responsible for any misuse of this tool.

  - This project is intended for personal lab environments,
    student learning, and academic study only.


==============================================================
  END OF README
==============================================================
