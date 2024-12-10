from collections import deque

def read_input(path):
    try:
        with open(path) as file:
            return [list(map(int, line.strip())) for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return []

def bfs_trailhead_rating(grid, i, j):
    row = len(grid)
    col = len(grid[0])

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = set()
    queue = deque([(i, j)])

    trail_count = 0

    while queue:
        cur_i, cur_j = queue.popleft()

        if grid[cur_i][cur_j] == 9:
            trail_count += 1

        for di, dj in directions:
            next_i, next_j = cur_i + di, cur_j + dj

            if 0 <= next_i < row and 0 <= next_j < col:
                if grid[next_i][next_j] == grid[cur_i][cur_j] + 1:
                    visited.add((next_i, next_j))
                    queue.append((next_i, next_j))

    return trail_count

def main():
    path = "input.txt"
    grid = read_input(path)
    if not grid:
        return

    row = len(grid)
    col = len(grid[0])
    total_rating = 0

    for i in range(row):
        for j in range(col):
            if grid[i][j] == 0:
                total_rating += bfs_trailhead_rating(grid, i, j)

    print("Total Rating of All Trailheads:", total_rating)

if __name__ == "__main__":
    main()
