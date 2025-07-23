@echo off
title ReconShadow v4.0 - Automated Installer
color 0A

echo.
echo ========================================
echo  ReconShadow v4.0 - Automated Installer
echo ========================================
echo  Made with love in Tunisia by N0ctyx
echo ========================================
echo.

echo [INFO] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH!
    echo [INFO] Please install Python 3.7+ from https://python.org
    pause
    exit /b 1
)

echo [SUCCESS] Python found!
echo.

echo [INFO] Installing required packages...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

if errorlevel 1 (
    echo [ERROR] Failed to install requirements!
    pause
    exit /b 1
)

echo [SUCCESS] Requirements installed!
echo.

echo [INFO] Building executables...
python setup.py

if errorlevel 1 (
    echo [ERROR] Build process failed!
    pause
    exit /b 1
)

echo.
echo [SUCCESS] Installation completed successfully!
echo [INFO] Check the 'ReconShadow_v4.0_Distribution' folder
echo [INFO] You can now run the GUI or CLI versions
echo.
pause
