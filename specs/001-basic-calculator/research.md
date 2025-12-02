# Phase 0: Research & Decisions

**Feature**: Simple Calculator (001-basic-calculator)
**Date**: 2025-12-02

## Technical Decisions

### 1. Programming Language
- **Decision**: Python 3.10+
- **Rationale**:
  - Python is highly readable and concise ("Simplicity First").
  - Excellent standard library support for mathematics.
  - Cross-platform compatibility (Windows, Linux, macOS).
  - No compilation step required, enabling fast feedback loops.
- **Alternatives Considered**:
  - *Node.js*: Good, but requires `package.json` setup and `node_modules`. Python is often cleaner for simple scripts/CLIs.
  - *Go*: Good for CLIs, but more boilerplate than Python for string parsing and basic math.
  - *C/C++*: Too complex for the scope; violates "Simplicity First" due to build management.

### 2. Testing Framework
- **Decision**: `pytest`
- **Rationale**:
  - Industry standard for Python testing.
  - Supports TDD effectively (Red-Green-Refactor).
  - Simple syntax (no boilerplate classes required).
- **Alternatives Considered**:
  - *unittest*: Built-in, but more verbose.

### 3. Implementation Approach
- **Decision**: Recursive Descent Parser (Simplified) or Regex-based Splitter
- **Rationale**:
  - Since the requirement "FR-008" enforces *single operation per input*, a full parser (Shunting-yard) is overkill.
  - A simple regex split (e.g., `(\d+)\s*([\+\-\*\/])\s*(\d+)`) is sufficient, robust, and extremely simple.
  - Meets "Simplicity First" and "Mathematical Correctness".
- **Alternatives Considered**:
  - *`eval()`*: Rejected due to security risks (arbitrary code execution) even if "Simplicity First" suggests it. Clean Architecture demands better control.
  - *Full Parser*: Rejected as over-engineering for the restricted scope.

### 4. Project Structure
- **Decision**: Single project layout (`src/` + `tests/`)
- **Rationale**:
  - Keeps concerns separated (Clean Architecture).
  - Easy to navigate.
