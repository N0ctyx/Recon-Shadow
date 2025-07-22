#!/usr/bin/env python3
# ReconShadow v4.0 - Enhanced Edition for Bug Bounty (FIXED & ENHANCED)
# By N0ctyx - Enhanced by Claude

import socket
import requests
import subprocess
import sys
import signal
import time
import datetime
import platform
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from fpdf import FPDF
import pandas as pd
import os
import urllib.request
import re
from urllib.parse import urljoin, urlparse
import urllib3

# Disable SSL warnings for better crawling
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Detect operating system
IS_WINDOWS = platform.system().lower() == 'windows'
IS_LINUX = platform.system().lower() == 'linux'
IS_MACOS = platform.system().lower() == 'darwin'

# Color Codes
R, G, B, Y, M, C, W, D, RS = ('\033[1;31m', '\033[1;32m', '\033[1;34m', '\033[1;33m', '\033[1;35m', '\033[1;36m', '\033[1;37m', '\033[1;30m', '\033[0m')

# Maximum Subdomain List for Bug Bounty
subdomain_list = [
    'www', 'mail', 'ftp', 'webmail', 'smtp', 'api', 'dev', 'test', 'admin', 'blog', 'portal', 'shop', 'secure', 'm', 'mobile',
    'vpn', 'docs', 'beta', 'staging', 'cdn', 'news', 'support', 'help', 'account', 'accounts', 'dashboard', 'forum', 'forums', 'status',
    'static', 'images', 'img', 'assets', 'backup', 'jenkins', 'git', 'bitbucket', 'github', 'svn', 'jira', 'confluence', 'mysql',
    'sql', 'db', 'database', 'data', 'logs', 'log', 'downloads', 'download', 'files', 'docs', 'documentation', 'customers',
    'client', 'clients', 'upload', 'uploads', 'billing', 'payment', 'payments', 'feedback', 'survey', 'tracking', 'track', 'tracker',
    'issue', 'issues', 'bug', 'bugs', 'error', 'errors', 'demo', 'demos', 'preview', 'sandbox', 'old', 'legacy', 'archive', 'archives',
    'proxy', 'proxies', 'gateway', 'direct', 'monitor', 'monitoring', 'alert', 'alerts', 'analytics', 'stats', 'statistics',
    'report', 'reports', 'api-docs', 'swagger', 'openapi', 'exchange', 'autodiscover', 'adfs', 'ad', 'sso', 'id', 'identity',
    'auth', 'authentication', 'oauth', 'owa', 'outlook', 'calendar', 'cal', 'conference', 'meet', 'meeting', 'stream', 'video', 'videos'
]

found_subdomains = []
found_vulnerabilities = []
found_ports = []
crawled_urls = []
dns_records = []
use_tor = False

# Graphic Banner
def show_banner():
    print(f"""{C}
██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗    ███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗
██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║    ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║
██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║    ███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║
██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║    ╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║
██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║    ███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝    ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝ 

{R}▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█▓▓▒░ {Y}Hunting vulnerabilities in the shadows, one subdomain at a time{R} ░▒▓▓█
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
                | FOR ETHICAL USE ONLY |
{W}Version: 4.0 Enhanced | Codename: ShadowHunter | Hunter: N0ctyx {R}🇹🇳{W}
{D}------------------------------------------------------------------{RS}
{M}ReconShadow: Stealth Reconnaissance & Vulnerability Discovery{RS}
{R}🇹🇳 Made with ❤️ in Tunisia - Proud Tunisian Hacker 🇹🇳{W}
""")

# Function to handle interruptions
def signal_handler(sig, frame):
    print(f"\n{R}[!]{W} Operation interrupted.")
    sys.exit(0)

# Subdomain Enumeration
def resolve_subdomain(subdomain, domain):
    try:
        full_domain = f"{subdomain}.{domain}"
        ip = socket.gethostbyname(full_domain)
        return full_domain, ip
    except:
        return None

def find_subdomains(domain):
    global found_subdomains
    found_subdomains.clear()
    print(f"{Y}[*]{W} Scanning subdomains for {domain}...")
    print(f"{Y}[*]{W} Testing {len(subdomain_list)} potential subdomains...\n")
    
    tested_count = 0
    
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(resolve_subdomain, sub, domain) for sub in subdomain_list]
        for future in as_completed(futures):
            result = future.result()
            tested_count += 1
            
            if result:
                found_subdomains.append(result)
                print(f"{G}[+]{W} Found: {result[0]} ({result[1]})", flush=True)
            
            # Show progress every 10 tests
            if tested_count % 10 == 0:
                progress = (tested_count / len(subdomain_list)) * 100
                print(f"{C}[PROGRESS]{W} Tested: {tested_count}/{len(subdomain_list)} ({progress:.1f}%) | Found: {G}{len(found_subdomains)}{W} subdomains", flush=True)
    
    # Final summary
    print(f"\n{Y}[*]{W} Subdomain scan completed!")
    if found_subdomains:
        print(f"{G}[+]{W} Successfully found {G}{len(found_subdomains)}{W} subdomains:")
        for subdomain, ip in found_subdomains:
            print(f"{G}    • {subdomain} → {ip}{W}")
    else:
        print(f"{Y}[-]{W} No subdomains found")

