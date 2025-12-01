def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
        return [line.strip() for line in content.splitlines()]


def calculate_l_r_point(data) -> int | None:
    start_point = 50
    count = 0
    max_ = 99
    min_ = 0
    size = max_ - min_ + 1
    for nthe_data in data:
        if not nthe_data:
            continue
        if nthe_data.startswith('L'):
            step = int(nthe_data[1:])
            start_point -= step
            start_point = start_point % size
        elif nthe_data.startswith('R'):
            step = int(nthe_data[1:])
            start_point += step
            start_point = start_point % size
        if start_point == 0:
            count += 1
    return count


if __name__ == '__main__':
    file_path = 'input.txt'
    data = read_file(file_path)
    ans = calculate_l_r_point(data)
    print(ans)
# ans = 1078