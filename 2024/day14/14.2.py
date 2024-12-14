import re
from collections import defaultdict
import time

def parse_input(filename):
    robots = []
    with open(filename, 'r') as file:
        for line in file:
            match = re.match(r'p=<(-?\d+),(-?\d+)> v=<(-?\d+),(-?\d+)>', line.strip())
            if match:
                px, py, vx, vy = map(int, match.groups())
                robots.append((px, py, vx, vy))
    return robots

def update_positions(robots, width, height):
    new_robots = []
    for px, py, vx, vy in robots:
        new_x = (px + vx) % width
        new_y = (py + vy) % height
        new_robots.append((new_x, new_y, vx, vy))
    return new_robots

def is_christmas_tree(robots, width, height):
    positions = defaultdict(int)
    for px, py, _, _ in robots:
        positions[(px, py)] += 1

    tree_width = width // 3
    tree_height = height // 2
    tree_base = height - tree_height

    # Check tree shape
    for y in range(tree_base, height):
        tree_row_width = (y - tree_base + 1) * 2 - 1
        start_x = (width - tree_row_width) // 2
        for x in range(start_x, start_x + tree_row_width):
            if positions[(x, y)] == 0:
                return False

    # Check trunk
    trunk_width = max(1, tree_width // 5)
    trunk_start = (width - trunk_width) // 2
    for y in range(tree_base - 3, tree_base):
        for x in range(trunk_start, trunk_start + trunk_width):
            if positions[(x, y)] == 0:
                return False

    return True

def simulate_robots(robots, width, height, max_seconds):
    start_time = time.time()
    for second in range(1, max_seconds + 1):
        robots = update_positions(robots, width, height)
        if is_christmas_tree(robots, width, height):
            return second

        if second % 100000 == 0:
            elapsed_time = time.time() - start_time
            print(f"Simulated {second} seconds. Elapsed time: {elapsed_time:.2f} seconds")

    return -1

# Main execution
width, height = 101, 103
robots = parse_input('input.txt')
max_simulation_time = 10000000  # 10 million seconds

print(f"Starting simulation with {len(robots)} robots for up to {max_simulation_time} seconds...")
result = simulate_robots(robots, width, height, max_simulation_time)

if result != -1:
    print(f"The robots display the Easter egg after {result} seconds.")
else:
    print("The Easter egg pattern was not found within the given time limit.")