# DNS Scan with DIG functionality - Enhanced to scan all subdomains
def dns_scan(domain):
    global dns_records
    dns_records.clear()
    
    # Create list of targets (main domain + found subdomains)
    targets = [domain]
    if found_subdomains:
        targets.extend([sub[0] for sub in found_subdomains])
        print(f"{Y}[*]{W} Performing comprehensive DNS scan on {len(targets)} targets (main domain + {len(found_subdomains)} subdomains)...\n")
    else:
        print(f"{Y}[*]{W} Performing comprehensive DNS scan for {domain}...\n")
        print(f"{Y}[*]{W} Note: Run subdomain enumeration first to scan all discovered subdomains\n")
    
    # Wait for user confirmation
    print(f"{C}[READY]{W} Press {G}Enter{W} to start DNS scanning...")
    input()
    
    for target in targets:
        print(f"{C}[TARGET]{W} DNS scanning: {C}{target}{W}")
        print(f"{C}{'-'*50}{W}")
        
        # Basic DNS resolution
        try:
            # Get A record
            ip = socket.gethostbyname(target)
            print(f"{G}[+]{W} A Record: {target} -> {ip}")
            dns_records.append(("A", target, ip))
            
            # Get hostname
            try:
                hostname = socket.gethostbyaddr(ip)
                print(f"{G}[+]{W} Reverse DNS: {ip} -> {hostname[0]}")
                dns_records.append(("PTR", ip, hostname[0]))
            except:
                print(f"{Y}[-]{W} No reverse DNS found for {ip}")
                
        except socket.error as e:
            print(f"{R}[!]{W} DNS resolution error for {target}: {str(e)}")
            continue
    
        # DIG-like functionality using nslookup/dig commands
        print(f"\n{Y}[*]{W} Performing DIG-like DNS queries for {target}...\n")
        
        # DNS record types to query
        record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME', 'SOA']
        
        for record_type in record_types:
            try:
                print(f"{Y}[*]{W} Querying {record_type} records for {target}...")
                
                # Try using dig first (preferred on Linux), then nslookup as fallback
                dns_success = False
                
                # Try dig first (Linux/Unix preferred)
                try:
                    result = subprocess.run(['dig', '+short', record_type, target], 
                                          capture_output=True, text=True, timeout=10)
                    if result.returncode == 0 and result.stdout.strip():
                        records = result.stdout.strip().split('\n')
                        print(f"{G}[+]{W} {record_type} Records found:")
                        for record in records[:5]:  # Limit output
                            if record.strip():
                                print(f"{G}    {record.strip()}{W}")
                                dns_records.append((record_type, target, record.strip()))
                        dns_success = True
                    else:
                        print(f"{Y}[-]{W} No {record_type} records found")
                        dns_success = True
                        
                except subprocess.TimeoutExpired:
                    print(f"{R}[!]{W} Timeout querying {record_type} records with dig")
                except FileNotFoundError:
                    # dig not available, try nslookup
                    pass
            
                # If dig failed or not available, try nslookup
                if not dns_success:
                    try:
                        # Different nslookup syntax for different systems
                        nslookup_cmd = ['nslookup', '-type=' + record_type, target]
                        if record_type == 'A':
                            nslookup_cmd = ['nslookup', target]
                        
                        result = subprocess.run(nslookup_cmd, 
                                              capture_output=True, text=True, timeout=10)
                        if result.returncode == 0 and result.stdout:
                            output_lines = result.stdout.strip().split('\n')
                            relevant_lines = []
                            
                            for line in output_lines:
                                line = line.strip()
                                if line and not line.startswith('Server:') and not line.startswith('Address:') and not line.startswith('Non-authoritative'):
                                    if record_type.lower() in line.lower() or '=' in line or '->' in line or 'answer:' in line.lower():
                                        relevant_lines.append(line)
                            
                            if relevant_lines:
                                print(f"{G}[+]{W} {record_type} Records found:")
                                for line in relevant_lines[:5]:  # Limit output
                                    print(f"{G}    {line}{W}")
                            else:
                                print(f"{Y}[-]{W} No {record_type} records found")
                        else:
                            print(f"{Y}[-]{W} No {record_type} records found")
                            
                    except subprocess.TimeoutExpired:
                        print(f"{R}[!]{W} Timeout querying {record_type} records")
                    except FileNotFoundError:
                        print(f"{Y}[-]{W} DNS tools not available for {record_type} query")
                    except Exception as e:
                        print(f"{R}[!]{W} Error querying {record_type} records for {target}: {str(e)}")
                        
            except Exception as e:
                print(f"{R}[!]{W} Error querying {record_type} records for {target}: {str(e)}")
        
        print(f"{C}{'-'*50}{W}\n")

