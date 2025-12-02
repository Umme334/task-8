# Quickstart: Simple Calculator

## Prerequisites

- **Python 3.10** or higher installed.
- `pip` installed (typically comes with Python).

## Installation

1.  Clone the repository.
2.  Install development dependencies (for testing):
    ```bash
    pip install pytest
    ```

## Running the Calculator

Run the script directly with an expression:

```bash
# Windows (PowerShell/CMD)
python src/main.py "2 + 2"
# Output: 4.0

# Division by zero
python src/main.py "10 / 0"
# Output: Error: Division by zero is not allowed
```

## Running Tests

Execute the test suite to verify mathematical correctness:

```bash
pytest
```
