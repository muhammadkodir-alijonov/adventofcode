def read_input(path):
    try:
        with open(path) as file:
            numbers = []
            for line in file:
                for num in line.strip().split():
                    numbers.append(int(num))
            return numbers
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return []

def process_stone(num):
    if num == 0:
        return [1]
    elif len(str(num)) % 2 == 0:
        mid = len(str(num)) // 2
        left = int(str(num)[:mid])
        right = int(str(num)[mid:])
        return [left, right]
    else:
        return [num * 2024]

def blinking_time(nums, blinks):
    current_stones = nums
    for _ in range(blinks):
        next_stones = []
        for num in current_stones:
            next_stones += process_stone(num)
        current_stones = next_stones
    return len(current_stones)

def main():
    path = "input.txt"
    initial_stones = read_input(path)
    if not initial_stones:
        return
    print(f"Initial stones: {initial_stones}")
    total_stones = blinking_time(initial_stones, 25)
    print(f"Total stones after 25 blinks: {total_stones}")

if __name__ == "__main__":
    main()
