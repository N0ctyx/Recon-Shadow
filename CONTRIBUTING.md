# Contributing to ReconShadow v4.1 Enhanced

We welcome contributions from the security community! This guide will help you get started.

## Ways to Contribute

### 🐛 Bug Reports
- Report bugs through GitHub Issues
- Include detailed reproduction steps
- Provide system information and error messages

### 💡 Feature Requests
- Suggest new features or improvements
- Explain the use case and benefits
- Discuss implementation approaches

### 🔧 Code Contributions
- Submit pull requests for bug fixes
- Add new detection signatures
- Improve existing functionality
- Enhance documentation

### 📖 Documentation
- Improve existing documentation
- Add usage examples
- Create tutorials and guides
- Fix typos and formatting

## Development Setup

### 1. Fork and Clone

```bash
# Fork the repository on GitHub
# Clone your fork
git clone https://github.com/yourusername/ReconShadow-v4.1-Enhanced.git
cd ReconShadow-v4.1-Enhanced
```

### 2. Create Development Environment

```bash
# Create virtual environment
python -m venv dev-env

# Activate virtual environment
# Windows:
dev-env\Scripts\activate
# Linux/Mac:
source dev-env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Create Feature Branch

```bash
# Create and switch to feature branch
git checkout -b feature/your-feature-name
```

## Code Style Guidelines

### Python Code Style
- Follow PEP 8 guidelines
- Use meaningful variable names
- Add comments for complex logic
- Keep functions focused and small

### Example Code Structure:
```python
def new_detection_function(target):
    """
    Brief description of the function
    
    Args:
        target (str): Target domain or URL
        
    Returns:
        list: List of findings or empty list
    """
    try:
        # Implementation here
        return results
    except Exception as e:
        # Error handling
        return []
```

## Adding New Takeover Signatures

### 1. Identify Service Patterns

Research the service to identify:
- Error messages indicating takeover opportunity
- CNAME patterns
- Response headers
- Content patterns

### 2. Add Detection Logic

```python
# Add to subdomain_takeover_scan function
elif "service-specific-error" in content_text:
    print(f"{R}[!]{W} POTENTIAL SERVICE TAKEOVER: {target}")
    takeover_vulnerabilities.append({
        "subdomain": target, 
        "service": "Service Name", 
        "risk": "High"
    })
```

### 3. Test the Detection

- Test with known vulnerable domains
- Verify no false positives
- Test edge cases

## Submission Guidelines

### Pull Request Process

1. **Update Documentation**
   - Update README.md if needed
   - Add to CHANGELOG.md
   - Update usage examples

2. **Test Your Changes**
   - Test on multiple platforms
   - Verify existing functionality works
   - Test new features thoroughly

3. **Create Pull Request**
   - Use descriptive title
   - Explain changes in detail
   - Reference related issues
   - Include testing information

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Testing
- [ ] Tested on Windows
- [ ] Tested on Linux
- [ ] Tested on macOS
- [ ] Added new test cases

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes
```

## Issue Guidelines

### Bug Report Template

```markdown
## Bug Description
Clear description of the bug

## Steps to Reproduce
1. Step one
2. Step two
3. Step three

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Environment
- OS: [e.g., Windows 10]
- Python Version: [e.g., 3.9.0]
- Tool Version: [e.g., v4.1.0]

## Additional Context
Any other relevant information
```

### Feature Request Template

```markdown
## Feature Description
Clear description of the proposed feature

## Use Case
Why is this feature needed?

## Proposed Solution
How should this feature work?

## Alternatives Considered
Other approaches you considered

## Additional Context
Any other relevant information
```

## Code Review Process

### What We Look For:
- **Functionality**: Does it work as intended?
- **Security**: No security vulnerabilities introduced
- **Performance**: Efficient implementation
- **Compatibility**: Works across platforms
- **Documentation**: Properly documented

### Review Timeline:
- Initial review within 48 hours
- Feedback provided for improvements
- Final approval after all requirements met

## Community Guidelines

### Be Respectful
- Use welcoming and inclusive language
- Respect different viewpoints
- Focus on constructive feedback

### Be Professional
- Keep discussions technical and relevant
- Avoid personal attacks or harassment
- Follow the code of conduct

### Be Helpful
- Help newcomers get started
- Share knowledge and experience
- Provide constructive feedback

## Recognition

Contributors will be:
- Listed in the README.md contributors section
- Mentioned in release notes
- Given credit for their contributions

## Getting Help

### Need Help?
- Create a GitHub Issue with "help wanted" label
- Join discussions in GitHub Discussions
- Review existing documentation and examples

### Contact
- GitHub Issues: Technical problems
- GitHub Discussions: General questions
- Security Issues: Create private security advisory

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to ReconShadow v4.1 Enhanced! 🚀

