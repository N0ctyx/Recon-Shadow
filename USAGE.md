# Usage Guide

## Basic Usage

### Starting ReconShadow

```bash
python reconshadow.py
```

### Menu Navigation

```
[ ReconShadow Enhanced Menu ]
──────────────────────────
1. Start Subdomain Enumeration
2. Perform DNS Scan
3. Perform Vulnerability Scan
4. Perform Port Scan
5. Start Enhanced URL Crawl
6. 🆕 Subdomain Takeover Scan
7. Generate Text Report
8. Generate Comprehensive Report
9. Exit
```

## Detailed Feature Guide

### 1. Subdomain Enumeration

Discovers subdomains using a comprehensive wordlist:

- **Input**: Target domain (e.g., example.com)
- **Output**: List of discovered subdomains with IP addresses
- **Threading**: 20 concurrent workers for fast scanning
- **Wordlist**: 65+ common subdomain patterns

**Example Output:**
```
[+] Found: www.example.com (192.168.1.1)
[+] Found: api.example.com (192.168.1.2)
[+] Found: dev.example.com (192.168.1.3)
```

### 2. DNS Scan

Comprehensive DNS analysis:

- **A Records**: IPv4 addresses
- **AAAA Records**: IPv6 addresses
- **MX Records**: Mail servers
- **NS Records**: Name servers
- **TXT Records**: Text records
- **CNAME Records**: Canonical names
- **SOA Records**: Start of Authority

### 3. Vulnerability Scan

Automated vulnerability detection:

- **Common paths**: /admin, /wp-admin, /phpmyadmin, etc.
- **Directory traversal**: Checks for exposed directories
- **File exposure**: Looks for sensitive files
- **Protocol testing**: Tests both HTTP and HTTPS

### 4. Port Scan

Fast port discovery:

- **Common ports**: 21, 22, 23, 25, 53, 80, 110, 143, 443, 993, 995
- **Service detection**: Identifies running services
- **Timeout handling**: Efficient scanning with timeouts

### 5. URL Crawling

Intelligent web crawling:

- **Common paths**: Tests 25+ common web paths
- **Protocol detection**: Automatically detects working protocol
- **Link extraction**: Finds additional URLs from page content
- **Progress tracking**: Real-time crawling progress

### 6. 🆕 Subdomain Takeover Scan

Advanced takeover detection:

#### Supported Services:
- **GitHub Pages**: Detects unclaimed GitHub Pages
- **Heroku**: Finds deleted Heroku applications
- **AWS S3**: Identifies non-existent S3 buckets
- **Shopify**: Detects unavailable Shopify stores

#### Detection Methods:
1. **Content Analysis**: Scans response content for takeover indicators
2. **Error Pattern Matching**: Identifies service-specific error messages
3. **Risk Assessment**: Provides High/Medium/Low risk ratings

**Example Output:**
```
[!] POTENTIAL GITHUB TAKEOVER: dev.example.com
    Service: GitHub Pages
    Risk: High Risk
```

## Advanced Usage Examples

### Complete Reconnaissance Workflow

```bash
# 1. Start ReconShadow
python reconshadow.py

# 2. Enter target domain
[?] Enter target domain: target.com

# 3. Run full reconnaissance
# Choose option 1: Subdomain Enumeration
# Choose option 2: DNS Scan
# Choose option 3: Vulnerability Scan
# Choose option 6: Subdomain Takeover Scan

# 4. Generate comprehensive report
# Choose option 8: Generate Comprehensive Report
```

### Quick Takeover Scan

```bash
# 1. Run subdomain enumeration first
# 2. Run takeover scan on discovered subdomains
# 3. Review findings for potential takeovers
```

## Output and Reports

### Text Report (Option 7)
- Single file with all findings
- Organized by scan type
- Easy to read format

### Comprehensive Report (Option 8)
- Separate files for each scan type
- Detailed findings with timestamps
- Professional formatting

### Report Files Generated:
- `{domain}_report.txt` - Main text report
- `{domain}_comprehensive_report/` - Folder with detailed reports
  - `subdomains.txt`
  - `dns_records.txt`
  - `vulnerabilities.txt`
  - `ports.txt`
  - `urls.txt`
  - `takeover_vulnerabilities.txt`

## Best Practices

### For Bug Bounty Hunting:
1. **Always run subdomain enumeration first**
2. **Follow up with takeover scan**
3. **Document all findings**
4. **Verify takeover opportunities manually**
5. **Report responsibly**

### For Penetration Testing:
1. **Get proper authorization**
2. **Use comprehensive scanning**
3. **Generate detailed reports**
4. **Follow responsible disclosure**

## Tips and Tricks

- **Run subdomain enumeration before takeover scan** for best results
- **Use comprehensive reports** for detailed documentation
- **Check multiple protocols** (HTTP/HTTPS) for complete coverage
- **Verify findings manually** before reporting
- **Keep tool updated** for latest detection signatures

## Troubleshooting

### Common Issues:
- **No subdomains found**: Try different target or check DNS resolution
- **Timeouts**: Adjust timeout values or check network connectivity
- **Permission errors**: Run with appropriate privileges
- **False positives**: Manually verify takeover opportunities

### Performance Optimization:
- **Adjust thread count** based on system capabilities
- **Use stable internet connection** for best results
- **Close unnecessary applications** during intensive scans

