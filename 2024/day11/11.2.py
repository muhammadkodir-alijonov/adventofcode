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
    stone_counts = {}

    for num in nums:
        stone_counts[num] = stone_counts.get(num, 0) + 1

    for _ in range(blinks):
        next_stones = {}
        for num, count in stone_counts.items():
            processed_stones = process_stone(num)
            for stone in processed_stones:
                next_stones[stone] = next_stones.get(stone, 0) + count

        stone_counts = next_stones

    total_stones = sum(stone_counts.values())
    return total_stones


def main():
    path = "input.txt"
    initial_stones = read_input(path)
    if not initial_stones:
        return
    print(f"Initial: {initial_stones}")
    total_stones = blinking_time(initial_stones, 75)
    print(f"Total stones: {total_stones}")


if __name__ == "__main__":
    main()
