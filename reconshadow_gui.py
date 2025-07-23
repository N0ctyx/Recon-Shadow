#!/usr/bin/env python3
"""
ReconShadow v4.0 - GUI Edition for Bug Bounty
Enhanced GUI version with modern interface
By N0ctyx - Enhanced by Claude
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import threading
import socket
import requests
import subprocess
import sys
import time
import datetime
import platform
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import os
import re
from urllib.parse import urljoin, urlparse
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Subdomain list
subdomain_list = [
    'www', 'mail', 'ftp', 'webmail', 'smtp', 'api', 'dev', 'test', 'admin', 'blog', 'portal', 'shop', 'secure', 'm', 'mobile',
    'vpn', 'docs', 'beta', 'staging', 'cdn', 'news', 'support', 'help', 'account', 'accounts', 'dashboard', 'forum', 'forums', 'status'
]

class ReconShadowGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ReconShadow v4.0 - GUI Edition")
        self.root.geometry("1200x800")
        self.root.configure(bg='#2b2b2b')
        
        self.found_subdomains = []
        self.found_vulnerabilities = []
        self.found_ports = []
        self.dns_records = []
        self.scan_running = False
        
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title_frame = tk.Frame(self.root, bg='#2b2b2b')
        title_frame.pack(fill='x', padx=10, pady=5)
        
        title_label = tk.Label(title_frame, 
                              text="🔍 ReconShadow v4.0 - GUI Edition 🔍", 
                              font=('Arial', 16, 'bold'),
                              bg='#2b2b2b', fg='#00ff00')
        title_label.pack()
        
        # Input
        input_frame = tk.Frame(self.root, bg='#2b2b2b')
        input_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(input_frame, text="Target Domain:", 
                font=('Arial', 12, 'bold'), bg='#2b2b2b', fg='#ffffff').pack(side='left')
        
        self.domain_entry = tk.Entry(input_frame, font=('Arial', 12), 
                                    bg='#404040', fg='#ffffff', width=30)
        self.domain_entry.pack(side='left', padx=10)
        
        # Buttons
        control_frame = tk.Frame(self.root, bg='#2b2b2b')
        control_frame.pack(fill='x', padx=10, pady=5)
        
        self.start_button = tk.Button(control_frame, text="🚀 Start Scan", 
                                     command=self.start_scan,
                                     bg='#00aa00', fg='#ffffff', font=('Arial', 10, 'bold'))
        self.start_button.pack(side='left', padx=5)
        
        self.stop_button = tk.Button(control_frame, text="⏹️ Stop", 
                                    command=self.stop_scan,
                                    bg='#cc0000', fg='#ffffff', font=('Arial', 10, 'bold'))
        self.stop_button.pack(side='left', padx=5)
        
        # Progress
        self.progress_var = tk.StringVar()
        self.progress_var.set("Ready to scan...")
        
        progress_frame = tk.Frame(self.root, bg='#2b2b2b')
        progress_frame.pack(fill='x', padx=10, pady=5)
        
        self.progress_label = tk.Label(progress_frame, textvariable=self.progress_var,
                                      font=('Arial', 10), bg='#2b2b2b', fg='#00ff00')
        self.progress_label.pack(side='left', padx=10)
        
        # Results
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Console tab
        self.console_frame = tk.Frame(self.notebook, bg='#1a1a1a')
        self.notebook.add(self.console_frame, text="Console")
        
        self.console_text = scrolledtext.ScrolledText(self.console_frame, 
                                                     bg='#1a1a1a', fg='#00ff00',
                                                     font=('Consolas', 10))
        self.console_text.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Results tab
        self.results_frame = tk.Frame(self.notebook, bg='#1a1a1a')
        self.notebook.add(self.results_frame, text="Results")
        
        self.results_text = scrolledtext.ScrolledText(self.results_frame,
                                                     bg='#1a1a1a', fg='#ffffff',
                                                     font=('Consolas', 10))
        self.results_text.pack(fill='both', expand=True, padx=5, pady=5)
        
        self.log_to_console("ReconShadow v4.0 GUI Edition Ready")
        
    def log_to_console(self, message):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        formatted_message = f"[{timestamp}] {message}\n"
        self.console_text.insert(tk.END, formatted_message)
        self.console_text.see(tk.END)
        self.root.update_idletasks()
        
    def get_domain(self):
        domain = self.domain_entry.get().strip()
        if not domain:
            messagebox.showerror("Error", "Please enter a target domain!")
            return None
        return domain.replace("http://", "").replace("https://", "").split("/")[0]
        
    def start_scan(self):
        domain = self.get_domain()
        if not domain or self.scan_running:
            return
            
        self.scan_running = True
        self.results_text.delete(1.0, tk.END)
        
        thread = threading.Thread(target=self.run_scan, args=(domain,))
        thread.daemon = True
        thread.start()
        
    def stop_scan(self):
        self.scan_running = False
        self.progress_var.set("Scan stopped")
        
    def run_scan(self, domain):
        try:
            self.log_to_console(f"Starting scan for {domain}")
            self.progress_var.set("Scanning subdomains...")
            
            # Subdomain scan
            found_count = 0
            for subdomain in subdomain_list[:20]:  # Limit for demo
                if not self.scan_running:
                    break
                try:
                    full_domain = f"{subdomain}.{domain}"
                    ip = socket.gethostbyname(full_domain)
                    found_count += 1
                    result = f"{full_domain} -> {ip}"
                    self.log_to_console(f"Found: {result}")
                    self.results_text.insert(tk.END, f"{result}\n")
                    self.results_text.see(tk.END)
                except:
                    pass
                    
            self.progress_var.set(f"Scan completed! Found {found_count} subdomains")
            self.log_to_console("Scan completed successfully!")
            
        except Exception as e:
            self.log_to_console(f"Error: {str(e)}")
        finally:
            self.scan_running = False

def main():
    root = tk.Tk()
    app = ReconShadowGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
