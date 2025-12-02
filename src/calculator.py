import re
from src.errors import CalculatorError

def calculate(expression: str) -> float:
    """
    Parses and evaluates a simple math expression.
    
    Args:
        expression (str): The string to evaluate (e.g., "2 + 2").
        
    Returns:
        float: The result of the calculation.
        
    Raises:
        CalculatorError: If input is invalid or contains multiple operators.
    """
    # Regex to split operands and operator: number, operator, number
    # Supports integers, floats, and negative numbers
    match = re.match(r'^\s*(-?\d+(?:\.\d+)?)\s*([+\-*/])\s*(-?\d+(?:\.\d+)?)\s*$', expression)
    
    if not match:
        raise CalculatorError("Invalid input expression")
        
    left_operand = float(match.group(1))
    operator = match.group(2)
    right_operand = float(match.group(3))
    
    if operator == '+':
        return left_operand + right_operand
    elif operator == '-':
        return left_operand - right_operand
    elif operator == '*':
        return left_operand * right_operand
    elif operator == '/':
        if right_operand == 0:
            raise CalculatorError("Division by zero is not allowed")
        return left_operand / right_operand
    
    raise CalculatorError("Unsupported operator")