# Enhanced URL Crawl Function with LIVE DISPLAY - Enhanced to crawl all subdomains
def url_crawl(domain, max_urls=50):
    """
    Enhanced URL crawler with LIVE terminal output - Crawls all discovered subdomains
    """
    global crawled_urls
    crawled_urls.clear()
    
    # Create list of targets (main domain + found subdomains)
    targets = [domain]
    if found_subdomains:
        targets.extend([sub[0] for sub in found_subdomains])
        print(f"{Y}[*]{W} Starting enhanced URL crawling on {len(targets)} targets (main domain + {len(found_subdomains)} subdomains)")
    else:
        print(f"{Y}[*]{W} Starting enhanced URL crawling for {C}{domain}{W}")
        print(f"{Y}[*]{W} Note: Run subdomain enumeration first to crawl all discovered subdomains")
    
    print(f"{Y}[*]{W} Starting crawl process...\n")
    
    protocols = ["https", "http"]
    common_paths = [
        "/", "/about", "/contact", "/services", "/products", "/blog", "/news", 
        "/login", "/register", "/admin", "/dashboard", "/account", "/profile",
        "/help", "/support", "/faq", "/search", "/sitemap.xml", "/robots.txt",
        "/api", "/docs", "/documentation", "/terms", "/privacy", "/careers",
        "/upload", "/download", "/files", "/images", "/assets", "/static"
    ]
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; ReconShadow/4.0; +https://github.com/n0ctyx)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive'
    }
    
    total_urls_found = 0
    
    # Crawl each target (main domain + subdomains)
    for target_index, target in enumerate(targets, 1):
        print(f"{C}[TARGET {target_index}/{len(targets)}]{W} Crawling: {C}{target}{W}")
        print(f"{C}{'='*60}{W}")
        
        working_protocol = None
        
        # Test protocols first for this target
        print(f"{Y}[*]{W} Testing protocols for {target}...")
        for protocol in protocols:
            print(f"{Y}[*]{W} Testing {protocol.upper()} protocol on {target}...")
            try:
                test_url = f"{protocol}://{target}"
                response = requests.get(test_url, timeout=10, headers=headers, verify=False, allow_redirects=True)
                if response.status_code == 200:
                    working_protocol = protocol
                    print(f"{G}[+]{W} {protocol.upper()} protocol is working! Starting crawl...")
                    break
                else:
                    print(f"{Y}[-]{W} {protocol.upper()} returned status {response.status_code}")
            except Exception as e:
                print(f"{R}[-]{W} {protocol.upper()} failed: {str(e)[:50]}...")
                continue
        
        if not working_protocol:
            print(f"{R}[!]{W} Could not establish connection with {target}")
            print(f"{R}[!]{W} Skipping this target...")
            print(f"{C}{'='*60}{W}\n")
            continue
        
        print(f"\n{G}[+]{W} Using {working_protocol.upper()} protocol for crawling {target}")
        print(f"{Y}[*]{W} Testing common paths and discovering URLs...\n")
        
        tested_count = 0
        found_count = 0
        target_urls = []
        
        # Test common paths with live output
        for path in common_paths:
            if len(target_urls) >= max_urls:
                print(f"{Y}[*]{W} Reached maximum URL limit ({max_urls}) for {target}")
                break
                
            full_url = f"{working_protocol}://{target}{path}"
            tested_count += 1
            
            try:
                # Print immediately without waiting
                print(f"{C}[{tested_count:2d}]{W} Testing: {Y}{path:<20}{W}", end="", flush=True)
                
                response = requests.get(full_url, timeout=5, headers=headers, 
                                      verify=False, allow_redirects=True)
                
                status_code = response.status_code
                
                if status_code == 200:
                    crawled_urls.append(full_url)
                    target_urls.append(full_url)
                    found_count += 1
                    print(f" {G}[200 OK] ✓ FOUND!{W}")
                    print(f"{G}    → URL: {full_url}{W}")
                    
                    # Try to extract more links from successful pages
                    try:
                        content = response.text
                        new_links = extract_links_from_content(content, f"{working_protocol}://{target}", target)
                        
                        links_added = 0
                        for link in new_links[:5]:  # Limit per page
                            if len(target_urls) >= max_urls:
                                break
                            if link not in crawled_urls:
                                crawled_urls.append(link)
                                target_urls.append(link)
                                links_added += 1
                                print(f"{G}    → DISCOVERED: {link}{W}")
                        
                        if links_added > 0:
                            found_count += links_added
                            print(f"{G}    → Extracted {links_added} additional links{W}")
                            
                    except Exception as e:
                        print(f"{Y}    → Link extraction failed: {str(e)[:30]}...{W}")
                        
                elif status_code in [301, 302]:
                    redirect_location = response.headers.get('Location', 'Unknown')
                    print(f" {Y}[{status_code}] → REDIRECT{W}")
                    print(f"{Y}    → Redirects to: {redirect_location}{W}")
                    
                    # Add redirect target if it's on same domain
                    if redirect_location and target in redirect_location and redirect_location not in crawled_urls:
                        crawled_urls.append(redirect_location)
                        target_urls.append(redirect_location)
                        found_count += 1
                        print(f"{G}    → ADDED REDIRECT: {redirect_location}{W}")
                        
                elif status_code == 403:
                    print(f" {Y}[403] ⚠ FORBIDDEN{W}")
                    print(f"{Y}    → Path exists but access denied{W}")
                    
                elif status_code == 404:
                    print(f" {D}[404] ✗ NOT FOUND{W}")
                    
                else:
                    print(f" {R}[{status_code}] ? UNKNOWN{W}")
                
                # Show progress every 3 URLs
                if tested_count % 3 == 0:
                    progress = (tested_count / len(common_paths)) * 100
                    print(f"{C}[PROGRESS]{W} {tested_count}/{len(common_paths)} paths ({progress:.1f}%) | Found: {G}{found_count}{W} URLs")
                    
            except requests.exceptions.Timeout:
                print(f" {R}[TIMEOUT] ✗ SLOW{W}")
                
            except requests.exceptions.ConnectionError:
                print(f" {R}[CONN_ERR] ✗ NO CONNECTION{W}")
                
            except Exception as e:
                print(f" {R}[ERROR] ✗ FAILED{W}")
            
            # Force output flush after each test
            sys.stdout.flush()
        
        # Target summary
        total_urls_found += len(target_urls)
        print(f"\n{C}[TARGET SUMMARY]{W} {target}: Found {G}{len(target_urls)}{W} URLs")
        print(f"{C}{'='*60}{W}\n")
    
    # Final comprehensive summary
    print(f"{C}{'='*70}{W}")
    print(f"{Y}[*]{W} URL crawling completed for all targets!")
    
    if not crawled_urls:
        print(f"{R}[!]{W} No URLs could be crawled from any target")
        print(f"{R}[!]{W} Possible reasons:")
        print(f"{R}    - Websites block automated requests{W}")
        print(f"{R}    - All paths return 404{W}")
        print(f"{R}    - Network connectivity issues{W}")
    else:
        print(f"{G}[+]{W} Successfully discovered {G}{len(crawled_urls)}{W} URLs across {len(targets)} targets!")
        print(f"{G}[+]{W} Complete URL list:")
        
        for i, url in enumerate(crawled_urls, 1):
            print(f"{G}    {i:2d}.{W} {url}")
            
        print(f"\n{G}[+]{W} Crawling statistics:")
        print(f"{G}    • Total targets scanned: {len(targets)}{W}")
        print(f"{G}    • Total URLs discovered: {len(crawled_urls)}{W}")
        print(f"{G}    • Average URLs per target: {len(crawled_urls)/len(targets):.1f}{W}")
    
    return crawled_urls

