def read_matrix(file_path):
    with open(file_path, 'r') as f:
        return [list(line.strip()) for line in f if line.strip()]

def forklifts_bounded(matrix, i, j):
    pass

"""
Once a roll of paper can be accessed by a forklift, it can be removed. Once a roll of paper is removed, the forklifts might be able to access more rolls of paper, which they might also be able to remove. How many total rolls of paper could the Elves remove if they keep repeating this process?

Starting with the same example as above, here is one way you could remove as many rolls of paper as possible, using highlighted @ to indicate that a roll of paper is about to be removed, and using x to indicate that a roll of paper was just removed:
"""
def calculate_forklifts(matrix):
    res = 0
    n = len(matrix)
    m = len(matrix[0]) if n > 0 else 0
    # up, down, left, right, diogonal up-left, diagonal up-right, diagonal down-left, diagonal down-right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]
    while True:
        to_remove = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '@':
                    count = 0
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] == '@':
                            count += 1
                    if count < 4:
                        to_remove.append((i, j))
        if not to_remove:
            break
        for i, j in to_remove:
            matrix[i][j] = 'x'
        res += len(to_remove)
    return res


if __name__ == "__main__":
    matrix = read_matrix('input.txt')
    result = calculate_forklifts(matrix)
    print("Result: " + str(result))