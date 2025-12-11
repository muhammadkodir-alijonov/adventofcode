"""
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out


read data like that
in hashmap: {
    "aaa": ["you", "hhh"],
    "you": ["bbb", "ccc"],
    ...
    "iii": ["out"]
}
"""
def read_data(file_path):
    data_map = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, values = line.strip().split(': ')
            data_map[key] = values.split(' ')
    return data_map

# # we have to calculate that How many different paths lead from you to out?
# def calculate_paths(data_map, start, end, memo):
#     if start == end:
#         return 1
#     if start not in data_map:
#         return 0
#     if start in memo:
#         return memo[start]
    
#     total_paths = 0
#     for neighbor in data_map[start]:
#         total_paths += calculate_paths(data_map, neighbor, end, memo)
    
#     memo[start] = total_paths
#     return total_paths

# from collections import deque

def count_paths_bfs(data_map, start, end):
    queue = deque([[start]])
    count = 0

    while queue:
        path = queue.popleft()
        current = path[-1]
        if current == end:
            count += 1
            continue
        if current not in data_map:
            continue
        for neighbor in data_map[current]:
            queue.append(path + [neighbor])
    return count

if __name__ == "__main__":
    data_map = read_data('input.txt')
    total_paths = count_paths_bfs(data_map, 'you', 'out')
    print(f"ans: {total_paths}")

# if __name__ == "__main__":
#     data_map = read_data('input.txt')
#     memo = {}
#     total_paths = calculate_paths(data_map, 'you', 'out', memo)
#     print(f"ans: {total_paths}")
    