def extract_links_from_content(html_content, base_url, target_domain):
    """
    Enhanced link extraction from HTML content
    """
    links = set()
    
    try:
        # Multiple regex patterns for different link types
        patterns = [
            r'href=[\'"]([^\'"]*)[\'"]',  # href links
            r'src=[\'"]([^\'"]*)[\'"]',   # src links
            r'action=[\'"]([^\'"]*)[\'"]', # form actions
        ]
        
        for pattern in patterns:
            try:
                matches = re.findall(pattern, html_content, re.IGNORECASE)
                for match in matches:
                    if match and len(match) > 1:
                        # Skip empty, javascript, mailto, tel links
                        if match.startswith(('javascript:', 'mailto:', 'tel:', '#', 'data:')):
                            continue
                            
                        # Convert relative URLs to absolute
                        try:
                            if match.startswith('/') and not match.startswith('//'):
                                full_url = f"{base_url.rstrip('/')}{match}"
                            elif match.startswith('http'):
                                full_url = match
                            elif match.startswith('//'):
                                # Protocol-relative URL
                                protocol = base_url.split('://')[0]
                                full_url = f"{protocol}:{match}"
                            else:
                                full_url = urljoin(base_url, match)
                            
                            # Parse URL to check domain
                            parsed_url = urlparse(full_url)
                            
                            # Only include URLs from target domain
                            if target_domain in parsed_url.netloc:
                                links.add(full_url)
                                
                        except Exception:
                            continue
                            
            except Exception:
                continue
                
    except Exception:
        pass
    
    return list(links)

