# CLI Contract: Simple Calculator

## Command Interface

The calculator is executed via the command line interface (CLI).

### Usage

```bash
python src/main.py "<expression>"
```

### Inputs

- **Argument 1**: A single string containing the mathematical expression.
  - Example: `"2 + 2"`
  - Example: `"10 / 5"`

### Outputs

**Success Case**:
- **Stream**: `stdout`
- **Format**: The result number (integer or float).
- **Example**:
  ```text
  4.0
  ```

**Error Case**:
- **Stream**: `stdout` (or `stderr` per simple requirement, but Constitution II implies "clear error messages").
- **Format**: Prefix "Error: " followed by the description.
- **Example**:
  ```text
  Error: Division by zero is not allowed
  ```
  ```text
  Error: Invalid input expression
  ```

## Library Interface (Internal)

If used as a library:

```python
def calculate(expression: str) -> float | str:
    """
    Parses and evaluates a simple math expression.
    
    Args:
        expression (str): The string to evaluate (e.g., "2 + 2").
        
    Returns:
        float: The result of the calculation.
        
    Raises:
        ValueError: If input is invalid or contains multiple operators.
        ZeroDivisionError: If division by zero is attempted.
    """
```
