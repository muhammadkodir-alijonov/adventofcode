def parse_input(input_data):
    """Parse the input into initial wire values and gate operations."""
    wire_values = {}
    gate_operations = []

    for line in input_data.splitlines():
        if ":" in line:
            wire, value = line.split(": ")
            wire_values[wire] = int(value)
        elif "->" in line:
            gate_operations.append(line)
    print(wire_values)
    print(gate_operations)
    return wire_values, gate_operations

def evaluate_gate(op, val1, val2):
    """Evaluate the output of a gate based on its operation."""
    if op == "AND":
        return val1 & val2
    elif op == "OR":
        return val1 | val2
    elif op == "XOR":
        return val1 ^ val2
    else:
        raise ValueError(f"Unknown operation: {op}")

def simulate_circuit(wire_values, gate_operations):
    pending_gates = gate_operations.copy()

    while pending_gates:
        for gate in pending_gates[:]:
            parts = gate.split()

            if len(parts) == 5:  
                input1, op, input2, _, output = parts

                if input1 in wire_values and input2 in wire_values:
                    wire_values[output] = evaluate_gate(op, wire_values[input1], wire_values[input2])
                    pending_gates.remove(gate)

    return wire_values

def compute_output(wire_values):
    z_wires = {key: value for key, value in wire_values.items() if key.startswith('z')}
    print()
    sorted_bits = [z_wires[f"z{str(i).zfill(2)}"] for i in range(len(z_wires))]
    binary_number = int("".join(map(str, sorted_bits[::-1])), 2)  
    return binary_number

with open('./2024/day24/input.txt', 'r') as file:
    input_data = file.read()

wire_values, gate_operations = parse_input(input_data)
final_wire_values = simulate_circuit(wire_values, gate_operations)
print(f"Final wire values: {final_wire_values}")
output = compute_output(final_wire_values)
print(f"Output: {output}")  