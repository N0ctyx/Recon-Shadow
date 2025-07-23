#!/usr/bin/env python3
"""
ReconShadow v4.0 - Quick Test Script
Verify that all components are working correctly
"""

import sys
import importlib
import subprocess

def test_imports():
    """Test if all required modules can be imported"""
    print("🧪 Testing Python imports...")
    
    required_modules = [
        'tkinter', 'requests', 'socket', 'subprocess', 
        'threading', 'concurrent.futures', 'pathlib'
    ]
    
    failed_imports = []
    
    for module in required_modules:
        try:
            importlib.import_module(module)
            print(f"✅ {module}")
        except ImportError:
            print(f"❌ {module}")
            failed_imports.append(module)
    
    if failed_imports:
        print(f"\n⚠️ Missing modules: {', '.join(failed_imports)}")
        print("Run 'pip install -r requirements.txt' to install missing modules")
        return False
    
    print("✅ All imports successful!")
    return True

def test_gui():
    """Test if GUI can be launched"""
    print("\n🖥️ Testing GUI launch...")
    
    try:
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()  # Hide the window
        root.destroy()
        print("✅ GUI framework working!")
        return True
    except Exception as e:
        print(f"❌ GUI test failed: {e}")
        return False

def test_network():
    """Test basic network functionality"""
    print("\n🌐 Testing network functionality...")
    
    try:
        import socket
        # Test DNS resolution
        socket.gethostbyname('google.com')
        print("✅ DNS resolution working!")
        
        # Test HTTP requests
        import requests
        response = requests.get('https://httpbin.org/ip', timeout=5)
        if response.status_code == 200:
            print("✅ HTTP requests working!")
            return True
        else:
            print(f"⚠️ HTTP request returned status {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Network test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 ReconShadow v4.0 - System Test")
    print("=" * 40)
    
    tests = [
        ("Python Imports", test_imports),
        ("GUI Framework", test_gui),
        ("Network Functions", test_network)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n📋 Running {test_name} test...")
        if test_func():
            passed += 1
    
    print("\n" + "=" * 40)
    print(f"📊 Test Results: {passed}/{total} passed")
    
    if passed == total:
        print("🎉 All tests passed! ReconShadow is ready to use.")
        print("🚀 You can now run 'python setup.py' to build executables")
    else:
        print("⚠️ Some tests failed. Please check the requirements.")
    
    return passed == total

if __name__ == "__main__":
    try:
        success = main()
        input(f"\n{'✅ Tests completed successfully!' if success else '❌ Tests failed.'} Press Enter to exit...")
    except KeyboardInterrupt:
        print("\n\n⏹️ Tests interrupted by user.")
    except Exception as e:
        print(f"\n❌ Test error: {e}")
        input("Press Enter to exit...")
