from collections import defaultdict

def read_input(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    return [line.strip().split('-') for line in lines]

def find_connected_trios(connections):
    adjacency_list = defaultdict(set)
    for conn in connections:
        a, b = conn
        adjacency_list[a].add(b)
        adjacency_list[b].add(a)

    trios = set()

    for a in adjacency_list:
        for b in adjacency_list[a]:
            for c in adjacency_list[b]:
                if a != b and b != c and a != c and c in adjacency_list[a]:
                    trio = tuple(sorted([a, b, c]))
                    trios.add(trio)

    return trios

def filter_trios_with_t(trios):
    return [trio for trio in trios if any(comp.startswith('t') for comp in trio)]

def main():
    path = "input.txt"
    connections = read_input(path)

    trios = find_connected_trios(connections)
    trios_with_t = filter_trios_with_t(trios)

    print(f"All trios: {trios}")
    print(f"Trios with at least one 't': {trios_with_t}")
    print(f"Number of trios with at least one 't': {len(trios_with_t)}")

if __name__ == "__main__":
    main()