# Simple vulnerability scan for testing
def vulnerability_scan(domain):
    global found_vulnerabilities
    found_vulnerabilities.clear()
    
    print(f"{Y}[*]{W} Performing vulnerability scan on {domain}...\n")
    
    # Wait for user confirmation
    print(f"{C}[READY]{W} Press {G}Enter{W} to start vulnerability scanning...")
    input()
    
    paths = ["/admin", "/wp-admin", "/phpmyadmin", "/manager", "/login", "/.git", "/backup", "/config"]
    protocols = ["https", "http"]
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    for protocol in protocols:
        print(f"{Y}[*]{W} Trying {protocol.upper()} protocol...")
        for path in paths:
            full_url = f"{protocol}://{domain}{path}"
            try:
                print(f"{Y}[*]{W} Testing: {path}", end=" ... ")
                response = requests.get(full_url, timeout=5, allow_redirects=False, 
                                      headers=headers, verify=False)
                
                if response.status_code == 200:
                    found_vulnerabilities.append((full_url, response.status_code, "Accessible", "High"))
                    print(f"{R}[200 - HIGH RISK]{W}")
                    print(f"{R}[!]{W} {R}CRITICAL:{W} {full_url} - {R}Accessible{W}")
                    
                elif response.status_code == 403:
                    found_vulnerabilities.append((full_url, response.status_code, "Forbidden", "Medium"))
                    print(f"{Y}[403 - FORBIDDEN]{W}")
                    print(f"{Y}[+]{W} {Y}EXISTS:{W} {full_url} - {Y}Forbidden{W}")
                    
                elif response.status_code in [301, 302]:
                    found_vulnerabilities.append((full_url, response.status_code, "Redirect", "Low"))
                    print(f"{C}[{response.status_code} - REDIRECT]{W}")
                    
                elif response.status_code == 404:
                    print(f"{D}[404 - NOT FOUND]{W}")
                    
                else:
                    print(f"{G}[{response.status_code}]{W}")
                    
            except requests.exceptions.RequestException:
                print(f"{R}[ERROR]{W}")
                continue
    
    # Summary
    print(f"\n{Y}[*]{W} Vulnerability scan completed!")
    
    if not found_vulnerabilities:
        print(f"{G}[+]{W} No obvious vulnerabilities found - Good security posture!")
    else:
        print(f"{R}[!]{W} Found {len(found_vulnerabilities)} potential security issues:")
        
        # Categorize by risk level
        high_risk = [v for v in found_vulnerabilities if len(v) > 3 and v[3] == "High"]
        medium_risk = [v for v in found_vulnerabilities if len(v) > 3 and v[3] == "Medium"]
        low_risk = [v for v in found_vulnerabilities if len(v) > 3 and v[3] == "Low"]
        
        if high_risk:
            print(f"{R}[!]{W} HIGH RISK: {len(high_risk)} issues")
        if medium_risk:
            print(f"{Y}[!]{W} MEDIUM RISK: {len(medium_risk)} issues")
        if low_risk:
            print(f"{G}[!]{W} LOW RISK: {len(low_risk)} issues")
    
    return found_vulnerabilities

