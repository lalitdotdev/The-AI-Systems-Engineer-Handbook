# 1. Python Fundamentals

> 📘 Volume I · 🟢 Beginner

---

## 📋 Learning outcome

By the end of this lesson you should be able to:

- [x] **Explain** what Python is and why it's dominant in AI/ML
- [x] **Implement** basic Python scripts using variables, data types, control flow, and functions
- [ ] **Run** the code and verify the output matches the expected result
- [ ] **Build** a small CLI tool that processes text files
- [ ] **Debug** a syntax error vs. runtime error
- [ ] **Measure** script execution time with `time`
- [ ] **Answer** the checkpoint interview questions

---

## 📚 Learn — Concepts

Python is a high-level, interpreted programming language known for its readability and extensive standard library. In AI engineering, Python serves as the lingua franca because:

1. **Ecosystem**: NumPy, pandas, PyTorch, TensorFlow, scikit-learn, Hugging Face
2. **Readability**: Code resembles pseudocode, making algorithms easier to understand
3. **Glue language**: Easy to call C/C++ libraries for performance-critical sections
4. **Community**: Massive open-source support and documentation

Core building blocks you'll master:

- **Variables & assignment**: `x = 5`, `name = "Alice"`
- **Data types**: `int`, `float`, `str`, `bool`, `list`, `dict`, `set`, `tuple`
- **Control flow**: `if/elif/else`, `for`, `while`, `break`, `continue`
- **Functions**: `def`, parameters, return values, scope, docstrings
- **Data structures**: Lists for sequences, dictionaries for key-value mapping
- **File I/O**: Reading/writing text and JSON files
- **Error handling**: `try/except/else/finally`

---

## 🔬 Understand — Mental models

### How Python executes code

```mermaid
flowchart TD
    A[Source Code (.py)] --> B{CPython Interpreter}
    B --> C[Compile to Bytecode]
    C --> D[Python Virtual Machine (PVM)]
    D --> E[Execute Bytecode]
    E --> F[Output / Side Effects]
```

### Variables as labels, not boxes

In Python, variables are **names that refer to objects**, not containers that hold values. This is crucial when understanding mutability:

```python
# Names refer to objects
a = [1, 2, 3]   # a refers to list object [1, 2, 3]
b = a           # b refers to the SAME object (not a copy!)
b.append(4)
print(a)        # [1, 2, 3, 4] - both names see the change
```

### Truthiness and falsiness

Python evaluates objects in boolean contexts using `__bool__` (or `__len__` for sequences):

```python
if []:          # False - empty list is falsy
    pass
if 0:           # False - zero is falsy
    pass
if None:        # False - None is falsy
    pass
if "":          # False - empty string is falsy
    pass
if [0]:         # True - non-empty list is truthy
    pass
```

---

## 💻 Implement — Build it from scratch

### Exercise: Build a CLI log analyzer

You'll create a program that analyzes a web server log file and outputs statistics.

**Starter code** (`code/starter.py`):

```python
#!/usr/bin/env python3
"""Log analyzer - complete the TODOs."""

import sys
from collections import Counter
from pathlib import Path


def parse_log_line(line: str) -> dict | None:
    """Parse a single log line (common log format).
    
    Returns dict with keys: ip, timestamp, method, path, status, size
    or None if line doesn't match format.
    """
    # TODO: Implement parsing
    # Example line: 127.0.0.1 - - [10/Oct/2024:14:30:00 +0000] "GET /index.html HTTP/1.1" 200 1024
    return None


def analyze_log_file(path: Path) -> dict:
    """Analyze the log file and return statistics."""
    stats = {
        "total_requests": 0,
        "successful_requests": 0,
        "failed_requests": 0,
        "total_bytes": 0,
        "methods": Counter(),
        "paths": Counter(),
        "status_codes": Counter(),
        "top_ips": Counter(),
    }
    
    # TODO: Read file line by line, parse each line, update stats
    
    return stats


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 starter.py <log_file>")
        sys.exit(1)
    
    log_path = Path(sys.argv[1])
    if not log_path.exists():
        print(f"Error: File {log_path} not found")
        sys.exit(1)
    
    stats = analyze_log_file(log_path)
    
    # TODO: Pretty-print the statistics
    print("Log Analysis Results:")
    print("=" * 50)
    # Print stats here


if __name__ == "__main__":
    main()
```

**Tests** (`code/test_starter.py`):

```python
import pytest
from starter import parse_log_line, analyze_log_file
from pathlib import Path


def test_parse_log_line():
    line = '127.0.0.1 - - [10/Oct/2024:14:30:00 +0000] "GET /index.html HTTP/1.1" 200 1024'
    result = parse_log_line(line)
    assert result is not None
    assert result["ip"] == "127.0.0.1"
    assert result["method"] == "GET"
    assert result["path"] == "/index.html"
    assert result["status"] == 200
    assert result["size"] == 1024


def test_analyze_log_file(tmp_path):
    log_content = '''\
127.0.0.1 - - [10/Oct/2024:14:30:00 +0000] "GET /index.html HTTP/1.1" 200 1024
192.168.1.1 - - [10/Oct/2024:14:30:01 +0000] "POST /api/data HTTP/1.1" 201 512
127.0.0.1 - - [10/Oct/2024:14:30:02 +0000] "GET /about HTTP/1.1" 404 0
'''
    log_file = tmp_path / "test.log"
    log_file.write_text(log_content)
    
    stats = analyze_log_file(log_file)
    assert stats["total_requests"] == 3
    assert stats["successful_requests"] == 2  # 200 + 201
    assert stats["failed_requests"] == 1      # 404
    assert stats["total_bytes"] == 1536       # 1024 + 512 + 0
    assert stats["methods"]["GET"] == 2
    assert stats["methods"]["POST"] == 1
    assert stats["paths"]["/index.html"] == 1
    assert stats["status_codes"][200] == 1
    assert stats["top_ips"]["127.0.0.1"] == 2
    assert stats["top_ips"]["192.168.1.1"] == 1
```

