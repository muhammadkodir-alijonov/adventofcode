def read_input(path):
    try:
        with open(path) as file:
            return [list(map(int, line.strip())) for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return []

def search_is_valid_trailhead(grid, i, j):
    row = len(grid)
    col = len(grid[0])

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    visited = set()
    queue = [(i, j, 0)]

    reachable_nines = set()

    while queue:
        cur_i, cur_j, cur_h = queue[0]
        queue = queue[1:]

        if (cur_i, cur_j) in visited:
            continue
        visited.add((cur_i, cur_j))

        if grid[cur_i][cur_j] == 9:
            reachable_nines.add((cur_i, cur_j))
            continue

        for di, dj in directions:
            next_i, next_j = cur_i + di, cur_j + dj
            if 0 <= next_i < row and 0 <= next_j < col:
                next_h = grid[next_i][next_j]
                if next_h == cur_h + 1:
                    queue.append((next_i, next_j, next_h))

    return len(reachable_nines)


def main():
    path = "input.txt"
    grid = read_input(path)
    if not grid:
        return

    row = len(grid)
    col = len(grid[0])
    total_score = 0
    print(grid)
    print(row)
    print(col)

    for i in range(row):
        for j in range(col):
            if grid[i][j] == 0:
                total_score += search_is_valid_trailhead(grid, i, j)

    print("Barcha boshlang‘ich nuqtalar umumiy bahosi:", total_score)


if __name__ == "__main__":
    main()
