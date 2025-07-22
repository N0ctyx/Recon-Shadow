# Recon-Shadow
ReconShadow: Stealth Reconnaissance &amp; Vulnerability Discovery
# ReconShadow v4.0 🇹🇳

<div align="center">

```
██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗    ███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗
██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║    ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║
██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║    ███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║
██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║    ╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║
██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║    ███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝    ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝ 
```

**🔍 Stealth Reconnaissance & Vulnerability Discovery Tool**

*Hunting vulnerabilities in the shadows, one subdomain at a time*

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)]()
[![Version](https://img.shields.io/badge/Version-4.0-red.svg)]()

🇹🇳 **Made with ❤️ in Tunisia - Proud Tunisian Hacker** 🇹🇳

</div>

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Output](#output)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [Disclaimer](#disclaimer)
- [License](#license)
- [Author](#author)

## 🎯 About

**ReconShadow** is a comprehensive reconnaissance and vulnerability discovery tool designed specifically for bug bounty hunters and security researchers. This enhanced v4.0 edition provides advanced subdomain enumeration, DNS analysis, port scanning, URL crawling, and vulnerability detection capabilities.

### 🌟 Key Highlights

- **Multi-threaded Performance**: Fast concurrent scanning with configurable thread pools
- **Cross-platform Support**: Works seamlessly on Windows, Linux, and macOS
- **Comprehensive Reporting**: Generates detailed PDF and Excel reports
- **Live Progress Tracking**: Real-time scanning progress with colored output
- **Enhanced DNS Analysis**: DIG-like functionality with multiple record types
- **Smart URL Crawling**: Intelligent web crawling with protocol detection
- **Vulnerability Detection**: Built-in checks for common security issues

## 🚀 Features

### 🔍 Subdomain Enumeration
- **Extensive Wordlist**: 65+ carefully curated subdomain patterns
- **Multi-threaded Scanning**: Concurrent resolution for maximum speed
- **Real-time Progress**: Live progress tracking with found subdomain display
- **IP Resolution**: Automatic IP address resolution for discovered subdomains

### 🌐 DNS Analysis
- **Comprehensive Records**: A, AAAA, MX, NS, TXT, CNAME, SOA record queries
- **Reverse DNS Lookup**: PTR record resolution
- **Multi-target Support**: Scans main domain + all discovered subdomains
- **Cross-platform Tools**: Uses `dig` (preferred) or `nslookup` as fallback

### 🔌 Port Scanning
- **Smart Port Detection**: Scans common and critical ports
- **Service Identification**: Attempts to identify running services
- **Multi-target Support**: Scans all discovered subdomains
- **Timeout Handling**: Configurable timeouts for reliable results

### 🕷️ URL Crawling
- **Protocol Detection**: Automatic HTTP/HTTPS protocol testing
- **Common Path Discovery**: Tests 20+ common web paths
- **Link Extraction**: Discovers additional URLs from page content
- **Response Analysis**: HTTP status code analysis and filtering

### 🛡️ Vulnerability Scanning
- **Common Vulnerabilities**: Tests for admin panels, exposed files, misconfigurations
- **Directory Traversal**: Checks for path traversal vulnerabilities
- **Information Disclosure**: Detects exposed sensitive files and directories
- **Custom Payloads**: Extensible vulnerability detection patterns

### 📊 Comprehensive Reporting
- **PDF Reports**: Professional formatted reports with charts and summaries
- **Excel Export**: Detailed spreadsheets with all discovered data
- **Multiple Formats**: Separate files for different scan types
- **Timestamp Tracking**: All reports include scan timestamps and metadata

## 🛠️ Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Quick Install

```bash
# Clone the repository
git clone https://github.com/yourusername/reconshadow.git
cd reconshadow

# Install dependencies
pip install -r requirements.txt

# Make executable (Linux/macOS)
chmod +x reconshadow.py

# Run the tool
python reconshadow.py
```

### Manual Installation

```bash
# Install required packages individually
pip install requests pandas fpdf2 urllib3
```

## 🎮 Usage

### Basic Usage

```bash
python reconshadow.py
```

### Interactive Menu

The tool provides an interactive menu with the following options:

1. **Subdomain Enumeration** - Discover subdomains using built-in wordlist
2. **DNS Scan** - Comprehensive DNS record analysis
3. **Port Scan** - Network port discovery and service identification
4. **URL Crawl** - Web application URL discovery
5. **Vulnerability Scan** - Security vulnerability detection
6. **Full Scan** - Complete reconnaissance (all modules)
7. **Generate Report** - Create comprehensive PDF/Excel reports
8. **Exit** - Quit the application

### Command Line Arguments

```bash
# Direct domain input
python reconshadow.py --domain example.com

# Enable verbose output
python reconshadow.py --verbose

# Custom output directory
python reconshadow.py --output /path/to/output
```

## 📝 Examples

### Example 1: Basic Subdomain Enumeration

```bash
$ python reconshadow.py
Enter target domain: example.com
Choose option: 1

[*] Scanning subdomains for example.com...
[*] Testing 65 potential subdomains...

[+] Found: www.example.com (93.184.216.34)
[+] Found: mail.example.com (93.184.216.35)
[+] Found: api.example.com (93.184.216.36)

[*] Subdomain scan completed!
[+] Successfully found 3 subdomains
```

### Example 2: Full Reconnaissance

```bash
$ python reconshadow.py
Enter target domain: target.com
Choose option: 6

[*] Starting comprehensive reconnaissance...
[*] Phase 1: Subdomain Enumeration
[*] Phase 2: DNS Analysis
[*] Phase 3: Port Scanning
[*] Phase 4: URL Crawling
[*] Phase 5: Vulnerability Detection
[*] Generating comprehensive report...
```

## 📊 Output

### Console Output
- **Color-coded Results**: Green for success, red for errors, yellow for info
- **Real-time Progress**: Live scanning progress with statistics
- **Structured Display**: Organized output with clear sections

### Report Files
- `{domain}_comprehensive_report.pdf` - Main PDF report
- `{domain}_subdomains.xlsx` - Subdomain enumeration results
- `{domain}_dns_records.xlsx` - DNS analysis results
- `{domain}_ports.xlsx` - Port scanning results
- `{domain}_urls.xlsx` - URL crawling results
- `{domain}_vulnerabilities.xlsx` - Vulnerability scan results

## 📋 Requirements

### Python Packages
```
requests>=2.25.1
pandas>=1.3.0
fpdf2>=2.5.0
urllib3>=1.26.0
```

### System Requirements
- **Operating System**: Windows 10+, Linux (any modern distro), macOS 10.14+
- **Python**: 3.7 or higher
- **Memory**: 512MB RAM minimum
- **Network**: Internet connection for external DNS queries

### Optional Tools
- `dig` (Linux/macOS) - For enhanced DNS queries
- `nslookup` (Windows/fallback) - DNS resolution fallback

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Add comments for complex functions
- Test on multiple platforms
- Update documentation for new features

## ⚠️ Disclaimer

**IMPORTANT**: This tool is designed for educational purposes and authorized security testing only.

- ✅ **Authorized Use**: Only use on domains you own or have explicit permission to test
- ❌ **Unauthorized Use**: Do not use for malicious purposes or unauthorized testing
- 🔒 **Responsible Disclosure**: Report vulnerabilities responsibly to domain owners
- 📜 **Legal Compliance**: Ensure compliance with local laws and regulations

The authors are not responsible for any misuse of this tool.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**N0ctyx** 🇹🇳
- **Version**: 4.0 Enhanced Edition

---

<div align="center">

**🇹🇳 Proudly Made in Tunisia 🇹🇳**

*If you find this tool useful, please consider giving it a ⭐ star!*

</div>
