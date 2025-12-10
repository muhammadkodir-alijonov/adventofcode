import re
from itertools import product

def parse_data(file_path):
    machines = []
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
    for line in lines:
        if not line.strip():
            continue

        target_match = re.search(r'\[([.#]+)\]', line)
        if not target_match:
            continue
            
        target_str = target_match.group(1)

        target = [1 if c == '#' else 0 for c in target_str]

        buttons_matches = re.findall(r'\(([\d,]+)\)', line)
        buttons = []
        
        for b_str in buttons_matches:
            indices = [int(x) for x in b_str.split(',')]
            buttons.append(indices)
            
        machines.append({
            'target': target,
            'buttons': buttons
        })
        
    print(f"Parsed {len(machines)} machines from data.")
    for i, machine in enumerate(machines):
        print(f"Machine {i+1}: Target: {machine['target']}, Buttons: {machine['buttons']}")
    return machines

def solve_machine(target, buttons):
    num_lights = len(target)
    num_buttons = len(buttons)
    min_presses = float('inf')
    found = False

    # Barcha kombinatsiyalarni sinab ko'ramiz (0=bosmaslik, 1=bosish)
    # Masalan 2 ta tugma bo'lsa: (0,0), (0,1), (1,0), (1,1)
    for combo in product([0, 1], repeat=num_buttons):
        # Hozirgi chiroqlar holati (boshida hammasi 0)
        current_lights = [0] * num_lights
        press_count = 0
        
        for i, press in enumerate(combo):
            if press == 1:
                press_count += 1
                # Tugma bosilganda tegishli chiroqlarni o'zgartiramiz
                affected_lights = buttons[i]
                for light_idx in affected_lights:
                    if light_idx < num_lights:
                        # 0 bo'lsa 1, 1 bo'lsa 0 qilamiz (Toggle)
                        current_lights[light_idx] = 1 - current_lights[light_idx]
        
        # Tekshiramiz: biz xohlagan natija chiqdimi?
        if current_lights == target:
            if press_count < min_presses:
                min_presses = press_count
                found = True

    return min_presses if found else 0

if __name__ == "__main__":
    file_path = 'input.txt'
    all_machines = parse_data(file_path)
    
    total_presses = 0
    
    for i, machine in enumerate(all_machines):
        presses = solve_machine(machine['target'], machine['buttons'])
        total_presses += presses
        print(f"Mashina {i+1}: {presses} ta bosish")

    print(f"ans: {total_presses}")