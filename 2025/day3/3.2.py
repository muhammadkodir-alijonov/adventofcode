def read_ranges(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def largest_12_digit_number(s):
    k = len(s) - 12
    stack = []
    for digit in s:
        while k and stack and stack[-1] < digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    while k:
        stack.pop()
        k -= 1
    return ''.join(stack)

if __name__ == "__main__":
    tokens = read_ranges('input.txt')
    summ = 0
    for line in tokens:
        summ += int(largest_12_digit_number(line))
    print(summ)