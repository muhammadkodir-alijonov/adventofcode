from collections import deque
def read_input(file_path):
    byte_positions = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(int, line.strip().split(','))
            byte_positions.append((x, y))
    return byte_positions


def simulate_memory_space(byte_positions, grid_size=71, max_bytes=1024):
    memory_space = [['.' for _ in range(grid_size)] for _ in range(grid_size)]

    for i, (x, y) in enumerate(byte_positions):
        print(i)
        if i >= max_bytes:
            break
        memory_space[y][x] = '#'
    return memory_space


def bfs_short_path(memory_space, start, goal):
    grid_size = len(memory_space)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(start, 0)])  # (Koordinata, qadamlar soni)
    visited = set()

    while queue:
        (x, y), steps = queue.popleft()

        if (x, y) == goal:
            return steps
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid_size and 0 <= ny < grid_size:
                if memory_space[ny][nx] == '.' and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), steps + 1))

    return -1
def main():
    file_path = "input.txt"
    byte_positions = read_input(file_path)
    memory_space = simulate_memory_space(byte_positions, grid_size=71, max_bytes=1024)

    start = (0, 0)
    goal = (70, 70)
    steps = bfs_short_path(memory_space, start, goal)
    print(len(memory_space))
    print(memory_space)

    print(len(byte_positions))
    print(byte_positions)
    print(f"Minimal qadamlar soni: {steps}")


if __name__ == "__main__":
    main()
