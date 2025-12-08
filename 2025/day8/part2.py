import itertools

def read_data(file_path):
    with open(file_path, 'r') as f:
        return [list(map(int, line.split(','))) for line in f if line.strip()]

def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, size, i, j):
    root_i = find(parent, i)
    root_j = find(parent, j)
    if root_i != root_j:
        if size[root_i] < size[root_j]:
            root_i, root_j = root_j, root_i
        parent[root_j] = root_i
        size[root_i] += size[root_j]
        return True
    return False

def solve():
    positions = read_data('input.txt')
    n = len(positions)

    # 1. Barcha masofalarni hisoblash
    edges = []
    for (i, p1), (j, p2) in itertools.combinations(enumerate(positions), 2):
        dist_sq = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2
        edges.append((dist_sq, i, j))

    # 2. Masofa bo'yicha saralash
    edges.sort()

    # 3. Birlashtirishni boshlaymiz
    parent = list(range(n))
    size = [1] * n
    components = n  # Boshida n ta alohida guruh bor

    for _, u, v in edges:
        if union(parent, size, u, v):
            components -= 1 # Guruhlar soni bittaga kamaydi
            
            # Agar hamma birlashib bo'lsa (faqat 1 ta guruh qolsa)
            if components == 1:
                x1 = positions[u][0]
                x2 = positions[v][0]
                print(f"Oxirgi ulangan nuqtalar: {positions[u]} va {positions[v]}")
                print(f"Natija (X * X): {x1 * x2}")
                return

if __name__ == "__main__":
    solve()