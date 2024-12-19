def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]

    patterns = lines[0].split(', ')
    towels = lines[1:]
    return patterns, towels

def is_design_possible(patterns, towel):
    n = len(towel)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for pattern in patterns:
            if towel[i - len(pattern):i] == pattern:
                dp[i] = dp[i] or dp[i - len(pattern)]
    return dp[n]

def count_possible_designs(patterns, towels):
    possible_count = 0
    for towel in towels:
        if is_design_possible(patterns, towel):
            possible_count += 1
    return possible_count

def main():
    file_path = "input.txt"
    patterns, towels = read_input(file_path)
    total_designs = count_possible_designs(patterns, towels)
    print("patterns:", patterns)
    print("towels:", towels)
    print("res:", total_designs)


if __name__ == "__main__":
    main()
