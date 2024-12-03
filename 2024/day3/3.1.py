import re

def compute_sum_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()

    pattern = r"mul\((\d+),(\d+)\)"

    matches = re.findall(pattern, data)

    total_sum = 0
    for match in matches:
        x, y = map(int, match)
        total_sum += x * y

    return total_sum


file_path = "input.txt"

result = compute_sum_from_file(file_path)
print(f"The sum of all valid `mul(X,Y)` results is: {result}")