**Run & verify**:

```bash
# First, run the tests to see what's failing
python3 -m pytest code/test_starter.py -v

# Implement the TODOs in starter.py, then re-run tests
# Once tests pass, create a sample log file and run:
python3 code/starter.py code/sample.log
```

Expected output format:

```
Log Analysis Results:
==================================================
Total requests: 1245
Successful requests (2xx): 982
Failed requests (4xx+5xx): 263
Total bytes served: 4.2 MB
Most common method: GET (78%)
Most requested path: /api/users (45x)
Top IP address: 192.168.1.100 (89 requests)
Average response size: 3.4 KB
```

---

## 🧪 Practice — Exercises

1. **Temperature converter**: Write a script that converts between Celsius, Fahrenheit, and Kelvin.
2. **Word counter**: Count word frequencies in a text file, ignoring common stop words.
3. **Password generator**: Generate secure passwords of variable length with options for symbols/numbers.
4. **CSV to JSON converter**: Read a CSV file and output JSON arrays of objects.
5. **Prime number sieve**: Implement the Sieve of Eratosthenes to find all primes < N.

---

## 🏗️ Project

**Build a CLI Todo List Manager**

Features:
- Add tasks with description and priority (low/medium/high)
- List all tasks or filter by priority/completion status
- Mark tasks as complete/incomplete
- Delete tasks
- Persist tasks to a JSON file (`todos.json`)
- Command-line interface with subcommands: `add`, `list`, `done`, `delete`

**Definition of done**:

- [ ] All CRUD operations work correctly
- [ ] Data persists between runs (JSON file)
- [ ] Input validation (e.g., priority must be low/medium/high)
- [ ] Help text displayed with `-h` or `--help`
- [ ] Error handling for invalid commands/missing arguments
- [ ] Unit tests for core functions (at least 80% coverage)
- [ ] Code formatted with `black` and passes `flake8` linting

---

## 🚀 Production

Consider:

- **Input validation**: Never trust user input; sanitize and validate
- **Error handling**: Distinguish between user errors (exit code 1) and system errors (exit code 2)
- **Logging**: Use `logging` module instead of `print` for production scripts
- **Configuration**: Allow configuration via environment variables or config file
- **Testing**: Write tests before implementing (TDD approach)
- **Documentation**: Include docstrings and a README for your CLI tool
- **Packaging**: Consider making it installable with `pip` (`entry_points` in setup.py)
- **Security**: Avoid shell injection; use `subprocess` with arguments list if calling external commands

---

## 🎯 Checkpoint — Self-assessment (click to reveal)

<details>
<summary><strong>What is the difference between `==` and `is` in Python?</strong></summary>

`==` compares **values** (equality). `is` compares **object identity** (whether they are the same object in memory).

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True - same values
print(a is b)  # False - different objects
print(a is c)  # True - same object
```

For small integers (-5 to 256) and short strings, Python interns/caches objects, so `is` may work unexpectedly. Always use `==` for value comparison unless you specifically need to check identity (e.g., checking for `None` with `is None`).

</details>

<details>
<summary><strong>When should you use a list vs. a tuple?</strong></summary>

Use a **list** when you need a **mutable** sequence (you'll add/remove/change elements).

Use a **tuple** when you need an **immutable** sequence (fixed collection that shouldn't change).

Guidelines:
- Tuples are hashable and can be used as dict keys or set elements
- Tuples convey intent: "this is a fixed collection of related values"
- Lists are for collections that will vary in size or content
- Return multiple values from a function as a tuple: `return x, y`
- Use tuples for dictionary items: `for key, value in my_dict.items():`

Example:
```python
# Point in 2D space - immutable, use tuple
point = (x, y)

# List of students in a class - mutable, use list
students = ["Alice", "Bob", "Charlie"]
students.append("David")  # OK
```

</details>

<details>
<summary><strong>What does `if __name__ == "__main__":` do?</strong></summary>

This conditional checks whether the Python script is being run **directly** (as the main program) or being **imported** as a module into another script.

- When you run `python3 myscript.py`, `__name__` is set to `"__main__"` so the block executes.
- When you import the script (`import myscript`), `__name__` is set to the module name (`"myscript"`), so the block is skipped.

This allows you to:
1. Make a file both importable as a module AND runnable as a script
2. Put test code, demos, or CLI interfaces in the `if __name__ == "__main__":` block
3. Keep the main logic in functions/classes that can be reused

Example:
```python
def fibonacci(n):
    """Return the nth Fibonacci number."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

if __name__ == "__main__":
    # This runs only when script is executed directly
    for i in range(10):
        print(fibonacci(i))
```

</details>
