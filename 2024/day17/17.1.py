def read_input():
    with open("input.txt") as file:
        a, b, c, p = 0, 0, 0, []
        for line in file:
            line = line.strip()
            if line.startswith('Register A:'):
                a = int(line.split(' ')[2])
            elif line.startswith('Register B:'):
                b = int(line.split(' ')[2])
            elif line.startswith('Register C:'):
                c = int(line.split(' ')[2])
            elif line.startswith('Program:'):
                p = list(map(int, line.split(' ')[1].split(',')))
        return a, b, c, p


def execute_program(a, b, c, program):
    output = []
    ip = 0

    while ip < len(program):
        opcode = program[ip]
        operand = program[ip + 1] if ip + 1 < len(program) else 0

        if opcode == 0:  # adv
            a = a // (2 ** resolve_combo_operand(operand, a, b, c))
        elif opcode == 1:  # bxl
            b = b ^ operand
        elif opcode == 2:  # bst
            b = resolve_combo_operand(operand, a, b, c) % 8
        elif opcode == 3:  # jnz
            if a != 0:
                ip = operand
                continue
        elif opcode == 4:  # bxc
            b = b ^ c
        elif opcode == 5:  # out
            output.append(resolve_combo_operand(operand, a, b, c) % 8)
        elif opcode == 6:  # bdv
            b = a // (2 ** resolve_combo_operand(operand, a, b, c))
        elif opcode == 7:  # cdv
            c = a // (2 ** resolve_combo_operand(operand, a, b, c))

        ip += 2

    return output


def resolve_combo_operand(operand, a, b, c):
    if operand <= 3:
        return operand
    elif operand == 4:
        return a
    elif operand == 5:
        return b
    elif operand == 6:
        return c
    else:
        print(f"Invalid operand: {operand}")


def main():
    a, b, c, program = read_input()

    output = execute_program(a, b, c, program)

    print(','.join(map(str, output)))


if __name__ == "__main__":
    main()
