# Instructions Calculator

Python CLI tool that reads mathematical instructions from a text file and executes them sequentially.

## How It Works

The input file contains one instruction per line. Each instruction represents a mathematical operation.

The last line must always be:

```text
apply <number>
```

The `apply` instruction defines the **initial value** (starting number). The program first reads this value and then executes every previous instruction from top to bottom in the order they appear.

For example:

```text
add 2
multiply 3
apply 3
```

Calculation:

```text
Start: 3
3 + 2 = 5
5 × 3 = 15
```

Output:

```text
15
```

## Prerequisites

- Python 3.8 or later

## Example Input (`instructions.txt`)

```text
add 2
multiply 3
apply 3
```

## Running the Program

Clone the repository:

```bash
git clone https://github.com/daria-pamp/calculator_pampukha.git
cd calculator_pampukha
```

Run the calculator:

```bash
python calculator.py instructions.txt
```

## Running Unit Tests

Run the complete test suite:

```bash
python -m unittest test_calculator.py
```

The tests cover:

- arithmetic operations
- whitespace handling
- floating-point numbers
- invalid instructions
- invalid number formats
- empty files
- missing files
- division by zero
- other edge cases

## Design Decisions

### Sequential Execution

Operations are executed exactly in the order they appear in the file. Standard mathematical operator precedence is intentionally ignored because this behavior is required by the specification.

### Error Handling

The application validates common error conditions, including:

- missing input files
- empty instruction files
- unsupported operations
- invalid numeric values
- malformed instructions
- division by zero

### Extensibility

Mathematical operations are implemented using Python's built-in `operator` module and stored in a mapping (dictionary). Adding a new operation only requires defining the corresponding function and registering it in the mapping.