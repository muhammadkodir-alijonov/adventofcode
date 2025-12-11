def read_data(file_path):
    with open(file_path, 'r') as file:
        return [list(map(int, line.strip())) for line in file.readlines()]

if __name__ == "__main__":
    data = read_data('2025/day11/input.txt')
    for row in data:
        print(row)