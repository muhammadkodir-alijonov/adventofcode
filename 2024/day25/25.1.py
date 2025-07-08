def read_locks_and_keys(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    grids = []
    current_grid = []

    for line in lines:
        stripped = line.strip()
        if stripped:
            current_grid.append(stripped)
        else:
            if current_grid:
                grids.append(current_grid)
                current_grid = []
    if current_grid:
        grids.append(current_grid)

    locks = []
    keys = []

    for grid in grids:
        if all(c == '#' for c in grid[0]):
            locks.append(grid)
        elif all(c == '#' for c in grid[-1]):
            keys.append(grid)

    return locks, keys

def get_heights(grid):
    heights = []
    for j in range(len(grid[0])):
        height = 0
        for i in range(len(grid)):
            if grid[i][j] == '#':
                height += 1
        heights.append(height)
    return heights

def main():
    path = './day25/input.txt'
    locks, keys = read_locks_and_keys(path)

    lock_heights = []
    for lock in locks:
        lock_heights.append(get_heights(lock))

    key_heights = []
    for key in keys:
        key_heights.append(get_heights(key))
    
    ans = 0
    for lock_height in lock_heights:
        for key_height in key_heights:
            flag = True
            for i in range(len(lock_height)):
                if lock_height[i] + key_height[i] > len(locks[0]):
                    flag = False
                    break
            if flag:
                ans += 1

    print(f"ANS: {ans}")

if __name__ == "__main__":
    main()