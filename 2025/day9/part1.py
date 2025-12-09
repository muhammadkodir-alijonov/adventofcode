def read_data(file_path):
    with open(file_path, 'r') as f:
        return [list(map(int, line.strip().split(','))) for line in f if line.strip()]

def calculate_area(data) -> int:
    area = 0
    n = len(data)
    for i in range(n - 1):
        for j in range(i + 1, n):
            # +1 qo'shamiz chunki kataklar sonini sanayapmiz
            rect_area = (abs(data[i][0] - data[j][0]) + 1) * (abs(data[i][1] - data[j][1]) + 1)
            if rect_area > area:
                area = rect_area
                best_pair = (data[i], data[j])
    return area

if __name__ == "__main__":
    data = read_data('input.txt')
    area = calculate_area(data)
    print('ans: ' + str(area))