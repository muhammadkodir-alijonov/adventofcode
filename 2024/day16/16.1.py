import heapq
from typing import List, Tuple

# Define directions: East, South, West, North
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def manhattan_distance(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    """Calculate Manhattan distance between two points."""
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

def find_position(maze: List[str], char: str) -> Tuple[int, int]:
    """Find the position of a character in the maze."""
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == char:
                return i, j
    raise ValueError(f"Character '{char}' not found in maze")

def is_valid_position(maze: List[str], row: int, col: int) -> bool:
    """Check if a position is valid (within bounds and not a wall)."""
    return (0 <= row < len(maze) and
            0 <= col < len(maze[0]) and
            maze[row][col] != '#')

def get_rotation_cost(old_direction: int, new_direction: int) -> int:
    """Calculate the cost of rotation."""
    rotation = (new_direction - old_direction) % 4
    if rotation in (1, 3):
        return 1000  # 90-degree rotation
    elif rotation == 2:
        return 2000  # 180-degree rotation
    return 0  # No rotation

def solve_reindeer_maze(maze: List[str]) -> int:
    """Solve the reindeer maze using A* algorithm."""
    rows, cols = len(maze), len(maze[0])
    start = find_position(maze, 'S')
    end = find_position(maze, 'E')

    # Priority queue: (f_score, g_score, row, col, direction)
    heap = [(0, 0, start[0], start[1], 0)]
    visited = set()

    while heap:
        _, g_score, row, col, direction = heapq.heappop(heap)

        if (row, col) == end:
            return g_score

        state = (row, col, direction)
        if state in visited:
            continue
        visited.add(state)

        for new_direction, (dr, dc) in enumerate(DIRECTIONS):
            new_row, new_col = row + dr, col + dc
            if is_valid_position(maze, new_row, new_col):
                rotation_cost = get_rotation_cost(direction, new_direction)
                new_g_score = g_score + 1 + rotation_cost  # Movement + rotation cost
                new_f_score = new_g_score + manhattan_distance((new_row, new_col), end)
                heapq.heappush(heap, (new_f_score, new_g_score, new_row, new_col, new_direction))

    return float('inf')  # No path found

def main():
    """Main function to read the maze and solve it."""
    with open('input.txt', 'r') as file:
        maze = [line.strip() for line in file]

    lowest_score = solve_reindeer_maze(maze)
    print(f"The lowest score a Reindeer could possibly get is: {lowest_score}")

if __name__ == "__main__":
    main()