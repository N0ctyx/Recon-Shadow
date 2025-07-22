# Contributing to ReconShadow 🇹🇳

First off, thank you for considering contributing to ReconShadow! It's people like you that make ReconShadow such a great tool for the security community.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Guidelines](#development-guidelines)
- [Pull Request Process](#pull-request-process)
- [Bug Reports](#bug-reports)
- [Feature Requests](#feature-requests)
- [Security Issues](#security-issues)

## 🤝 Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

### Our Standards

- **Be Respectful**: Treat everyone with respect and kindness
- **Be Inclusive**: Welcome newcomers and help them learn
- **Be Constructive**: Provide helpful feedback and suggestions
- **Be Professional**: Maintain a professional tone in all interactions

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- Git
- Basic understanding of networking and security concepts
- Familiarity with Python development

### Setting Up Development Environment

1. **Fork the Repository**
   ```bash
   # Fork on GitHub, then clone your fork
   git clone https://github.com/yourusername/reconshadow.git
   cd reconshadow
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On Linux/macOS
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # If available
   ```

4. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 🛠️ How Can I Contribute?

### 🐛 Bug Fixes
- Fix existing bugs listed in Issues
- Improve error handling
- Enhance cross-platform compatibility

### ✨ New Features
- Add new scanning modules
- Improve existing functionality
- Add new vulnerability detection patterns
- Enhance reporting capabilities

### 📚 Documentation
- Improve README.md
- Add code comments
- Create usage examples
- Write tutorials

### 🧪 Testing
- Add unit tests
- Test on different platforms
- Validate with various target types
- Performance testing

### 🎨 UI/UX Improvements
- Enhance terminal output
- Improve progress indicators
- Better error messages
- Color scheme improvements

## 📝 Development Guidelines

### Code Style

- **Follow PEP 8**: Use Python's official style guide
- **Use Type Hints**: Add type hints where appropriate
- **Write Docstrings**: Document all functions and classes
- **Keep Functions Small**: Aim for single responsibility principle

### Example Code Style

```python
def scan_subdomain(subdomain: str, domain: str, timeout: int = 5) -> Optional[Tuple[str, str]]:
    """
    Resolve a subdomain and return the full domain and IP address.
    
    Args:
        subdomain: The subdomain to test (e.g., 'www')
        domain: The base domain (e.g., 'example.com')
        timeout: DNS resolution timeout in seconds
        
    Returns:
        Tuple of (full_domain, ip_address) if successful, None otherwise
        
    Raises:
        socket.error: If DNS resolution fails
    """
    try:
        full_domain = f"{subdomain}.{domain}"
        ip = socket.gethostbyname(full_domain)
        return full_domain, ip
    except socket.error:
        return None
```

### Commit Messages

Use clear and descriptive commit messages:

```bash
# Good
git commit -m "Add support for IPv6 DNS resolution"
git commit -m "Fix timeout handling in port scanner"
git commit -m "Update subdomain wordlist with 10 new entries"

# Bad
git commit -m "fix bug"
git commit -m "update"
git commit -m "changes"
```

### Branch Naming

Use descriptive branch names:

```bash
feature/ipv6-support
bugfix/timeout-handling
enhancement/better-reporting
docs/installation-guide
```

## 🔄 Pull Request Process

1. **Update Documentation**
   - Update README.md if needed
   - Add docstrings to new functions
   - Update CHANGELOG.md

2. **Test Your Changes**
   - Test on multiple platforms if possible
   - Ensure existing functionality still works
   - Add tests for new features

3. **Create Pull Request**
   - Use a clear title and description
   - Reference related issues
   - Include screenshots if UI changes
   - List breaking changes if any

4. **Pull Request Template**
   ```markdown
   ## Description
   Brief description of changes
   
   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Breaking change
   - [ ] Documentation update
   
   ## Testing
   - [ ] Tested on Windows
   - [ ] Tested on Linux
   - [ ] Tested on macOS
   
   ## Checklist
   - [ ] Code follows style guidelines
   - [ ] Self-review completed
   - [ ] Documentation updated
   - [ ] No breaking changes (or documented)
   ```

## 🐛 Bug Reports

When filing a bug report, please include:

### Required Information
- **ReconShadow Version**: Which version you're using
- **Operating System**: Windows/Linux/macOS and version
- **Python Version**: Output of `python --version`
- **Error Message**: Full error message and stack trace
- **Steps to Reproduce**: Detailed steps to reproduce the issue
- **Expected Behavior**: What you expected to happen
- **Actual Behavior**: What actually happened

### Bug Report Template
```markdown
**ReconShadow Version:** 4.0.0
**OS:** Windows 11
**Python Version:** 3.9.7

**Description:**
Brief description of the bug

**Steps to Reproduce:**
1. Run `python reconshadow.py`
2. Select option 1
3. Enter domain 'example.com'
4. Error occurs

**Expected Behavior:**
Should scan subdomains successfully

**Actual Behavior:**
Crashes with timeout error

**Error Message:**
```
[Full error message here]
```

**Additional Context:**
Any other relevant information
```

## 💡 Feature Requests

We welcome feature requests! Please provide:

- **Clear Description**: What feature you'd like to see
- **Use Case**: Why this feature would be useful
- **Implementation Ideas**: Any thoughts on how it could work
- **Examples**: Similar features in other tools

## 🔒 Security Issues

**IMPORTANT**: Do not report security vulnerabilities through public GitHub issues.

### Reporting Security Issues

1. **Email**: Send details to [security@example.com] (replace with actual email)
2. **Include**: 
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

3. **Response**: We'll respond within 48 hours
4. **Disclosure**: We follow responsible disclosure practices

## 🏷️ Issue Labels

We use the following labels to categorize issues:

- `bug` - Something isn't working
- `enhancement` - New feature or request
- `documentation` - Improvements to documentation
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention is needed
- `question` - Further information is requested
- `wontfix` - This will not be worked on

## 🎯 Development Priorities

Current development priorities:

1. **Cross-platform Compatibility**: Ensure consistent behavior across OS
2. **Performance Optimization**: Improve scanning speed and memory usage
3. **Enhanced Reporting**: Better report formats and visualizations
4. **API Integration**: Support for external APIs and services
5. **Plugin System**: Modular architecture for extensions

## 📞 Getting Help

If you need help with contributing:

- **GitHub Discussions**: Ask questions in GitHub Discussions
- **Issues**: Check existing issues for similar problems
- **Documentation**: Read the README and code comments
- **Community**: Join our community channels (if available)

## 🙏 Recognition

Contributors will be recognized in:

- **README.md**: Contributors section
- **CHANGELOG.md**: Release notes
- **GitHub**: Contributor graphs and statistics

## 📄 License

By contributing to ReconShadow, you agree that your contributions will be licensed under the MIT License.

---

<div align="center">

**🇹🇳 Thank you for contributing to ReconShadow! 🇹🇳**

*Together, we make the internet more secure, one subdomain at a time.*

</div>