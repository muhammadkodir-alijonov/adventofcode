with open("input.txt") as fin:
    lines = fin.readlines()

n = len(lines)
m = len(lines[0])


def has_xmas(i, j):
    if not (1 <= i < n - 1 and 1 <= j < m - 1):
        return False
    if lines[i][j] != "A":
        return False

    diag_1 = [lines[i - 1][j - 1], lines[i + 1][j + 1]]
    diag_2 = [lines[i - 1][j + 1], lines[i + 1][j - 1]]

    # Diagonallarni tekshirish
    return "".join(diag_1) in ["MS", "SM"] and "".join(diag_2) in ["MS", "SM"]



ans = 0
for i in range(n):
    for j in range(m):
        ans += has_xmas(i, j)

print(ans)
