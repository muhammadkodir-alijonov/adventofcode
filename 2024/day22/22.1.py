def mix_and_prune(secret_number, factor):
    mixed_value = secret_number ^ factor
    return mixed_value % 16777216


def generate_next_secret_number(secret_number):
    secret_number = mix_and_prune(secret_number, secret_number * 64)

    secret_number = mix_and_prune(secret_number, secret_number // 32)

    secret_number = mix_and_prune(secret_number, secret_number * 2048)

    return secret_number


def generate_secret_number_sequence(start, iterations):
    secret_number = start
    for _ in range(iterations):
        secret_number = generate_next_secret_number(secret_number)
    return secret_number


def read_initial_numbers(file_path):
    with open(file_path, "r") as file:
        return [int(line.split()[-1]) for line in file]


def calculate_final_sum(initial_numbers, iterations):
    total_sum = 0
    for num in initial_numbers:
        final_number = generate_secret_number_sequence(num, iterations)
        total_sum += final_number
        print(f"2000th secret number for {num}: {final_number}")
    return total_sum


if __name__ == "__main__":
    input_file = "input.txt"
    iterations = 2000

    initial_numbers = read_initial_numbers(input_file)

    result = calculate_final_sum(initial_numbers, iterations)

    print("Sum of 2000th secret numbers:", result)
