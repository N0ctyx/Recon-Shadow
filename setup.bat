@echo off
echo 🔍 ReconShadow v4.1 Enhanced Setup
echo ==================================

echo 📋 Checking Python version...
python --version
if %errorlevel% neq 0 (
    echo ❌ Python not found. Please install Python 3.7+
    pause
    exit /b 1
)

echo 📦 Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ❌ Failed to install dependencies
    pause
    exit /b 1
)

echo 🧪 Testing installation...
python -c "import requests, pandas, fpdf; print(\"✅ All modules imported successfully\")"
if %errorlevel% neq 0 (
    echo ❌ Setup failed - please check error messages above
    pause
    exit /b 1
)

echo 🎉 Setup completed successfully!
echo.
echo 🚀 You can now run ReconShadow:
echo    python reconshadow.py
echo.
echo 📖 For usage guide, see: docs\USAGE.md
pause

