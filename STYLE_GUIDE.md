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
