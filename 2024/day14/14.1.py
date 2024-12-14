import re

def read_input(path):
    try:
        with open(path) as file:
            data = file.read()
            pattern = r"p=(\d+),(\d+) v=([+-]?\d+),([+-]?\d+)"
            matches = re.findall(pattern, data)
            robots = []
            for match in matches:
                x, y, vx, vy = map(int, match)
                robots.append(((x, y), (vx, vy)))
            return robots
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return []

def simulate_robots(robots, width, height, seconds):
    updated_positions = []
    for (x, y), (vx, vy) in robots:
        new_x = (x + vx * seconds) % width
        new_y = (y + vy * seconds) % height
        updated_positions.append((new_x, new_y))
    return updated_positions

def calculate_safety_factor(positions, width, height):
    half_width = width // 2
    half_height = height // 2

    quadrants = [0, 0, 0, 0]
    for x, y in positions:
        if x == half_width or y == half_height:
            continue
        if x < half_width and y < half_height:
            quadrants[0] += 1
        elif x >= half_width and y < half_height:
            quadrants[1] += 1
        elif x < half_width and y >= half_height:
            quadrants[2] += 1
        else:
            quadrants[3] += 1

    safety_factor = 1
    for count in quadrants:
        safety_factor *= count

    return safety_factor

def main():
    path = "input.txt"
    width, height = 101, 103
    seconds = 100
    robots = read_input(path)
    if not robots:
        return

    positions = simulate_robots(robots, width, height, seconds)

    safety_factor = calculate_safety_factor(positions, width, height)

    print(f"Safety factor after {seconds} seconds: {safety_factor}")

if __name__ == "__main__":
    main()
