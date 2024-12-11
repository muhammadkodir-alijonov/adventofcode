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


def find_free_spans(amphipod):
    spans = []
    start = None
    for i, block in enumerate(amphipod):
        if block == '.':
            if start is None:
                start = i
        else:
            if start is not None:
                spans.append((start, i - 1))
                start = None
    if start is not None:
        spans.append((start, len(amphipod) - 1))
    return spans


def move_files_whole(amphipod):
    file_ids = sorted({int(block) for block in amphipod if block.isnumeric()}, reverse=True)
    for file_id in file_ids:
        file_indices = [i for i, block in enumerate(amphipod) if block == str(file_id)]
        file_length = len(file_indices)

        # Find all free spans
        free_spans = find_free_spans(amphipod)

        # Look for the leftmost suitable span that can fit the current file
        best_span = None
        for start, end in free_spans:
            if end - start + 1 >= file_length:
                best_span = (start, start + file_length - 1)
                break

        if best_span:
            start, end = best_span
            # Move the file to the span
            for i in range(start, end + 1):
                amphipod[i] = str(file_id)
            # Clear the original file positions
            for idx in file_indices:
                amphipod[idx] = '.'
    return amphipod


def filesystem_checksum(amphipod):
    total_sum = 0
    for i, block in enumerate(amphipod):
        if block.isnumeric():
            total_sum += i * int(block)
    return total_sum


def main_part_two():
    path = "input.txt"
    map_ = read_input(path)
    if not map_:
        return

    amphipod = make_up_amphipod(map_)
    print("Initial amphipod:", ''.join(amphipod))

    compacted_amphipod = move_files_whole(amphipod)
    print("Compacted amphipod after whole-file moves:", ''.join(compacted_amphipod))

    checksum = filesystem_checksum(compacted_amphipod)
    print("Filesystem checksum (Part 2):", checksum)


if __name__ == "__main__":
    main_part_two()
