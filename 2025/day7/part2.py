from functools import lru_cache

def read_matrix(file_path):
    with open(file_path, 'r') as f:
        return [list(line.strip()) for line in f if line.strip()]
    
def print_juniper(matrix) -> int:
    n = len(matrix)
    m = len(matrix[0]) if n > 0 else 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'S':
                start_i, start_j = i, j

    @lru_cache(maxsize=None)
    def dfs(i, j):
        if i >= n or j < 0 or j >= m:
            return 1
        if matrix[i][j] == '.':
            return dfs(i + 1, j)
        elif matrix[i][j] == '^':
            return dfs(i + 1, j - 1) + dfs(i + 1, j + 1)
        else:
            return 0

    return dfs(start_i + 1, start_j)

if __name__ == "__main__":
    matrix = read_matrix('input.txt')
    ans = print_juniper(matrix)
    print(f"Total timelines: {ans}")