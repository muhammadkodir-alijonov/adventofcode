def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]

    patterns = lines[0].split(', ')
    towels = lines[1:]
    return patterns, towels

def is_design_possible(patterns, towel):
    n = len(towel)
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for pattern in patterns:
            if towel[i - len(pattern):i] == pattern:
                print("i:", i, "pattern:", pattern)
                dp[i] += dp[i - len(pattern)]

    return dp[n]

def count_possible_designs(patterns, towels):
    total_combinations = 0
    for towel in towels:
        total_combinations += is_design_possible(patterns, towel)
    return total_combinations

def main():
    file_path = "input.txt"
    patterns, towels = read_input(file_path)
    total_designs = count_possible_designs(patterns, towels)
    print("patterns:", patterns)
    print("towels:", towels)
    print("res:", total_designs)


if __name__ == "__main__":
    main()
