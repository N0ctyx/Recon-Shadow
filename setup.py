#!/usr/bin/env python3
"""
ReconShadow v4.0 - Setup Script
Automated setup and executable builder for Windows
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def install_requirements():
    """Install required packages"""
    print("🔧 Installing requirements...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("✅ Requirements installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install requirements: {e}")
        return False

def build_executable():
    """Build executable using PyInstaller"""
    print("🏗️ Building executable...")
    
    # Build GUI version
    gui_cmd = [
        sys.executable, '-m', 'PyInstaller',
        '--onefile',
        '--windowed',
        '--name=ReconShadow_GUI',
        '--icon=NONE',
        'reconshadow_gui.py'
    ]
    
    # Build CLI version
    cli_cmd = [
        sys.executable, '-m', 'PyInstaller',
        '--onefile',
        '--console',
        '--name=ReconShadow_CLI',
        '--icon=NONE',
        'reconshadow.py'
    ]
    
    try:
        print("Building GUI version...")
        subprocess.check_call(gui_cmd)
        
        print("Building CLI version...")
        subprocess.check_call(cli_cmd)
        
        print("✅ Executables built successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed: {e}")
        return False

def create_distribution():
    """Create distribution folder"""
    print("📦 Creating distribution package...")
    
    dist_folder = Path("ReconShadow_v4.0_Distribution")
    if dist_folder.exists():
        shutil.rmtree(dist_folder)
    
    dist_folder.mkdir()
    
    # Copy executables
    gui_exe = Path("dist/ReconShadow_GUI.exe")
    cli_exe = Path("dist/ReconShadow_CLI.exe")
    
    if gui_exe.exists():
        shutil.copy2(gui_exe, dist_folder / "ReconShadow_GUI.exe")
        print("✅ Copied GUI executable")
    
    if cli_exe.exists():
        shutil.copy2(cli_exe, dist_folder / "ReconShadow_CLI.exe")
        print("✅ Copied CLI executable")
    
    # Create launcher batch files
    gui_batch = """@echo off
title ReconShadow v4.0 - GUI Edition
echo Starting ReconShadow GUI...
ReconShadow_GUI.exe
pause"""
    
    cli_batch = """@echo off
title ReconShadow v4.0 - CLI Edition
echo Starting ReconShadow CLI...
ReconShadow_CLI.exe
pause"""
    
    with open(dist_folder / "Launch_GUI.bat", "w") as f:
        f.write(gui_batch)
    
    with open(dist_folder / "Launch_CLI.bat", "w") as f:
        f.write(cli_batch)
    
    # Create README
    readme_content = """# ReconShadow v4.0 - Distribution Package

## Quick Start
1. Double-click `Launch_GUI.bat` for the graphical interface
2. Double-click `Launch_CLI.bat` for the command-line interface
3. Or run the executables directly:
   - `ReconShadow_GUI.exe` - Modern GUI version
   - `ReconShadow_CLI.exe` - Traditional CLI version

## Features
- Subdomain enumeration
- DNS record analysis
- Port scanning
- Vulnerability detection
- Comprehensive reporting

## System Requirements
- Windows 10 or later
- Internet connection
- Administrator privileges (recommended)

## Legal Notice
This tool is for educational and authorized testing purposes only.
Users are responsible for complying with applicable laws and regulations.

## Support
GitHub: https://github.com/n0ctyx/reconshadow

---
Made with ❤️ in Tunisia by N0ctyx 🇹🇳
"""
    
    with open(dist_folder / "README.txt", "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    print(f"✅ Distribution package created: {dist_folder}")
    return True

def cleanup():
    """Clean up build artifacts"""
    print("🧹 Cleaning up...")
    
    cleanup_items = ["build", "dist", "__pycache__", "*.spec"]
    
    for item in cleanup_items:
        if item.endswith("*"):
            import glob
            for file in glob.glob(item):
                try:
                    os.remove(file)
                except:
                    pass
        else:
            path = Path(item)
            if path.exists():
                if path.is_dir():
                    shutil.rmtree(path)
                else:
                    path.unlink()
    
    print("✅ Cleanup completed")

def main():
    """Main setup process"""
    print("🚀 ReconShadow v4.0 - Automated Setup")
    print("=" * 50)
    
    # Check if we have the required files
    required_files = ["reconshadow.py", "reconshadow_gui.py", "requirements.txt"]
    for file in required_files:
        if not Path(file).exists():
            print(f"❌ Required file missing: {file}")
            return False
    
    # Step 1: Install requirements
    if not install_requirements():
        return False
    
    # Step 2: Build executables
    if not build_executable():
        return False
    
    # Step 3: Create distribution
    if not create_distribution():
        return False
    
    # Step 4: Cleanup
    cleanup()
    
    print("\n🎉 Setup completed successfully!")
    print("📦 Your distribution package is ready in 'ReconShadow_v4.0_Distribution' folder")
    print("🚀 You can now share this folder with others for easy installation")
    
    return True

if __name__ == "__main__":
    try:
        success = main()
        if not success:
            input("\n❌ Setup failed. Press Enter to exit...")
        else:
            input("\n✅ Setup completed. Press Enter to exit...")
    except KeyboardInterrupt:
        print("\n\n⏹️ Setup interrupted by user.")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        input("Press Enter to exit...")