# Enhanced port scan - scans all subdomains
def port_scan(domain):
    global found_ports
    found_ports.clear()
    
    # Create list of targets (main domain + found subdomains)
    targets = [domain]
    if found_subdomains:
        targets.extend([sub[0] for sub in found_subdomains])
        print(f"{Y}[*]{W} Performing port scan on {len(targets)} targets (main domain + {len(found_subdomains)} subdomains)...\n")
    else:
        print(f"{Y}[*]{W} Performing port scan on {domain}...\n")
        print(f"{Y}[*]{W} Note: Run subdomain enumeration first to scan all discovered subdomains\n")
    
    # Wait for user confirmation
    print(f"{C}[READY]{W} Press {G}Enter{W} to start port scanning...")
    input()
    
    common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 993, 995, 8080, 8443, 3389, 5432, 3306]
    
    total_open_ports = 0
    
    for target_index, target in enumerate(targets, 1):
        print(f"{C}[TARGET {target_index}/{len(targets)}]{W} Port scanning: {C}{target}{W}")
        print(f"{C}{'-'*50}{W}")
        
        try:
            target_ip = socket.gethostbyname(target)
            print(f"{Y}[*]{W} Resolved {target} to {target_ip}")
        except socket.error as e:
            print(f"{R}[!]{W} Failed to resolve {target}: {str(e)}")
            print(f"{C}{'-'*50}{W}\n")
            continue
        
        target_open_ports = []
        
        for port in common_ports:
            try:
                print(f"{Y}[*]{W} Testing {target}:{port}...", end=" ", flush=True)
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(3)
                result = sock.connect_ex((target_ip, port))
                sock.close()
                
                if result == 0:
                    found_ports.append((target, port))
                    target_open_ports.append(port)
                    print(f"{G}[OPEN] ✓{W}")
                else:
                    print(f"{D}[CLOSED]{W}")
                    
            except Exception as e:
                print(f"{R}[ERROR] - {str(e)[:30]}...{W}")
        
        if target_open_ports:
            print(f"{G}[+]{W} {target}: Open ports found: {', '.join(map(str, target_open_ports))}")
            total_open_ports += len(target_open_ports)
        else:
            print(f"{Y}[-]{W} {target}: No open ports found")
        
        print(f"{C}{'-'*50}{W}\n")
    
    print(f"{C}{'='*60}{W}")
    print(f"{Y}[*]{W} Port scan completed for all targets!")
    
    if found_ports:
        print(f"{G}[+]{W} Total open ports found: {total_open_ports} across {len(targets)} targets")
        print(f"{G}[+]{W} Detailed results:")
        for target, port in found_ports:
            print(f"{G}    • {target}:{port} - OPEN{W}")
    else:
        print(f"{Y}[-]{W} No open ports found on any target")
    
    return found_ports

# Simple report generation
def generate_text_report(domain):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    folder = Path(f"n0ctyx_reports_{domain}_{timestamp}")
    folder.mkdir(parents=True, exist_ok=True)
    report_path = folder / "n0ctyx_report.txt"
    
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(f"ReconShadow Report\n")
        f.write(f"Target: {domain}\n")
        f.write(f"Date: {timestamp}\n")
        f.write("=" * 50 + "\n\n")
        
        f.write(f"DNS Records Found: {len(dns_records)}\n")
        for record_type, query, result in dns_records:
            f.write(f"  {record_type}: {query} -> {result}\n")
        
        f.write(f"\nSubdomains Found: {len(found_subdomains)}\n")
        for sub, ip in found_subdomains:
            f.write(f"  {sub} -> {ip}\n")
        
        f.write(f"\nVulnerabilities Found: {len(found_vulnerabilities)}\n")
        for vuln in found_vulnerabilities:
            f.write(f"  {vuln[0]} - Status: {vuln[1]}\n")
        
        f.write(f"\nOpen Ports: {len(found_ports)}\n")
        for port_info in found_ports:
            if isinstance(port_info, tuple):
                f.write(f"  {port_info[0]}:{port_info[1]} - OPEN\n")
            else:
                f.write(f"  Port {port_info}\n")
        
        f.write(f"\nCrawled URLs: {len(crawled_urls)}\n")
        for url in crawled_urls:
            f.write(f"  {url}\n")
    
    print(f"\n{G}[+]{W} Text report generated: {Y}{report_path}{W}")
    return report_path

