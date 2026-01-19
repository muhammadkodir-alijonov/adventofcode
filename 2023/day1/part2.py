def read_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]
def extract_digits(line):
    spelled_num = {
        'one':'1', 'two':'2', 'three':'3', 'four':'4',
        'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'
    }
    found = []
    
    for i in range(len(line)):
        # Check if the current character is a digit
        if line[i].isdigit():
            found.append(line[i])
        
        # Check if a spelled-out word starts at this index
        print(spelled_num.items())
        for word, digit in spelled_num.items():
            print(word + ' ' + digit)
            if line.startswith(word, i):
                found.append(digit)
                # We do NOT skip ahead; we move to i+1 in the next loop 
                # to catch overlaps like 'twone'
                
    return found

def calculate_trebuchet(data):
    total = 0
    for line in data:
        digits = extract_digits(line)
        if digits:
            # Combine the first and last found digit
            number = int(digits[0] + digits[-1])
            total += number
    return total

if __name__ == '__main__':
    file_path = 'input.txt'
    data = read_file(file_path)
    res = calculate_trebuchet(data)
    print(res)