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
    n = len(s)
    half = n // 2
    return s[:half] == s[half:]

if __name__ == "__main__":
    path = 'input.txt'
    data = read_ranges(path)
    print('data len: ' + str(data))
    ans = 0
    for rng in data:
        left, right = map(int, rng.split('-'))
        print(f'Processing range: {left}-{right}')
        ans += calculate_range_token(left, right)
    print('ans: ' + str(ans))