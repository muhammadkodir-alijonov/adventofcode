def read_matrix_and_ops(file_path):
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
        print(lines)
    matrix = [list(map(int, line.split())) for line in lines[:-1]]
    print(matrix)
    ops = lines[-1].split()
    print(ops)
    return matrix, ops

if __name__ == "__main__":
    matrix, ops = read_matrix_and_ops('input.txt')
    results = []
    for col in range(len(ops)):
        col_vals = [row[col] for row in matrix]
        if ops[col] == '*':
            res = 1
            for v in col_vals:
                res *= v
        elif ops[col] == '+':
            res = sum(col_vals)
        results.append(res)
    print(sum(results))