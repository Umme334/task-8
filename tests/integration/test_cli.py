import subprocess
import sys
import pytest

def run_calculator(expression):
    """Helper to run the calculator CLI."""
    # Use sys.executable to ensure we use the same python interpreter
    result = subprocess.run(
        [sys.executable, "src/main.py", expression],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def test_cli_addition():
    assert run_calculator("2 + 3") == "5.0"

def test_cli_error_division_by_zero():
    output = run_calculator("10 / 0")
    assert "Error: Division by zero is not allowed" in output

def test_cli_error_invalid_input():
    output = run_calculator("abc")
    assert "Error: Invalid input expression" in output
