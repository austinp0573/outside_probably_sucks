# Contributing to Weather Email Notifier

Thank you for your interest in contributing to Weather Email Notifier! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for all contributors.

## Getting Started

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/your-username/weather-email-notifier.git
   cd weather-email-notifier
   ```
3. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate  # Windows
   # OR
   source .venv/bin/activate     # Unix/MacOS
   pip install -r requirements.txt
   ```
4. Create a new branch for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Guidelines

### Code Style

- Follow PEP 8 style guidelines
- Use type hints for function parameters and return values
- Write descriptive variable and function names
- Include docstrings for modules, classes, and functions
- Keep functions focused and concise

### Testing

- Write tests for new features and bug fixes
- Ensure all tests pass before submitting changes
- Maintain or improve code coverage
- Run tests using:
  ```bash
  python -m unittest discover tests
  ```

### Logging

- Use the established logging system
- Include appropriate log levels (INFO, WARNING, ERROR)
- Add context to log messages
- Don't log sensitive information

### Documentation

- Update README.md for new features or changes
- Keep code comments clear and relevant
- Document configuration options
- Update docstrings as needed

## Pull Request Process

1. Update documentation to reflect your changes
2. Add or update tests as needed
3. Ensure all tests pass
4. Update the README.md if needed
5. Create a pull request with a clear title and description
6. Link any related issues

### Pull Request Description Template

```markdown
## Description
Brief description of the changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring
- [ ] Other (please describe)

## Testing
Describe the tests you ran and any relevant results

## Checklist
- [ ] My code follows the project's style guidelines
- [ ] I have added/updated tests
- [ ] All tests pass
- [ ] I have updated the documentation
- [ ] My changes generate no new warnings
```

## Feature Requests and Bug Reports

- Use the GitHub issue tracker
- Provide clear, detailed descriptions
- Include steps to reproduce bugs
- Suggest solutions if possible

## Environment Setup Tips

### Gmail Configuration
1. Enable 2-factor authentication
2. Generate an app password
3. Use the app password in `.env`

### OpenWeatherMap API
1. Sign up for an API key
2. Start with the free tier
3. Monitor API usage

## Questions or Problems?

- Check existing issues first
- Open a new issue if needed
- Be clear and provide context
- Follow up on your issues

Thank you for contributing! 