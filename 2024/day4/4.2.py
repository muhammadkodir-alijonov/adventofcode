import re


def process_memory(memory):
    mul_enabled = True
    total_sum = 0

    mul_pattern = r"mul\((\d+),(\d+)\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    tokens = re.finditer(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", memory)

    for token in tokens:
        match = token.group(0)

        if match == "do()":
            mul_enabled = True
        elif match == "don't()":
            mul_enabled = False
        elif match.startswith("mul("):
            nums = re.match(mul_pattern, match)
            if nums and mul_enabled:
                x, y = map(int, nums.groups())
                total_sum += x * y

    return total_sum


with open('input.txt', 'r') as file:
    memory = file.read()

result = process_memory(memory)
print(result)
