import sys
import os

# Add the parent directory to sys.path to allow importing from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.calculator import calculate
from src.errors import CalculatorError

def main():
    if len(sys.argv) != 2:
        print("Usage: python src/main.py \"<expression>\"")
        sys.exit(1)

    expression = sys.argv[1]

    try:
        result = calculate(expression)
        print(result)
    except CalculatorError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

