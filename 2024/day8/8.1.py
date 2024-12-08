def read_input(path):
    try:
        with open(path) as fin:
            map_ = fin.read().strip().split("\n")
            return [list(line) for line in map_]
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return []

def in_bounds(x, y, map_list):
    return 0 <= x < len(map_list) and 0 <= y < len(map_list[x])

def get_antinodes(x1, y1, x2, y2, map_list):
    # Antenna joylarini tekshirish va antinode hisoblash
    ax, ay = x1, y1
    bx, by = x2, y2

    cx, cy = ax - (bx - ax), ay - (by - ay)
    dx, dy = bx + (bx - ax), by + (by - ay)

    # Antinode bo'lishi mumkin bo'lgan nuqtalarni qaytarish
    antinodes = []
    if in_bounds(cx, cy, map_list):
        antinodes.append((cx, cy))
    if in_bounds(dx, dy, map_list):
        antinodes.append((dx, dy))
    return antinodes

def find_all_antennas(map_list):
    antennas = []
    for i in range(len(map_list)):
        for j in range(len(map_list[i])):
            if map_list[i][j] != '.':
                antennas.append((i, j))
    return antennas

def main():
    path = "input.txt"
    map_ = read_input(path)
    if not map_:
        return

    antennas = find_all_antennas(map_)
    antinode_locations = set()

    for i in range(len(antennas)):
        for j in range(i + 1, len(antennas)):
            x1, y1 = antennas[i]
            x2, y2 = antennas[j]
            if map_[x1][y1] == map_[x2][y2]:
                antinodes = get_antinodes(x1, y1, x2, y2, map_)
                for antinode in antinodes:
                    mid_x, mid_y = antinode
                    if in_bounds(mid_x, mid_y, map_):
                        antinode_locations.add((mid_x, mid_y))

    print(f"Count of unique antinodes: {len(antinode_locations)}")

if __name__ == "__main__":
    main()
