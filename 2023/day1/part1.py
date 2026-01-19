def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        return [line.strip() for line in content.splitlines()]

def calculate_trebuchet(data):
    summ_ = 0
    for line in data:
        digits = [c for c in line if c.isdigit()]
        if digits:
            summ_ = int(digits[0] + digits[-1])
            total += summ_
            print(f"Intermediate sum :  {summ_}")
    print(f"Total:  {total}")

if __name__ == '__main__':
    file_path = 'input.txt'
    data = read_file(file_path)
    print(data) 
    res = calculate_trebuchet(data)
    print(res)