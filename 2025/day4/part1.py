def read_matrix(file_path):
    with open(file_path, 'r') as f:
        return [list(line.strip()) for line in f if line.strip()]

def forklifts_bounded(matrix, i, j):
    pass

"""
..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.
"""
def calculate_forklifts(matrix):
    res = 0
    n = len(matrix)
    m = len(matrix[0]) if n > 0 else 0
    # up, down, left, right, diogonal up-left, diagonal up-right, diagonal down-left, diagonal down-right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '@':
                count = 0
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] == '@':
                        count += 1
                if count < 4:
                    res += 1
    return res



if __name__ == "__main__":
    matrix = read_matrix('input.txt')
    result = calculate_forklifts(matrix)
    print("Result: " + str(result))