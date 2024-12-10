def read_input(path):
    try:
        with open(path) as fin:
            map_ = fin.read().strip().split("\n")
            return [list(line) for line in map_]
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return []


def is_antinode(map_list, x1, y1, x2, y2):
    if map_list[x1][y1] == map_list[x2][y2]:  # Check if antennas have the same frequency
        dx, dy = abs(x2 - x1), abs(y2 - y1)
        # Check if one distance is twice the other
        if dx == 2 * dy or dy == 2 * dx:
            return True
    return False


def find_all_antennas(map_list):
    antennas = []
    for i in range(len(map_list)):
        for j in range(len(map_list[i])):
            if map_list[i][j].isalnum():  # Check for antennas (alphanumeric characters)
                antennas.append((i, j))
    return antennas


def main():
    path = "input.txt"  # Specify your input file path here
    map_ = read_input(path)
    if not map_:
        return

    antennas = find_all_antennas(map_)

    antinode_locations = set()

    for i in range(len(antennas)):
        for j in range(i + 1, len(antennas)):
            x1, y1 = antennas[i]
            x2, y2 = antennas[j]
            if is_antinode(map_, x1, y1, x2, y2):
                # Calculate midpoints for antinodes
                mid_x, mid_y = (x1 + x2) // 2, (y1 + y2) // 2
                # Check if the midpoint is a valid position inside the map
                if 0 <= mid_x < len(map_) and 0 <= mid_y < len(map_[mid_x]):
                    antinode_locations.add((mid_x, mid_y))

                # Also check the opposite direction for another antinode
                mid_x_opposite, mid_y_opposite = (x1 - x2) // 2, (y1 - y2) // 2
                if 0 <= mid_x_opposite < len(map_) and 0 <= mid_y_opposite < len(map_[mid_x_opposite]):
                    antinode_locations.add((mid_x_opposite, mid_y_opposite))

    print(f"Count of unique antinodes: {len(antinode_locations)}")


if __name__ == "__main__":
    main()
