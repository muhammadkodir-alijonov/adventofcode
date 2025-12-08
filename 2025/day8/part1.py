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
        # Kichik guruhni kattasiga qo'shamiz
        if size[root_i] < size[root_j]:
            root_i, root_j = root_j, root_i
        parent[root_j] = root_i
        size[root_i] += size[root_j]
        return True
    return False

def solve():
    positions = read_data('input.txt')
    n = len(positions)

    # 1. Barcha masofalarni hisoblash (itertools bilan oson)
    edges = []
    for (i, p1), (j, p2) in itertools.combinations(enumerate(positions), 2):
        dist_sq = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2
        edges.append((dist_sq, i, j))

    # 2. Masofa bo'yicha saralash
    edges.sort()

    # 3. Eng yaqin 1000 ta juftlikni ulash
    parent = list(range(n))
    size = [1] * n

    # edges[:1000] -> avtomatik ravishda birinchi 1000 tasini oladi
    for _, u, v in edges[:1000]:
        union(parent, size, u, v)

    # 4. Natijani hisoblash (faqat guruh boshliqlarini olamiz)
    final_sizes = [size[i] for i in range(n) if parent[i] == i]
    final_sizes.sort(reverse=True)

    print("Eng katta 3 ta circuit:", final_sizes[:3])
    
    if len(final_sizes) >= 3:
        print("Natija:", final_sizes[0] * final_sizes[1] * final_sizes[2])
    else:
        print("Natija: 0")

if __name__ == "__main__":
    solve()