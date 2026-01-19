def read_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

if __name__ == '__main__':
    file_path = 'input.txt'
    data = read_file(file_path)
    print(res)