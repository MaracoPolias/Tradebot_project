# Style Guide
**tradebot-project**

This document defines the coding and documentation standards used across tradebot-project.

---

## 1. Python Code Style
The project follows **PEP 8** with the following conventions:

### Naming
- Variables: `lower_case_with_underscores`
- Functions: `lower_case_with_underscores`
- Classes: `PascalCase`
- Constants: `UPPER_CASE_WITH_UNDERSCORES`

### Structure
- Keep functions short and focused  
- Avoid nested complexity where possible  
- Use descriptive naming (avoid `data`, `temp`, `x`)  
- Use type hints:
```python
def rsi(values: list[float], period: int = 14) -> float:
```

### Imports

- Standard library first
- Third-party next
- Local modules last

### Logging

- Use logging instead of print().

## 2. Documentation Style

- Use concise, professional language

- Prefer clarity over cleverness

- Use Markdown headings consistently

- Provide copy-paste-ready code examples

- Keep lines narrow for GitHub readability

- Update docs when behavior changes

## 3. Commit Message Guidelines

Use a descriptive prefix:

feat: add neural threshold tuner
fix: correct API error handling
docs: update contributing guide
refactor: simplify execution loop
test: add unit tests for position engine


Do not use vague messages like "update stuff".

## 4. File Structure Guidelines

- Group related components together

- Keep modules logically separated

- Avoid large monolithic files

- Prefer multiple small, cohesive modules

## 5. Editor and Linter Configuration

### Recommended tools:

- black or autopep8 for formatting

- flake8 for linting

- isort for import ordering

- mypy for type checking

Maintaining consistent style ensures readability, quality, and easier collaboration.
