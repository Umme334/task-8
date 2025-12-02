# Tasks: Simple Calculator

**Branch**: `001-basic-calculator` | **Spec**: [Link](spec.md) | **Plan**: [Link](plan.md)

## Implementation Strategy
- **MVP Approach**: Start with a core logic library capable of parsing and evaluating simple expressions, then wrap it in a CLI handler.
- **Incremental Delivery**: Implement addition first to validate the pipeline, then add other operations.
- **Testing**: All core logic tasks will include unit tests (TDD).
- **Parallelism**: Core logic implementation is sequential per operation, but error handling and CLI integration can potentially proceed in parallel once the base structure is in place.

## Phase 1: Setup
*Goal: Initialize project structure and testing environment.*

- [x] T001 Create project directory structure (`src/`, `tests/unit/`, `tests/integration/`) per plan
- [x] T002 Create empty `__init__.py` files in `src/` and `tests/` to make them packages
- [x] T003 Create `requirements.txt` (or just document `pytest` dependency)
- [x] T004 Create `tests/conftest.py` for shared test fixtures

## Phase 2: Foundation (Core Logic Skeleton)
*Goal: Establish the `Calculator` class/module and custom errors.*

- [x] T005 Define custom exception classes in `src/errors.py` (e.g., `CalculatorError`)
- [x] T006 Create `src/calculator.py` with a stub `calculate(expression: str)` function
- [x] T007 Create `tests/unit/test_calculator.py` with a simple import test to verify setup

## Phase 3: User Story 1 (Basic Addition)
*Goal: Implement parsing and evaluation for single-operator addition.*

- [x] T008 [US1] Create unit test for addition (e.g., "2 + 3" -> 5.0) in `tests/unit/test_calculator.py`
- [x] T009 [US1] Implement regex parser in `src/calculator.py` to split operands and operator
- [x] T010 [US1] Implement addition logic in `src/calculator.py`
- [x] T011 [US1] Verify addition tests pass

## Phase 4: User Story 2 (Basic Subtraction)
*Goal: Extend logic to support subtraction.*

- [x] T012 [US2] Create unit test for subtraction (e.g., "5 - 2" -> 3.0) in `tests/unit/test_calculator.py`
- [x] T013 [US2] Extend parser/evaluator in `src/calculator.py` to handle subtraction
- [x] T014 [US2] Verify subtraction tests pass

## Phase 5: User Story 3 (Basic Multiplication)
*Goal: Extend logic to support multiplication.*

- [x] T015 [US3] Create unit test for multiplication (e.g., "4 * 5" -> 20.0) in `tests/unit/test_calculator.py`
- [x] T016 [US3] Extend parser/evaluator in `src/calculator.py` to handle multiplication
- [x] T017 [US3] Verify multiplication tests pass

## Phase 6: User Story 4 & 5 (Division & Zero Handling)
*Goal: Support division and ensure division by zero is handled safely.*

- [x] T018 [US4] Create unit test for valid division (e.g., "10 / 2" -> 5.0) in `tests/unit/test_calculator.py`
- [x] T019 [US5] Create unit test for division by zero (e.g., "10 / 0") expecting explicit error
- [x] T020 [US4] Extend evaluator in `src/calculator.py` to handle division
- [x] T021 [US5] Implement division-by-zero check in `src/calculator.py` to raise specific error
- [x] T022 [US4] [US5] Verify all division tests pass

## Phase 7: User Story 6 (Invalid Input & CLI)
*Goal: Handle invalid inputs robustly and expose functionality via CLI.*

- [x] T023 [US6] Create unit tests for invalid inputs (multiple ops, non-numbers) in `tests/unit/test_calculator.py`
- [x] T024 [US6] Implement input validation in `src/calculator.py` to enforce single-op rule (FR-008)
- [x] T025 [US6] Create `src/main.py` to parse command line args and call `calculate()`
- [x] T026 [US6] Implement error catching in `src/main.py` to print user-friendly error messages
- [x] T027 [US6] Create integration test `tests/integration/test_cli.py` running `main.py` as a subprocess against success and error cases

## Phase 8: Polish
*Goal: Final code quality checks and documentation.*

- [x] T028 Run full test suite (`pytest`) and ensure 100% pass rate
- [x] T029 Add docstrings to `src/calculator.py` functions
- [x] T030 Verify `quickstart.md` instructions work as expected

## Dependencies

1. **Setup** (T001-T004) must be completed first.
2. **Foundation** (T005-T007) blocks all User Stories.
3. **US1** (T008-T011) establishes the core parsing pattern used by subsequent stories.
4. **US2-US5** (T012-T022) can be implemented sequentially or in parallel by different developers if the parser logic is modular enough (though here it's simple enough to do sequentially).
5. **US6/CLI** (T023-T027) depends on the core logic being stable but can be started in draft form earlier.

## Parallel Execution Examples

- **Example 1**: One developer works on **US2 (Subtraction)** (T012-T014) while another works on **US3 (Multiplication)** (T015-T017) once US1 is done.
- **Example 2**: **Integration Tests** (T027) can be written in parallel with **CLI Implementation** (T025-T026).
