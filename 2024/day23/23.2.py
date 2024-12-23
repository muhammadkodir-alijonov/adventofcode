from collections import defaultdict



def read_input(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    return [line.strip().split('-') for line in lines]



def dfs(computer, adjacency_list, visited, component):
    visited.add(computer)
    component.append(computer)
    for neighbor in adjacency_list[computer]:
        if neighbor not in visited:
            dfs(neighbor, adjacency_list, visited, component)



def find_largest_connected_component(connections):
    adjacency_list = defaultdict(set)
    for a, b in connections:
        adjacency_list[a].add(b)
        adjacency_list[b].add(a)

    visited = set()
    largest_component = []

    for computer in adjacency_list:
        if computer not in visited:
            component = []
            dfs(computer, adjacency_list, visited, component)
            if len(component) > len(largest_component):
                largest_component = component

    return largest_component



def main():
    path = "input.txt"
    connections = read_input(path)

    largest_component = find_largest_connected_component(connections)
    largest_component.sort()
    password = ",".join(largest_component)

    print(f"Password: {password}")


if __name__ == "__main__":
    main()
