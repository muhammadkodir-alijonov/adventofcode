def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        return [line.strip() for line in content.splitlines()]

def calculate_l_r_point(data) -> int | None:
    start_point = 50
    count = 0
    size = 100
    for nthe_data in data:
        if not nthe_data:
            continue
        prev_point = start_point
        if nthe_data.startswith('L'):
            step = int(nthe_data[1:])
            start_point = (start_point - step) % size
            full_rotations = step // size
            count += full_rotations
            for i in range(1, step % size + 1):
                pos = (prev_point - i) % size
                if pos == 0:
                    count += 1
        elif nthe_data.startswith('R'):
            step = int(nthe_data[1:])
            start_point = (start_point + step) % size
            full_rotations = step // size
            count += full_rotations
            for i in range(1, step % size + 1):
                pos = (prev_point + i) % size
                if pos == 0:
                    count += 1
    return count

if __name__ == '__main__':
    file_path = 'input.txt'
    data = read_file(file_path)
    ans = calculate_l_r_point(data)
    print("ans: " + str(ans))

# wong: 6392, 5321, 7235, 4074, 3649
# ans: 6412