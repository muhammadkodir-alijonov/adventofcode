def read_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]



def find_word(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    count = 0
    for row in grid:
        count += row.count(word)
        count += row[::-1].count(word)

    for col in range(cols):
        column_str = ''.join([grid[row][col] for row in range(rows)])
        count += column_str.count(word)
        count += column_str[::-1].count(word)

    for row in range(rows - word_len + 1):
        for col in range(cols - word_len + 1):
            diag_str = ''.join([grid[row + i][col + i] for i in range(word_len)])
            count += diag_str.count(word)
            count += diag_str[::-1].count(word)

    for row in range(word_len - 1, rows):
        for col in range(cols - word_len + 1):
            diag_str = ''.join([grid[row - i][col + i] for i in range(word_len)])
            count += diag_str.count(word)
            count += diag_str[::-1].count(word)

    return count



if __name__ == '__main__':
    file_path = 'input.txt'
    grid = read_file(file_path)

    word_to_find = 'XMAS'
    count = find_word(grid, word_to_find)
    
    print(f"XMAS {count}")