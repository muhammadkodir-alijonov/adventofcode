def parse_input(filename):
    machines = []
    current_machine = {}

    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                if current_machine:
                    machines.append(current_machine)
                    current_machine = {}
                continue

            if line.startswith('Button A:'):
                parts = line.split(',')
                x = int(parts[0].split('+')[1])
                y = int(parts[1].split('+')[1])
                current_machine['A'] = (x, y)
            elif line.startswith('Button B:'):
                parts = line.split(',')
                x = int(parts[0].split('+')[1])
                y = int(parts[1].split('+')[1])
                current_machine['B'] = (x, y)
            elif line.startswith('Prize:'):
                parts = line.split(',')
                x = 10000000000+int(parts[0].split('=')[1])
                y = 10000000000+int(parts[1].split('=')[1])
                current_machine['prize'] = (x, y)

    if current_machine:
        machines.append(current_machine)

    return machines


def can_win_prize(machine, max_presses=100):
    ax, ay = machine['A']
    bx, by = machine['B']
    px, py = machine['prize']

    for a in range(max_presses + 1):
        for b in range(max_presses + 1):
            if (a * ax + b * bx == px) and (a * ay + b * by == py):
                return True, a, b
    return False, 0, 0


def calculate_tokens(a_presses, b_presses):
    return (a_presses * 3) + b_presses


def main():
    machines = parse_input('input.txt')
    total_tokens = 0
    winnable_prizes = 0
    print(machines)

    for i, machine in enumerate(machines, 1):
        can_win, a_presses, b_presses = can_win_prize(machine)
        if can_win:
            tokens = calculate_tokens(a_presses, b_presses)
            total_tokens += tokens
            winnable_prizes += 1
            print(f"Machine {i}: Win {a_presses} A p and {b_presses} B p ({tokens} tokens)")
        else:
            print(f"Machine {i}: Not win")

    print(f"\nTotal w: {winnable_prizes}")
    print(f"Totalt: {total_tokens}")


if __name__ == "__main__":
    main()