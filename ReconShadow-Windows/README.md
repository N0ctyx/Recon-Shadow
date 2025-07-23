# 🔍 ReconShadow v4.0 - Enhanced Bug Bounty Reconnaissance Tool

<div align="center">

![ReconShadow Logo](https://img.shields.io/badge/ReconShadow-v4.0-green?style=for-the-badge&logo=security&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-blue?style=for-the-badge&logo=windows&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.7+-yellow?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-red?style=for-the-badge)

**🇹🇳 Made with ❤️ in Tunisia by N0ctyx 🇹🇳**

*Hunting vulnerabilities in the shadows, one subdomain at a time*

</div>

## 🚀 Features

### 🔍 **Comprehensive Reconnaissance**
- **Subdomain Enumeration**: Discover hidden subdomains using an extensive wordlist
- **DNS Analysis**: Complete DNS record analysis (A, AAAA, MX, NS, TXT, CNAME, SOA)
- **Port Scanning**: Identify open ports and running services
- **URL Crawling**: Discover web paths and endpoints
- **Vulnerability Detection**: Basic vulnerability scanning

### 🖥️ **Dual Interface**
- **GUI Version**: Modern, user-friendly graphical interface
- **CLI Version**: Traditional command-line interface for automation

### 📊 **Advanced Reporting**
- Real-time results display
- Comprehensive PDF and Excel reports
- Export capabilities for further analysis

## 📦 Quick Installation (Windows)

### Option 1: Automated Installer (Recommended)
1. Download the `git_exe` folder
2. Double-click `install.bat`
3. Wait for automatic installation
4. Launch from the distribution folder

### Option 2: Manual Installation
```bash
# Clone or download the repository
git clone https://github.com/n0ctyx/reconshadow.git
cd reconshadow/git_exe

# Install requirements
pip install -r requirements.txt

# Run setup
python setup.py
```

## 🎯 Usage

### GUI Version
1. Run `Launch_GUI.bat` or `ReconShadow_GUI.exe`
2. Enter target domain
3. Select scan type or run full scan
4. View results in real-time
5. Export reports as needed

### CLI Version
1. Run `Launch_CLI.bat` or `ReconShadow_CLI.exe`
2. Follow the interactive menu
3. Enter target domain
4. Select desired scans
5. View results in terminal

## 🛠️ System Requirements

- **OS**: Windows 10 or later
- **Python**: 3.7+ (for source code)
- **RAM**: 4GB minimum, 8GB recommended
- **Network**: Internet connection required
- **Privileges**: Administrator recommended for full functionality

## 📋 Scan Types

### 🌐 Subdomain Enumeration
- Tests 60+ common subdomain patterns
- Multi-threaded for fast scanning
- Real-time progress tracking
- IP resolution for found subdomains

### 🔍 DNS Analysis
- Complete DNS record enumeration
- Reverse DNS lookups
- DNS server identification
- Zone transfer attempts

### 🔌 Port Scanning
- Common port scanning (21, 22, 80, 443, etc.)
- Service identification
- Banner grabbing
- Timeout optimization

### ⚠️ Vulnerability Detection
- Common path enumeration
- Directory traversal checks
- Exposed file detection
- Basic security misconfigurations

## 📊 Output Formats

- **Console**: Real-time colored output
- **Text Reports**: Structured text files
- **PDF Reports**: Professional formatted reports
- **Excel Files**: Spreadsheet format for analysis

## 🔒 Legal & Ethical Use

⚠️ **IMPORTANT**: This tool is designed for:
- **Educational purposes**
- **Authorized penetration testing**
- **Bug bounty programs**
- **Security research on owned assets**

**DO NOT USE** on systems you don't own or lack explicit permission to test.

## 🤝 Contributing

We welcome contributions! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📞 Support

- **GitHub Issues**: Report bugs and request features
- **Documentation**: Check the wiki for detailed guides
- **Community**: Join our discussions

## 🏆 Changelog

### v4.0 (Current)
- ✅ Added GUI interface
- ✅ Enhanced subdomain enumeration
- ✅ Improved DNS analysis
- ✅ Better error handling
- ✅ Automated executable building
- ✅ Professional reporting

### v3.x
- Basic CLI functionality
- Core reconnaissance features

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **N0ctyx** - Original creator and maintainer
- **Claude** - Enhanced version development
- **Bug Bounty Community** - Feedback and testing
- **Tunisia** 🇹🇳 - Our proud homeland

## ⭐ Star History

If you find ReconShadow useful, please consider giving it a star! ⭐

---

<div align="center">

**🔍 Happy Hunting! 🔍**

*Remember: With great power comes great responsibility*

</div>
