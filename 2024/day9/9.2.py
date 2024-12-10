def read_input(path):
    try:
        with open(path) as fin:
            return fin.read().strip()
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return ""

def make_filesystem(diskmap):
    loc = [0] * len(diskmap)
    size = [0] * len(diskmap)
    blocks = []

    id = 0
    is_file = True
    for x in diskmap:
        x = int(x)
        if is_file:
            loc[id] = len(blocks)
            size[id] = x
            blocks += [id] * x
            id += 1
            is_file = False
        else:
            blocks += [None] * x
            is_file = True

    return blocks, loc, size

def move_files(filesystem, loc, size):
    big = 0
    while size[big] > 0:
        big += 1
    big -= 1

    for to_move in range(big, -1, -1):
        file_size = size[to_move]
        first_free = 0
        free_space = 0

        while first_free < loc[to_move] and free_space < file_size:
            first_free += free_space
            free_space = 0
            while filesystem[first_free] is not None:
                first_free += 1
            while first_free + free_space < len(filesystem) and filesystem[first_free + free_space] is None:
                free_space += 1

        if first_free >= loc[to_move]:
            continue

        for idx in range(first_free, first_free + file_size):
            filesystem[idx] = to_move
        for idx in range(loc[to_move], loc[to_move] + file_size):
            filesystem[idx] = None

    return filesystem

def checksum(filesystem):
    total_sum = 0
    for i, x in enumerate(filesystem):
        if x is not None:
            total_sum += i * x
    return total_sum

def main():
    path = "input.txt"
    diskmap = read_input(path)
    if not diskmap:
        return

    filesystem, loc, size = make_filesystem(diskmap)

    moved_filesystem = move_files(filesystem, loc, size)

    result_checksum = checksum(moved_filesystem)
    print(f"Filesystem checksum: {result_checksum}")

if __name__ == "__main__":
    main()
