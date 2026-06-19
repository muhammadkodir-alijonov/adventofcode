def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        return [line.replace("Game ", "") for line in content.strip().split("\n")]

def calculate_cubes(data):
    pass

if __name__ == '__main__':
    file_path = 'input.txt'
    data = read_file(file_path)
    print(data) 