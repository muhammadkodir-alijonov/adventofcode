from collections import deque

def read_input(path):
    try:
        with open(path) as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return []

def flood_fill(row, col, garden, visited):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    plant_type = garden[row][col]
    queue = deque([(row, col)])
    visited[row][col] = True
    area = 0
    perimeter = 0

    while queue:
        cur_row, cur_col = queue.popleft()
        area += 1
        for dr, dc in directions:
            nr, nc = cur_row + dr, cur_col + dc
            if nr < 0 or nr >= len(garden) or nc < 0 or nc >= len(garden[0]) or garden[nr][nc] != plant_type:
                perimeter += 1
            elif not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc))

    return area, perimeter

def calculate_total_price(garden):
    rows = len(garden)
    cols = len(garden[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    total_price = 0

    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                area, perimeter = flood_fill(i, j, garden, visited)
                total_price += area * perimeter

    return total_price

def main():
    path = "input.txt"
    garden = read_input(path)
    if not garden:
        return
    print(garden)
    total_price = calculate_total_price(garden)
    print(f"Total price of fencing all regions: {total_price}")

if __name__ == "__main__":
    main()

# C C A C C
# C C A C C
# A A A C C
# C C A A A
# C C C C C

