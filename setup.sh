#!/bin/bash

# ReconShadow v4.1 Enhanced Setup Script

echo "🔍 ReconShadow v4.1 Enhanced Setup"
echo "=================================="

# Check Python version
echo "📋 Checking Python version..."
python_version=$(python --version 2>&1)
echo "Found: $python_version"

# Check if Python 3.7+
if python -c "import sys; exit(0 if sys.version_info >= (3,7) else 1)"; then
    echo "✅ Python version is compatible"
else
    echo "❌ Python 3.7+ required"
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

# Test installation
echo "🧪 Testing installation..."
python -c "import requests, pandas, fpdf; print(\"✅ All modules imported successfully\")"

if [ $? -eq 0 ]; then
    echo "🎉 Setup completed successfully!"
    echo ""
    echo "🚀 You can now run ReconShadow:"
    echo "   python reconshadow.py"
    echo ""
    echo "📖 For usage guide, see: docs/USAGE.md"
else
    echo "❌ Setup failed - please check error messages above"
    exit 1
fi

