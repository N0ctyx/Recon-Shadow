#!/usr/bin/env python3
"""
ReconShadow v4.0 - Enhanced Edition for Bug Bounty
Setup script for pip installation
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

# Read requirements
requirements = []
try:
    with open('requirements.txt', 'r', encoding='utf-8') as f:
        requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]
except FileNotFoundError:
    requirements = [
        'requests>=2.25.1',
        'pandas>=1.3.0',
        'fpdf2>=2.5.0',
        'urllib3>=1.26.0',
        'openpyxl>=3.0.0'
    ]

setup(
    name="reconshadow",
    version="4.0.0",
    author="N0ctyx",
    author_email="n0ctyx@example.com",  # Replace with actual email
    description="Stealth Reconnaissance & Vulnerability Discovery Tool for Bug Bounty",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/n0ctyx/reconshadow",  # Replace with actual URL
    project_urls={
        "Bug Reports": "https://github.com/n0ctyx/reconshadow/issues",
        "Source": "https://github.com/n0ctyx/reconshadow",
        "Documentation": "https://github.com/n0ctyx/reconshadow#readme",
    },
    packages=find_packages(),
    py_modules=["reconshadow"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Developers",
        "Topic :: Security",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: System :: Networking",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
    ],
    keywords=[
        "security", "reconnaissance", "subdomain", "enumeration", 
        "vulnerability", "scanner", "bug-bounty", "penetration-testing",
        "dns", "port-scanner", "web-crawler", "cybersecurity"
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=0.5",
        ],
    },
    entry_points={
        "console_scripts": [
            "reconshadow=reconshadow:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.txt", "*.md", "*.rst"],
    },
    zip_safe=False,
    platforms=["any"],
    license="MIT",
    test_suite="tests",
)