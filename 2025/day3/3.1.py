def read_ranges(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]
    
def calculate_max_joltage(tokens):
    total_joltage = 0
    for token in tokens:
        max_joltage = 0
        length = len(token)
        for i in range(length):
            for j in range(i + 1, length):
                joltage = int(token[i] + token[j])
                if joltage > max_joltage:
                    max_joltage = joltage
        total_joltage += max_joltage
        print(f"Max joltage for bank {token}: {max_joltage}")
    return total_joltage

if __name__ == "__main__":
    tokens = read_ranges('input.txt')
    total_joltage = calculate_max_joltage(tokens)
    print(total_joltage)