# Data Model: Simple Calculator

## Key Entities

### 1. Expression
Represents the raw user input that needs to be processed.

- **Fields**:
  - `raw_text` (string): The input string provided by the user.
  - `clean_text` (string): The input after whitespace trimming.

- **Validation Rules**:
  - Must not be empty.
  - Must contain exactly one valid operator (`+`, `-`, `*`, `/`).
  - Must contain exactly two valid numeric operands.

### 2. Calculation
Represents a parsed and valid mathematical operation ready to be executed.

- **Fields**:
  - `left_operand` (float): The first number.
  - `operator` (enum): The operation to perform (ADD, SUBTRACT, MULTIPLY, DIVIDE).
  - `right_operand` (float): The second number.

- **Logic**:
  - Division by zero check happens during execution of the Calculation.

### 3. CalculationResult
Represents the outcome of a Calculation.

- **Fields**:
  - `value` (float, optional): The numeric result if successful.
  - `error` (string, optional): Error message if failed (e.g., "Division by zero").
  - `is_success` (boolean): True if calculation was valid and computed.

## State Transitions

1.  **Input** (`string`) → **Parser** → **Calculation** (or Error)
2.  **Calculation** → **Evaluator** → **CalculationResult**
