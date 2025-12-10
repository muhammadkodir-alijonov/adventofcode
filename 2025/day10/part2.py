import re
from scipy.optimize import linprog, milp, LinearConstraint, Bounds
import numpy as np

def parse_data_part2(file_path):
    machines = []
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
    for line in lines: 
        if not line.strip():
            continue

        # Parse joltage requirements {3,5,4,7}
        joltage_match = re.search(r'\{([^\}]+)\}', line)
        if not joltage_match:
            continue
            
        joltage_str = joltage_match.group(1)
        target = [int(x) for x in joltage_str.split(',')]

        # Parse buttons (indices they affect)
        buttons_matches = re.findall(r'\(([\d,]+)\)', line)
        buttons = []
        
        for b_str in buttons_matches: 
            indices = [int(x) for x in b_str.split(',')]
            buttons. append(indices)
            
        machines.append({
            'target': target,
            'buttons': buttons
        })
        
    print(f"Parsed {len(machines)} machines from data.")
    for i, machine in enumerate(machines):
        print(f"Machine {i+1}:  Target:  {machine['target']}, Buttons: {machine['buttons']}")
    return machines

def solve_machine_part2(target, buttons):
    """
    Solve using Integer Linear Programming. 
    
    We need to find non-negative integers x_0, x_1, ..., x_n (button press counts)
    such that for each counter j: 
        sum(x_i for all buttons i that affect counter j) = target[j]
    
    Minimize: sum(x_i) (total button presses)
    """
    num_counters = len(target)
    num_buttons = len(buttons)
    
    if num_buttons == 0:
        # No buttons, check if target is all zeros
        if all(t == 0 for t in target):
            return 0
        else:
            return None  # Impossible
    
    # Build the constraint matrix A
    # A[j][i] = 1 if button i affects counter j, else 0
    A_eq = np.zeros((num_counters, num_buttons))
    
    for i, button in enumerate(buttons):
        for counter_idx in button:
            if counter_idx < num_counters: 
                A_eq[counter_idx][i] = 1
    
    b_eq = np. array(target)
    
    # Objective: minimize sum of all x_i (each x_i counts as 1 press)
    c = np.ones(num_buttons)
    
    # Use MILP (Mixed Integer Linear Programming) from scipy
    # All variables must be non-negative integers
    
    # Bounds:  x_i >= 0, no upper bound (but we can set a reasonable max)
    max_presses = max(target) * 2 if target else 100  # reasonable upper bound
    bounds = Bounds(lb=np.zeros(num_buttons), ub=np.full(num_buttons, max_presses))
    
    # Equality constraints: A_eq @ x = b_eq
    constraints = LinearConstraint(A_eq, b_eq, b_eq)
    
    # All variables are integers
    integrality = np.ones(num_buttons)  # 1 means integer
    
    try:
        result = milp(c, constraints=constraints, bounds=bounds, integrality=integrality)
        
        if result.success:
            total_presses = int(round(result.fun))
            return total_presses
        else:
            print(f"  No solution found:  {result.message}")
            return None
    except Exception as e:
        print(f"  Error solving: {e}")
        return None

if __name__ == "__main__":
    file_path = 'input.txt'
    all_machines = parse_data_part2(file_path)
    
    total_presses = 0
    
    for i, machine in enumerate(all_machines):
        presses = solve_machine_part2(machine['target'], machine['buttons'])
        if presses is not None:
            total_presses += presses
            print(f"Machine {i+1}:  {presses} button presses")
        else:
            print(f"Machine {i+1}: No solution!")

    print(f"\nAnswer: {total_presses}")