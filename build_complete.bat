@echo off
title ReconShadow v4.0 - Complete Build System
color 0A

echo.
echo ================================================
echo  ReconShadow v4.0 - Complete Build System
echo ================================================
echo  Creating professional executable distribution
echo  Made with love in Tunisia by N0ctyx
echo ================================================
echo.

echo [STEP 1/5] System Check...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found! Please install Python 3.7+
    pause
    exit /b 1
)
echo [SUCCESS] Python found!

echo.
echo [STEP 2/5] Testing System...
python test_system.py
if errorlevel 1 (
    echo [WARNING] Some tests failed, but continuing...
)

echo.
echo [STEP 3/5] Installing Requirements...
python -m pip install --upgrade pip
python -m pip install pyinstaller requests pandas fpdf2 urllib3 openpyxl
if errorlevel 1 (
    echo [ERROR] Failed to install requirements!
    pause
    exit /b 1
)

echo.
echo [STEP 4/5] Building Executables...
echo Building GUI version...
python -m PyInstaller --onefile --windowed --name=ReconShadow_GUI reconshadow_gui.py

echo Building CLI version...
python -m PyInstaller --onefile --console --name=ReconShadow_CLI reconshadow.py

if not exist "dist\ReconShadow_GUI.exe" (
    echo [ERROR] GUI executable not created!
    pause
    exit /b 1
)

if not exist "dist\ReconShadow_CLI.exe" (
    echo [ERROR] CLI executable not created!
    pause
    exit /b 1
)

echo.
echo [STEP 5/5] Creating Distribution Package...

if exist "ReconShadow_v4.0_Complete" rmdir /s /q "ReconShadow_v4.0_Complete"
mkdir "ReconShadow_v4.0_Complete"

copy "dist\ReconShadow_GUI.exe" "ReconShadow_v4.0_Complete\"
copy "dist\ReconShadow_CLI.exe" "ReconShadow_v4.0_Complete\"
copy "README.md" "ReconShadow_v4.0_Complete\"
copy "LICENSE" "ReconShadow_v4.0_Complete\"

echo @echo off > "ReconShadow_v4.0_Complete\Launch_GUI.bat"
echo title ReconShadow v4.0 - GUI Edition >> "ReconShadow_v4.0_Complete\Launch_GUI.bat"
echo echo Starting ReconShadow GUI... >> "ReconShadow_v4.0_Complete\Launch_GUI.bat"
echo ReconShadow_GUI.exe >> "ReconShadow_v4.0_Complete\Launch_GUI.bat"
echo pause >> "ReconShadow_v4.0_Complete\Launch_GUI.bat"

echo @echo off > "ReconShadow_v4.0_Complete\Launch_CLI.bat"
echo title ReconShadow v4.0 - CLI Edition >> "ReconShadow_v4.0_Complete\Launch_CLI.bat"
echo echo Starting ReconShadow CLI... >> "ReconShadow_v4.0_Complete\Launch_CLI.bat"
echo ReconShadow_CLI.exe >> "ReconShadow_v4.0_Complete\Launch_CLI.bat"
echo pause >> "ReconShadow_v4.0_Complete\Launch_CLI.bat"

echo # ReconShadow v4.0 - Ready to Use! > "ReconShadow_v4.0_Complete\QUICK_START.txt"
echo. >> "ReconShadow_v4.0_Complete\QUICK_START.txt"
echo ## How to Use: >> "ReconShadow_v4.0_Complete\QUICK_START.txt"
echo 1. Double-click Launch_GUI.bat for graphical interface >> "ReconShadow_v4.0_Complete\QUICK_START.txt"
echo 2. Double-click Launch_CLI.bat for command line interface >> "ReconShadow_v4.0_Complete\QUICK_START.txt"
echo 3. Enter a target domain when prompted >> "ReconShadow_v4.0_Complete\QUICK_START.txt"
echo 4. Follow the on-screen instructions >> "ReconShadow_v4.0_Complete\QUICK_START.txt"
echo. >> "ReconShadow_v4.0_Complete\QUICK_START.txt"
echo ## Legal Notice: >> "ReconShadow_v4.0_Complete\QUICK_START.txt"
echo Only use on domains you own or have permission to test! >> "ReconShadow_v4.0_Complete\QUICK_START.txt"
echo. >> "ReconShadow_v4.0_Complete\QUICK_START.txt"
echo Made with love in Tunisia by N0ctyx >> "ReconShadow_v4.0_Complete\QUICK_START.txt"

echo.
echo [CLEANUP] Removing build artifacts...
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"
if exist "*.spec" del "*.spec"

echo.
echo ================================================
echo  BUILD COMPLETED SUCCESSFULLY!
echo ================================================
echo.
echo Your complete ReconShadow distribution is ready:
echo 📁 Folder: ReconShadow_v4.0_Complete
echo 🖥️  GUI Version: Launch_GUI.bat
echo 💻 CLI Version: Launch_CLI.bat
echo 📖 Documentation: README.md
echo 🚀 Quick Start: QUICK_START.txt
echo.
echo You can now:
echo 1. Test the executables locally
echo 2. Share the folder with others
echo 3. Upload to GitHub for distribution
echo.
echo Happy hunting! Made with love in Tunisia 🇹🇳
echo.
pause
