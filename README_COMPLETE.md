# 🔍 ReconShadow v4.0 - Cross-Platform Bug Bounty Reconnaissance Tool

<div align="center">

![ReconShadow Logo](https://img.shields.io/badge/ReconShadow-v4.0-green?style=for-the-badge&logo=security&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-blue?style=for-the-badge&logo=linux&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.7+-yellow?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-red?style=for-the-badge)

**🇹🇳 Made with ❤️ in Tunisia by N0ctyx 🇹🇳**

*Hunting vulnerabilities in the shadows, one subdomain at a time*

</div>

## 🚀 Features

### 🔍 **Comprehensive Reconnaissance**
- **Subdomain Enumeration**: Discover hidden subdomains using an extensive wordlist (60+ patterns)
- **DNS Analysis**: Complete DNS record analysis (A, AAAA, MX, NS, TXT, CNAME, SOA, PTR)
- **Port Scanning**: Identify open ports and running services
- **URL Crawling**: Discover web paths and endpoints
- **Vulnerability Detection**: Basic vulnerability scanning and exposure detection

### 🖥️ **Dual Interface**
- **GUI Version**: Modern, user-friendly graphical interface with dark theme
- **CLI Version**: Traditional command-line interface for automation and scripting

### 📊 **Advanced Reporting**
- Real-time results display with progress tracking
- Comprehensive text, PDF, and Excel reports
- Export capabilities for further analysis
- Professional formatted output

## 📦 Installation Guide

### 🪟 Windows Installation

#### Option 1: Automated Installer (Recommended)
```batch
# Download the repository
git clone https://github.com/n0ctyx/reconshadow.git
cd reconshadow

# Run automated installer
install.bat

# Or use complete build system
build_complete.bat
```

#### Option 2: Manual Windows Installation
```batch
# Install Python 3.7+ from https://python.org
# Open Command Prompt as Administrator

# Clone repository
git clone https://github.com/n0ctyx/reconshadow.git
cd reconshadow

# Install requirements
pip install -r requirements.txt

# Run GUI version
python reconshadow_gui.py

# Or run CLI version
python reconshadow.py
```

#### Option 3: Pre-built Executables (Windows)
```batch
# Download from releases page
# Extract ReconShadow_v4.0_Complete.zip
# Double-click Launch_GUI.bat or Launch_CLI.bat
```

### 🐧 Linux Installation

#### Option 1: Automated Script (Recommended)
```bash
# Download and run install script
curl -sSL https://raw.githubusercontent.com/n0ctyx/reconshadow/main/install_linux.sh | bash

# Or manual download
git clone https://github.com/n0ctyx/reconshadow.git
cd reconshadow
chmod +x install_linux.sh
./install_linux.sh
```

#### Option 2: Manual Linux Installation
```bash
# Update system packages
sudo apt update && sudo apt upgrade -y

# Install Python and pip (Ubuntu/Debian)
sudo apt install python3 python3-pip python3-tk git -y

# For CentOS/RHEL/Fedora
sudo yum install python3 python3-pip tkinter git -y
# or
sudo dnf install python3 python3-pip python3-tkinter git -y

# Clone repository
git clone https://github.com/n0ctyx/reconshadow.git
cd reconshadow

# Install Python requirements
pip3 install -r requirements.txt

# Make scripts executable
chmod +x reconshadow.py reconshadow_gui.py

# Run GUI version (requires X11/Wayland)
python3 reconshadow_gui.py

# Or run CLI version
python3 reconshadow.py
```

#### Option 3: Docker Installation (Linux/Windows/macOS)
```bash
# Build Docker image
docker build -t reconshadow .

# Run CLI version
docker run -it --rm reconshadow python3 reconshadow.py

# Run with volume mount for reports
docker run -it --rm -v $(pwd)/reports:/app/reports reconshadow
```

## 🎯 Usage Guide

### 🖥️ GUI Version Usage

#### Windows:
```batch
# From executable
Launch_GUI.bat

# From source
python reconshadow_gui.py
```

#### Linux:
```bash
# Ensure X11 forwarding for SSH
ssh -X user@server

# Run GUI
python3 reconshadow_gui.py

# Or with virtual display
xvfb-run -a python3 reconshadow_gui.py
```

**GUI Features:**
1. **Target Input**: Enter domain name (e.g., example.com)
2. **Scan Options**: 
   - 🚀 Full Scan (all modules)
   - 🔍 Subdomain Scan only
   - 🌐 DNS Analysis only
   - 🔌 Port Scan only
3. **Real-time Results**: View progress in multiple tabs
4. **Export Reports**: Save results in various formats

### 💻 CLI Version Usage

#### Windows:
```batch
# From executable
Launch_CLI.bat

# From source
python reconshadow.py
```

#### Linux:
```bash
# Run CLI version
python3 reconshadow.py

# Or make it executable
chmod +x reconshadow.py
./reconshadow.py
```

**CLI Menu Options:**
```
1. Subdomain Enumeration
2. DNS Record Analysis
3. Port Scanning
4. URL Crawling
5. Vulnerability Detection
6. Full Reconnaissance
7. Generate Report
8. Exit
```

## 🛠️ System Requirements

### Windows Requirements:
- **OS**: Windows 10 or later (Windows 11 recommended)
- **Python**: 3.7+ (if running from source)
- **RAM**: 4GB minimum, 8GB recommended
- **Network**: Internet connection required
- **Privileges**: Administrator recommended for full functionality

### Linux Requirements:
- **OS**: Ubuntu 18.04+, CentOS 7+, Debian 9+, or equivalent
- **Python**: 3.7+ (usually pre-installed)
- **Packages**: python3-pip, python3-tk (for GUI)
- **RAM**: 2GB minimum, 4GB recommended
- **Network**: Internet connection required
- **Privileges**: sudo access for installation, regular user for operation

### Dependencies (All Platforms):
```
requests>=2.25.1
pandas>=1.3.0
fpdf2>=2.5.0
urllib3>=1.26.0
openpyxl>=3.0.0
pyinstaller>=5.0.0 (for building executables)
```

## 📋 Detailed Feature Guide

### 🌐 Subdomain Enumeration
```bash
# Tests common patterns:
www, mail, ftp, api, dev, test, admin, blog, portal, shop, secure, mobile,
vpn, docs, beta, staging, cdn, support, dashboard, forum, status, static,
backup, jenkins, git, database, logs, uploads, billing, analytics, etc.

# Features:
- Multi-threaded scanning (20 concurrent threads)
- Real-time progress tracking
- IP resolution for found subdomains
- Duplicate detection and filtering
```

### 🔍 DNS Analysis
```bash
# Record types analyzed:
- A Records (IPv4 addresses)
- AAAA Records (IPv6 addresses)
- MX Records (Mail servers)
- NS Records (Name servers)
- TXT Records (Text records, SPF, DKIM)
- CNAME Records (Canonical names)
- SOA Records (Start of Authority)
- PTR Records (Reverse DNS)

# Advanced features:
- Zone transfer attempts
- DNS server identification
- Reverse DNS lookups
- DNS cache analysis
```

### 🔌 Port Scanning
```bash
# Common ports scanned:
21 (FTP), 22 (SSH), 23 (Telnet), 25 (SMTP), 53 (DNS), 80 (HTTP),
110 (POP3), 143 (IMAP), 443 (HTTPS), 993 (IMAPS), 995 (POP3S),
8080 (HTTP-Alt), 8443 (HTTPS-Alt), 3389 (RDP), 5432 (PostgreSQL),
3306 (MySQL), 1433 (MSSQL), 5984 (CouchDB), 6379 (Redis)

# Features:
- TCP connect scanning
- Service detection
- Banner grabbing
- Timeout optimization
- Custom port ranges
```

### ⚠️ Vulnerability Detection
```bash
# Checks for:
- Exposed admin panels (/admin, /wp-admin, /phpmyadmin)
- Configuration files (/.env, /config, /.git)
- Backup files (/backup, /old, /.bak)
- Debug endpoints (/debug, /test, /.well-known)
- Common web paths (/api, /docs, /swagger)

# HTTP status codes analyzed:
- 200 (OK) - Accessible content
- 301/302 (Redirect) - Potential redirects
- 403 (Forbidden) - Protected but existing
- 401 (Unauthorized) - Authentication required
```

## 📊 Output Formats

### Console Output:
- **Real-time colored output** with timestamps
- **Progress indicators** and statistics
- **Error handling** with detailed messages
- **Summary reports** at completion

### File Exports:
- **Text Reports**: Structured .txt files with all findings
- **PDF Reports**: Professional formatted documents
- **Excel Files**: Spreadsheet format for analysis
- **JSON Output**: Machine-readable format for automation

## 🔒 Legal & Ethical Use

⚠️ **IMPORTANT LEGAL NOTICE**:

This tool is designed for **AUTHORIZED TESTING ONLY**:
- ✅ **Educational purposes** and learning
- ✅ **Authorized penetration testing** with written permission
- ✅ **Bug bounty programs** with valid scope
- ✅ **Security research** on owned assets
- ✅ **Red team exercises** with proper authorization

**❌ DO NOT USE** for:
- Unauthorized scanning of third-party systems
- Malicious activities or attacks
- Violation of terms of service
- Any illegal activities

**Users are solely responsible** for ensuring compliance with:
- Local and international laws
- Terms of service of target systems
- Responsible disclosure practices
- Ethical hacking guidelines

## 🛡️ Security Considerations

### For Defenders:
- Monitor for reconnaissance activities
- Implement rate limiting
- Use web application firewalls
- Regular security assessments

### For Researchers:
- Always get written permission
- Respect rate limits and scope
- Follow responsible disclosure
- Document findings properly

## 🐛 Troubleshooting

### Common Windows Issues:

#### Python Not Found:
```batch
# Install Python from https://python.org
# Ensure "Add to PATH" is checked during installation
# Restart command prompt after installation
```

#### Permission Denied:
```batch
# Run Command Prompt as Administrator
# Right-click -> "Run as administrator"
```

#### Antivirus Blocking:
```batch
# Add ReconShadow folder to antivirus exclusions
# Temporarily disable real-time protection during build
```

### Common Linux Issues:

#### Missing Dependencies:
```bash
# Ubuntu/Debian
sudo apt install python3-pip python3-tk

# CentOS/RHEL
sudo yum install python3-pip tkinter

# Fedora
sudo dnf install python3-pip python3-tkinter
```

#### Permission Issues:
```bash
# Make scripts executable
chmod +x reconshadow.py reconshadow_gui.py

# Install packages for user only
pip3 install --user -r requirements.txt
```

#### GUI Not Working:
```bash
# Install X11 libraries
sudo apt install python3-tk

# For SSH, enable X11 forwarding
ssh -X username@server

# For headless servers, use virtual display
sudo apt install xvfb
xvfb-run -a python3 reconshadow_gui.py
```

## 🤝 Contributing

We welcome contributions from the community!

### How to Contribute:
1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Setup:
```bash
# Clone your fork
git clone https://github.com/yourusername/reconshadow.git
cd reconshadow

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate     # Windows

# Install development dependencies
pip install -r requirements.txt
pip install pytest black flake8

# Run tests
python test_system.py
```

### Contribution Guidelines:
- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation
- Ensure cross-platform compatibility

## 📞 Support & Community

### Getting Help:
- **GitHub Issues**: Report bugs and request features
- **Discussions**: Ask questions and share ideas
- **Wiki**: Detailed documentation and guides
- **Security**: Report vulnerabilities privately

### Community:
- **Discord**: Join our community server
- **Twitter**: Follow @n0ctyx for updates
- **Blog**: Read about latest features and techniques

## 🏆 Changelog

### v4.0 (Current) - "Shadow Hunter"
- ✅ **NEW**: Modern GUI interface with dark theme
- ✅ **NEW**: Cross-platform support (Windows/Linux)
- ✅ **ENHANCED**: Multi-threaded subdomain enumeration
- ✅ **ENHANCED**: Comprehensive DNS analysis
- ✅ **ENHANCED**: Advanced port scanning
- ✅ **ENHANCED**: Professional reporting system
- ✅ **IMPROVED**: Error handling and stability
- ✅ **ADDED**: Docker support
- ✅ **ADDED**: Automated build system
- ✅ **ADDED**: CI/CD integration

### v3.x - "Classic Edition"
- Basic CLI functionality
- Core reconnaissance features
- Simple reporting

### Roadmap v4.1:
- 🔄 **PLANNED**: Web interface
- 🔄 **PLANNED**: API integration
- 🔄 **PLANNED**: Custom wordlists
- 🔄 **PLANNED**: Advanced vulnerability scanning
- 🔄 **PLANNED**: Integration with popular tools

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### License Summary:
- ✅ Commercial use allowed
- ✅ Modification allowed
- ✅ Distribution allowed
- ✅ Private use allowed
- ❗ License and copyright notice required
- ❗ No warranty provided

## 🙏 Acknowledgments

### Special Thanks:
- **N0ctyx** - Original creator and maintainer 🇹🇳
- **Claude AI** - Enhanced version development
- **Bug Bounty Community** - Feedback and testing
- **Open Source Contributors** - Code improvements
- **Security Researchers** - Vulnerability reports
- **Tunisia** 🇹🇳 - Our proud homeland

### Inspiration:
- **Sublist3r** - Subdomain enumeration techniques
- **Amass** - DNS analysis methods
- **Nmap** - Port scanning approaches
- **Burp Suite** - Vulnerability detection patterns

## ⭐ Star History

If you find ReconShadow useful, please consider:
- ⭐ **Starring** the repository
- 🍴 **Forking** for your own modifications
- 📢 **Sharing** with the community
- 🐛 **Reporting** bugs and issues
- 💡 **Suggesting** new features

## 📊 Statistics

- **Languages**: Python, Batch, Shell
- **Platforms**: Windows, Linux, macOS (via Docker)
- **Dependencies**: 6 core packages
- **Features**: 5+ reconnaissance modules
- **Output Formats**: 4 different formats
- **Scan Types**: 60+ subdomain patterns

---

<div align="center">

**🔍 Happy Hunting! 🔍**

*"In the shadows we hunt, in the light we protect"*

**Remember: With great power comes great responsibility**

Made with ❤️ in Tunisia 🇹🇳 by N0ctyx

[⬆ Back to Top](#-reconshadow-v40---cross-platform-bug-bounty-reconnaissance-tool)

</div>
