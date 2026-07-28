import sys
import operator

# Mapping instruction keywords to standard Python math operators.
# Using a dict keeps things clean and makes it super easy to add new operations later.
OPERATIONS = {
    'add': operator.add,
    'subtract': operator.sub,
    'multiply': operator.mul,
    'divide': operator.truediv
}

def calculate(lines: list[str]) -> float:
    # Strip whitespace from each line and skip any empty ones
    cleaned_lines = [line.strip() for line in lines if line.strip()]
    
    if not cleaned_lines:
        raise ValueError("Instruction file is empty.")

    # The last line should always be 'apply <number>'. 
    # Since this defines our starting value, we grab it first before processing the rest.
    last_line = cleaned_lines[-1]
    last_parts = last_line.split()

    if len(last_parts) != 2 or last_parts[0].lower() != 'apply':
        raise ValueError("The final instruction must be in the format 'apply <number>'.")

    try:
        current_value = float(last_parts[1])
    except ValueError:
        raise ValueError(f"Invalid initial value in apply instruction: '{last_parts[1]}'")

    # Process all previous instructions sequentially from top to bottom
    for line in cleaned_lines[:-1]:
        parts = line.split()
        if len(parts) != 2:
            raise ValueError(f"Invalid instruction format: '{line}'")

        op_name, val_str = parts[0].lower(), parts[1]

        if op_name not in OPERATIONS:
            raise ValueError(f"Unsupported operation: '{op_name}'")

        try:
            val = float(val_str)
        except ValueError:
            raise ValueError(f"Invalid numeric value in line: '{line}'")

        # Handle division by zero explicitly so it fails gracefully
        if op_name == 'divide' and val == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")

        # Execute the calculation
        current_value = OPERATIONS[op_name](current_value, val)

    return current_value


def main():
    # Basic CLI handling to check if file argument is passed
    if len(sys.argv) < 2:
        print("Usage: python calculator.py <path_to_instruction_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        result = calculate(lines)
        
        # Format whole numbers nicely (e.g. 15.0 -> 15), but keep actual decimals
        if result.is_integer():
            print(int(result))
        else:
            print(result)

    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()