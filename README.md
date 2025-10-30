# python-lib-package-module

**An example project demonstrating Python library, package, and module structure.**

This project serves as a practical example of how to organize Python code into libraries, packages, and modules. It includes a simple mathematics library with basic arithmetic operations, vector operations, and other mathematical utilities to illustrate best practices in Python project structure.

## What You'll Learn

This example project demonstrates:

- **Module**: Individual Python files (e.g., `add.py`, `multi.py`) containing functions and classes
- **Package**: Directories containing `__init__.py` files (e.g., `mathlib/`, `mathlib/arithmetic/`) that organize related modules
- **Library**: The complete distributable collection of packages and modules that can be installed and imported

## Features

- **Arithmetic Operations**: Basic mathematical operations
- **Vector Operations**: Element-wise operations and dot products
- **Custom Math Functions**: Extended mathematical utilities

## Installation

### Using pip

```bash
pip install dist/python_lib_package_module-0.1.0-py3-none-any.whl
```

### Using uv (recommended)

```bash
# Install from wheel
uv pip install dist/python_lib_package_module-0.1.0-py3-none-any.whl

# Or install directly from source
uv pip install .

# For development (editable mode)
uv pip install -e .
```

## Usage

### Arithmetic Operations

```python
from mathlib.arithmetic import add

result = add(5, 3)
print(result)  # Output: 8
```

### Vector Operations

```python
from mathlib.vector import add, multi, dot

# Element-wise addition
v1 = [1, 2, 3]
v2 = [4, 5, 6]
result = add(v1, v2)
print(result)  # Output: [5, 7, 9]

# Element-wise multiplication
result = multi(v1, v2)
print(result)  # Output: [4, 10, 18]

# Dot product
result = dot(v1, v2)
print(result)  # Output: 32 (1*4 + 2*5 + 3*6)
```

### Other Mathematical Functions

```python
from mathlib.etc import crazymath

result = crazymath(4, 2)
print(result)  # Output: 8.0 (4 + 2 * 4 / 2)
```

## API Reference

### `mathlib.arithmetic`

- `add(a, b)` - Returns the sum of two numbers

### `mathlib.vector`

- `add(a, b)` - Element-wise addition of two vectors
- `multi(a, b)` - Element-wise multiplication of two vectors
- `dot(a, b)` - Calculates the dot product of two vectors

**Note**: All vector functions require vectors of equal length.

### `mathlib.etc`

- `crazymath(a, b)` - Calculates `a + b * a / b`

## Development

### Building from Source

```bash
# Using uv
uv build

# This will create a wheel file in the dist/ directory
```

### Running the Example

```bash
python main.py
```

## Requirements

- Python >= 3.12

## Project Structure

```
python_lib_package_module/
├── mathlib/
│   ├── arithmetic/
│   │   ├── __init__.py
│   │   └── add.py
│   ├── vector/
│   │   ├── __init__.py
│   │   └── multi.py
│   └── etc/
│       ├── __init__.py
│       └── crazymath.py
├── main.py
├── pyproject.toml
└── README.md
```

## License

This project is open source and available under the MIT License.

