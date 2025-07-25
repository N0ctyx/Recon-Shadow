# Installation Guide

## System Requirements

- Python 3.7 or higher
- pip package manager
- Internet connection for dependency installation

## Installation Methods

### Method 1: Quick Install (Recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/ReconShadow-v4.1-Enhanced.git

# Navigate to directory
cd ReconShadow-v4.1-Enhanced

# Install dependencies
pip install -r requirements.txt

# Run the tool
python reconshadow.py
```

### Method 2: Manual Installation

```bash
# Install required packages individually
pip install requests
pip install pandas
pip install fpdf2
pip install urllib3

# Download the script
wget https://raw.githubusercontent.com/yourusername/ReconShadow-v4.1-Enhanced/main/reconshadow.py

# Run the tool
python reconshadow.py
```

### Method 3: Virtual Environment (Recommended for Development)

```bash
# Create virtual environment
python -m venv reconshadow-env

# Activate virtual environment
# On Windows:
reconshadow-env\Scripts\activate
# On Linux/Mac:
source reconshadow-env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the tool
python reconshadow.py
```

## Troubleshooting

### Common Issues

1. **Python not found**
   - Ensure Python 3.7+ is installed
   - Add Python to system PATH

2. **Permission denied**
   - Run with administrator/sudo privileges
   - Check file permissions

3. **Module not found**
   - Reinstall dependencies: `pip install -r requirements.txt`
   - Use virtual environment

4. **Network issues**
   - Check internet connection
   - Configure proxy if needed

### Platform-Specific Notes

#### Windows
- Use PowerShell or Command Prompt
- May need to install Visual C++ Build Tools for some dependencies

#### Linux
- Install python3-pip if not available
- May need to use python3 instead of python

#### macOS
- Install Xcode Command Line Tools
- Use Homebrew for Python installation if needed

## Verification

Test the installation:

```bash
python reconshadow.py --help
```

If successful, you should see the ReconShadow banner and menu.