# Comprehensive Report Generation (All scans in separate files)
def generate_comprehensive_report(domain):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    folder = Path(f"n0ctyx_comprehensive_{domain}_{timestamp}")
    folder.mkdir(parents=True, exist_ok=True)
    
    print(f"\n{Y}[*]{W} Generating comprehensive report in: {Y}{folder}{W}")
    
    # Create individual scan files
    files_created = []
    
    # 1. DNS Records Report
    if dns_records:
        dns_file = folder / "01_dns_records.txt"
        with open(dns_file, "w", encoding="utf-8") as f:
            f.write(f"ReconShadow - DNS Records Report\n")
            f.write(f"Target: {domain}\n")
            f.write(f"Date: {timestamp}\n")
            f.write(f"Total DNS Records Found: {len(dns_records)}\n")
            f.write("=" * 60 + "\n\n")
            
            # Group by record type
            record_types = {}
            for record_type, query, result in dns_records:
                if record_type not in record_types:
                    record_types[record_type] = []
                record_types[record_type].append((query, result))
            
            for record_type, records in record_types.items():
                f.write(f"{record_type} Records:\n")
                f.write("-" * 20 + "\n")
                for query, result in records:
                    f.write(f"  {query} -> {result}\n")
                f.write("\n")
        
        files_created.append(("DNS Records", dns_file))
        print(f"{G}[+]{W} DNS records report: {dns_file.name}")
    
    # 2. Subdomains Report
    if found_subdomains:
        subdomain_file = folder / "02_subdomains.txt"
        with open(subdomain_file, "w", encoding="utf-8") as f:
            f.write(f"ReconShadow - Subdomain Enumeration Report\n")
            f.write(f"Target: {domain}\n")
            f.write(f"Date: {timestamp}\n")
            f.write(f"Total Subdomains Found: {len(found_subdomains)}\n")
            f.write("=" * 60 + "\n\n")
            
            for sub, ip in found_subdomains:
                f.write(f"{sub:<40} -> {ip}\n")
        
        files_created.append(("Subdomains", subdomain_file))
        print(f"{G}[+]{W} Subdomains report: {subdomain_file.name}")
    
    # 3. Vulnerabilities Report
    if found_vulnerabilities:
        vuln_file = folder / "03_vulnerabilities.txt"
        with open(vuln_file, "w", encoding="utf-8") as f:
            f.write(f"ReconShadow - Vulnerability Scan Report\n")
            f.write(f"Target: {domain}\n")
            f.write(f"Date: {timestamp}\n")
            f.write(f"Total Issues Found: {len(found_vulnerabilities)}\n")
            f.write("=" * 60 + "\n\n")
            
            # Group by risk level
            high_risk = [v for v in found_vulnerabilities if len(v) > 3 and v[3] == "High"]
            medium_risk = [v for v in found_vulnerabilities if len(v) > 3 and v[3] == "Medium"]
            low_risk = [v for v in found_vulnerabilities if len(v) > 3 and v[3] == "Low"]
            
            if high_risk:
                f.write("🚨 HIGH RISK VULNERABILITIES:\n")
                f.write("-" * 30 + "\n")
                for vuln in high_risk:
                    f.write(f"[!] {vuln[0]}\n")
                    f.write(f"    Status: {vuln[1]} | Description: {vuln[2]} | Risk: {vuln[3]}\n\n")
                f.write("\n")
            
            if medium_risk:
                f.write("⚠️  MEDIUM RISK VULNERABILITIES:\n")
                f.write("-" * 30 + "\n")
                for vuln in medium_risk:
                    f.write(f"[+] {vuln[0]}\n")
                    f.write(f"    Status: {vuln[1]} | Description: {vuln[2]} | Risk: {vuln[3]}\n\n")
                f.write("\n")
            
            if low_risk:
                f.write("ℹ️  LOW RISK VULNERABILITIES:\n")
                f.write("-" * 30 + "\n")
                for vuln in low_risk:
                    f.write(f"[-] {vuln[0]}\n")
                    f.write(f"    Status: {vuln[1]} | Description: {vuln[2]} | Risk: {vuln[3]}\n\n")
        
        files_created.append(("Vulnerabilities", vuln_file))
        print(f"{G}[+]{W} Vulnerabilities report: {vuln_file.name}")
    
    # 4. Ports Report
    if found_ports:
        ports_file = folder / "04_open_ports.txt"
        with open(ports_file, "w", encoding="utf-8") as f:
            f.write(f"ReconShadow - Port Scan Report\n")
            f.write(f"Target: {domain}\n")
            f.write(f"Date: {timestamp}\n")
            f.write(f"Total Open Ports: {len(found_ports)}\n")
            f.write("=" * 60 + "\n\n")
            
            for port_info in sorted(found_ports):
                if isinstance(port_info, tuple):
                    f.write(f"{port_info[0]}:{port_info[1]}/tcp - OPEN\n")
                else:
                    f.write(f"Port {port_info}/tcp - OPEN\n")
        
        files_created.append(("Open Ports", ports_file))
        print(f"{G}[+]{W} Ports report: {ports_file.name}")
    
    # 5. URLs Report
    if crawled_urls:
        urls_file = folder / "05_crawled_urls.txt"
        with open(urls_file, "w", encoding="utf-8") as f:
            f.write(f"ReconShadow - URL Crawling Report\n")
            f.write(f"Target: {domain}\n")
            f.write(f"Date: {timestamp}\n")
            f.write(f"Total URLs Found: {len(crawled_urls)}\n")
            f.write("=" * 60 + "\n\n")
            
            for url in sorted(crawled_urls):
                f.write(f"{url}\n")
        
        files_created.append(("Crawled URLs", urls_file))
        print(f"{G}[+]{W} URLs report: {urls_file.name}")
    
    # 6. Summary Report
    summary_file = folder / "00_summary.txt"
    with open(summary_file, "w", encoding="utf-8") as f:
        f.write(f"ReconShadow - Comprehensive Scan Summary\n")
        f.write(f"Target: {domain}\n")
        f.write(f"Date: {timestamp}\n")
        f.write(f"Hunter: N0ctyx\n")
        f.write("=" * 60 + "\n\n")
        
        f.write("SCAN RESULTS SUMMARY:\n")
        f.write("-" * 30 + "\n")
        f.write(f"DNS Records Found: {len(dns_records)}\n")
        f.write(f"Subdomains Found: {len(found_subdomains)}\n")
        f.write(f"Vulnerabilities Found: {len(found_vulnerabilities)}\n")
        f.write(f"Open Ports Found: {len(found_ports)}\n")
        f.write(f"URLs Crawled: {len(crawled_urls)}\n\n")
        
        if found_vulnerabilities:
            high_risk = [v for v in found_vulnerabilities if len(v) > 3 and v[3] == "High"]
            medium_risk = [v for v in found_vulnerabilities if len(v) > 3 and v[3] == "Medium"]
            low_risk = [v for v in found_vulnerabilities if len(v) > 3 and v[3] == "Low"]
            
            f.write("VULNERABILITY BREAKDOWN:\n")
            f.write("-" * 30 + "\n")
            f.write(f"🚨 High Risk: {len(high_risk)}\n")
            f.write(f"⚠️  Medium Risk: {len(medium_risk)}\n")
            f.write(f"ℹ️  Low Risk: {len(low_risk)}\n\n")
        
        f.write("FILES GENERATED:\n")
        f.write("-" * 30 + "\n")
        for scan_type, file_path in files_created:
            f.write(f"{scan_type}: {file_path.name}\n")
    
    files_created.insert(0, ("Summary", summary_file))
    print(f"{G}[+]{W} Summary report: {summary_file.name}")
    
    print(f"\n{G}[+]{W} Comprehensive report completed!")
    print(f"{G}[+]{W} Report folder: {Y}{folder}{W}")
    print(f"{G}[+]{W} Total files created: {len(files_created)}")
    
    return folder

