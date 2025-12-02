def read_ranges(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return [tok.strip() for tok in text.replace('\n', ',').split(',') if tok.strip()]

def calculate_range_token(left, right) -> int:
    print(left)
    print(right)
    summ = 0
    for num in range(left, right+1): 
        if is_invalid_token(num):
            summ += num
    return summ

def is_invalid_token(num) -> bool:
    s = str(num)
    length = len(s)
    for size in range(1, length // 2 + 1):
        if length % size == 0:
            segment = s[:size]
            if segment * (length // size) == s:
                return True
    return False

if __name__ == "__main__":
    path = '2025/day2/input.txt'
    data = read_ranges(path)
    print('data len: ' + str(data))
    ans = 0
    for rng in data:
        left, right = map(int, rng.split('-'))
        print(f'Processing range: {left}-{right}')
        ans += calculate_range_token(left, right)
    print('ans: ' + str(ans))