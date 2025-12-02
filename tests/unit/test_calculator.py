import pytest
from src.calculator import calculate
from src.errors import CalculatorError

def test_calculate_import():
    """Verify we can import the calculate function."""
    assert callable(calculate)

def test_calculate_addition():
    """Test basic addition."""
    assert calculate("2 + 3") == 5.0
    assert calculate("2.5 + 3.5") == 6.0
    assert calculate("-1 + -5") == -6.0

def test_calculate_subtraction():
    """Test basic subtraction."""
    assert calculate("5 - 2") == 3.0
    assert calculate("2 - 5") == -3.0
    assert calculate("-1 - -5") == 4.0

def test_calculate_multiplication():
    """Test basic multiplication."""
    assert calculate("4 * 5") == 20.0
    assert calculate("-2 * 3") == -6.0
    assert calculate("2.5 * 4") == 10.0

def test_calculate_division():
    """Test basic division."""
    assert calculate("10 / 2") == 5.0
    assert calculate("7 / 2") == 3.5

def test_calculate_division_by_zero():
    """Test division by zero."""
    with pytest.raises(CalculatorError, match="Division by zero is not allowed"):
        calculate("10 / 0")

def test_calculate_invalid_input():
    """Test invalid inputs."""
    with pytest.raises(CalculatorError, match="Invalid input expression"):
        calculate("2 + 3 * 4")  # Multiple operators
    with pytest.raises(CalculatorError, match="Invalid input expression"):
        calculate("abc")
    with pytest.raises(CalculatorError, match="Invalid input expression"):
        calculate("2 +")