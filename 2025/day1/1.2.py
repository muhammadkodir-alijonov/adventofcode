def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        return [line.strip() for line in content.splitlines()]

def calculate_l_r_point(data) -> int | None:
    pos = 50
    count1 = 0
    count2 = 0
    size = 100
    for nthe_data in data:
        if not nthe_data:
            continue
        d = nthe_data[0]
        nthe_data = int(nthe_data[1:])
        for _ in range(nthe_data):
            if d == 'L':
                pos = (pos - 1 + 100) % 100
            elif d == 'R':
                pos = (pos + 1) % 100
            if pos == 0:
                count2 += 1
        if pos == 0:
            count1 += 1
    print("count1: " + str(count1))
    print("count2: " + str(count2))
    return count2

if __name__ == '__main__':
    file_path = 'input.txt'
    data = read_file(file_path)
    ans = calculate_l_r_point(data)
    print("ans: " + str(ans))

# wong: 6392, 5321, 7235, 4074, 3649
# ans: 6412