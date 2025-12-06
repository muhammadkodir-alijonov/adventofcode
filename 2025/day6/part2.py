def read_file(file_path):
    """Step 1: Read the file and pad all lines to same length"""
    with open(file_path, 'r') as f:
        lines = [line. rstrip('\n') for line in f if line.strip()]
    
    # Make all lines the same length
    max_len = max(len(line) for line in lines)
    lines = [line.ljust(max_len) for line in lines]
    
    return lines


def separate_data_and_operators(lines):
    data_rows = lines[:-1]  # All rows except last
    op_row = lines[-1]       # Last row has operators
    return data_rows, op_row


def is_separator_column(data_rows, col):
    for row in data_rows:
        if row[col] != ' ':
            return False
    return True


def get_number_from_column(data_rows, col):
    digits = ''
    for row in data_rows:
        if row[col] != ' ':
            digits += row[col]
    
    if digits:
        return int(digits)
    return None


def find_operator(op_row, columns):
    for col in columns:
        char = op_row[col]. strip()
        if char in ['+', '*']:
            return char
    return None


def calculate(numbers, operator):
    if operator == '+':
        return sum(numbers)
    elif operator == '*':
        result = 1
        for n in numbers:
            result *= n
        return result
    return 0


def find_problems(data_rows, op_row):
    max_len = len(data_rows[0])
    col = max_len - 1
    problems = []
    
    while col >= 0:
        # Skip separator columns 
        while col >= 0 and is_separator_column(data_rows, col):
            col -= 1
        
        if col < 0:
            break
        
        # Collect columns for this problem
        problem_cols = []
        while col >= 0 and not is_separator_column(data_rows, col):
            problem_cols.append(col)
            col -= 1
        
        problems.append(problem_cols)
    
    return problems


def solve_problem(data_rows, op_row, columns):
    # Get all numbers
    numbers = []
    for col in columns:
        num = get_number_from_column(data_rows, col)
        if num is not None:
            numbers.append(num)
    
    # Get operator
    operator = find_operator(op_row, columns)
    
    # Calculate result
    result = calculate(numbers, operator)
    
    print(f"Numbers: {numbers}, Operator: {operator}, Result: {result}")
    return result


def solve_worksheet(file_path):
    # Step 1: Read file
    lines = read_file(file_path)
    
    # Step 2: Separate data and operators
    data_rows, op_row = separate_data_and_operators(lines)

    # Step 3: Find all problems
    problems = find_problems(data_rows, op_row)
    
    # Step 4: Solve each problem
    total = 0
    for problem_cols in problems:
        result = solve_problem(data_rows, op_row, problem_cols)
        print(f" Result: {result}")
        total += result
    
    return total


if __name__ == "__main__":
    answer = solve_worksheet('input.txt')
    print(f"\nGrand Total: {answer}")