# Main Menu
def main_menu():
    print(f"\n{Y}[ ReconShadow Menu ]{W}")
    print(f"{D}──────────────────────────{RS}")
    print(f"{G}1.{W} Start Subdomain Enumeration")
    print(f"{G}2.{W} Perform DNS Scan")
    print(f"{G}3.{W} Perform Vulnerability Scan")
    print(f"{G}4.{W} Perform Port Scan")
    print(f"{G}5.{W} Start Enhanced URL Crawl")
    print(f"{G}6.{W} Generate Text Report")
    print(f"{G}7.{W} Generate Comprehensive Report (Separate Files)")
    print(f"{G}8.{W} Exit")
    print(f"{D}──────────────────────────{RS}")

# Main Function
def main():
    show_banner()
    
    domain = input(f"\n{B}[?]{W} Enter target domain (e.g., example.com): ").strip()
    if not domain:
        print(f"{R}[!]{W} Please enter a valid domain")
        return

    # Start Subdomain Enumeration
    find_subdomains(domain)
    
    while True:
        main_menu()
        choice = input(f"\n{B}[?]{W} Select option (1-8): ").strip()
        


        if choice == '1':
            find_subdomains(domain)

        elif choice == '2':
            dns_scan(domain)

        elif choice == '3':
            vulnerability_scan(domain)

        elif choice == '4':
            port_scan(domain)

        elif choice == '5':
            url_crawl(domain, 50)

        elif choice == '6':
            generate_text_report(domain)

        elif choice == '7':
            print(f"\n{Y}[*]{W} Generating comprehensive report with separate files...")
            generate_comprehensive_report(domain)

        elif choice == '8':
            print(f"\n{G}[+]{W} Exiting ReconShadow...")
            break

        else:
            print(f"{R}[!]{W} Invalid option. Choose between 1-8")

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}[!]{W} Operation interrupted.")
        sys.exit(0)
