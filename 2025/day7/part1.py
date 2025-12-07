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

    split_count = 0
    visited = set()

    def dfs(i, j):
        nonlocal split_count
        if i >= n or j < 0 or j >= m:
            return
        if (i, j) in visited:
            return
        visited.add((i, j))
        if matrix[i][j] == '.':
            dfs(i + 1, j)
        elif matrix[i][j] == '^':
            split_count += 1
            dfs(i + 1, j - 1)
            dfs(i + 1, j + 1)

    dfs(start_i + 1, start_j)
    return split_count

if __name__ == "__main__":
    matrix = read_matrix('input.txt')
    ans = print_juniper(matrix)
    print(f"Total splits: {ans}")