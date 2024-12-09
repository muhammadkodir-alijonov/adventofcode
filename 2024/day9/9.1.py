def read_input(path):
    try:
        with open(path) as fin:
            map_ = fin.read().strip()
            return map_
        
        
        
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return ""
    
    
def make_up_amphipod(map_):
    amphipod = []
    is_file = True
    file_id = 0

    for length in map_:
        length = int(length)
        if is_file:
            amphipod.extend([str(file_id)] * length)
            file_id += 1
        else:
            amphipod.extend(['.'] * length)
        is_file = not is_file

    return amphipod

def filesystem_make_up(amphipod):
    left = 0
    right = len(amphipod) - 1

    while left < right:
        if amphipod[left] == '.' and amphipod[right].isnumeric():
            amphipod[left], amphipod[right] = amphipod[right], '.'
            left += 1
            right -= 1
        elif amphipod[left] != '.':
            left += 1
        elif amphipod[right] == '.':
            right -= 1

    return amphipod

def filesystem_checksum(amphipod):
    total_sum = 0
    for i, block in enumerate(amphipod):
        if block.isnumeric():
            total_sum += i * int(block)
    return total_sum

def main():
    path = "input.txt"
    map_ = read_input(path)
    if not map_:
        return

    amphipod = make_up_amphipod(map_)
    print("Initial amphipod:", ''.join(amphipod))

    compacted_amphipod = filesystem_make_up(amphipod)
    print("Compacted amphipod:", ''.join(compacted_amphipod))

    checksum = filesystem_checksum(compacted_amphipod)
    print("Filesystem checksum:", checksum)

if __name__ == "__main__":
    main()
