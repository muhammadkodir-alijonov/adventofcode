import sys
sys.setrecursionlimit(20000)

def read_data(file_path):
    data_map = {}
    with open(file_path, 'r') as file:
        for line in file:
            if not line.strip():
                continue
            parts = line.strip().split(': ')
            if len(parts) == 2:
                key, values = parts
                data_map[key] = values.split(' ')
    return data_map

def count_paths_memo(data_map, current, end, visited_dac, visited_fft, memo):
    state = (current, visited_dac, visited_fft)
    if state in memo:
        return memo[state]
    
    if current == end:
        return 1 if visited_dac and visited_fft else 0
    
    if current not in data_map:
        return 0
        
    total_paths = 0
    for neighbor in data_map[current]:
        new_dac = visited_dac or (neighbor == 'dac')
        new_fft = visited_fft or (neighbor == 'fft')
        total_paths += count_paths_memo(data_map, neighbor, end, new_dac, new_fft, memo)
        
    memo[state] = total_paths
    return total_paths

if __name__ == "__main__":
    data_map = read_data('2025/day11/input.txt')
    memo = {}
    start_node = 'svr'
    start_dac = (start_node == 'dac')
    start_fft = (start_node == 'fft')
    total_paths = count_paths_memo(data_map, start_node, 'out', start_dac, start_fft, memo)
    print(f"ans: {total_paths}")
