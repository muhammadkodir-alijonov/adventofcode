import sys
import time

# Rekursiya chuqurligini oshiramiz
sys.setrecursionlimit(100000)

def read_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    shape_map = {}
    dimension_map = {}
    current_shape_id = None
    current_shape = []

    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Shakl ID sini o'qish (masalan "0:")
        if line[0].isdigit() and line.endswith(':'):
            if current_shape_id is not None: 
                shape_map[current_shape_id] = current_shape
                current_shape = []
            current_shape_id = int(line[:-1])
        # Shakl qatorlarini o'qish
        elif all(c in '#.' for c in line):
            current_shape.append(list(line))
        # O'lcham va sovg'alar ro'yxatini o'qish
        else:
            if ':' in line:
                parts = line.split(':')
                dimension = parts[0].strip()
                shape_ids = list(map(int, parts[1].strip().split()))
                if dimension not in dimension_map: 
                    dimension_map[dimension] = []
                dimension_map[dimension].append(shape_ids)

    if current_shape_id is not None and current_shape: 
        shape_map[current_shape_id] = current_shape

    return shape_map, dimension_map

def get_all_rotations(shape):
    rotations = set()
    current = [row[:] for row in shape]
    
    for _ in range(4):
        rotations.add(tuple(map(tuple, current)))
        
        # Gorizontal aks (flip)
        flipped = [row[::-1] for row in current]
        rotations.add(tuple(map(tuple, flipped)))
        
        # 90 gradus aylantirish
        current = [list(row) for row in zip(*current[::-1])]
    
    return [[list(row) for row in rotation] for rotation in rotations]

def get_shape_coords(shape):
    coords = []
    for r, row in enumerate(shape):
        for c, val in enumerate(row):
            if val == '#':
                coords.append((r, c))
    return coords

def can_place(grid, coords, start_row, start_col):
    height = len(grid)
    width = len(grid[0])
    
    for dr, dc in coords:
        r = start_row + dr
        c = start_col + dc
        # Chegaradan chiqib ketishni tekshirish
        if r < 0 or r >= height or c < 0 or c >= width:
            return False
        if grid[r][c] != '.':
            return False
    return True

def place_shape(grid, coords, start_row, start_col):
    for dr, dc in coords:
        grid[start_row + dr][start_col + dc] = 'X'

def remove_shape(grid, coords, start_row, start_col):
    for dr, dc in coords:
        grid[start_row + dr][start_col + dc] = '.'

def solve(grid, pieces_to_place):
    if all(count == 0 for _, count in pieces_to_place):
        return True

    empty_cells = sum(row.count('.') for row in grid)
    required_area = 0
    for rotations, count in pieces_to_place:
        if count > 0:
            # Har bir sovg'a yuzasini hisoblaymiz (birinchi aylanishdan olish kifoya)
            area = len(get_shape_coords(rotations[0]))
            required_area += area * count
    
    if empty_cells < required_area:
        return False
    
    height = len(grid)
    width = len(grid[0])
    first_empty = None
    for r in range(height):
        for c in range(width):
            if grid[r][c] == '.':
                first_empty = (r, c)
                break
        if first_empty:
            break
    
    if not first_empty:
        return False
    
    er, ec = first_empty
    
    for i in range(len(pieces_to_place)):
        rotations, count = pieces_to_place[i]
        
        if count > 0:
            for rotation in rotations:
                coords = get_shape_coords(rotation)
                
                for dr, dc in coords: 
                    start_r = er - dr
                    start_c = ec - dc
                    
                    if can_place(grid, coords, start_r, start_c):
                        place_shape(grid, coords, start_r, start_c)
                        pieces_to_place[i] = (rotations, count - 1)
                        
                        if solve(grid, pieces_to_place):
                            return True
                        
                        # Backtrack
                        pieces_to_place[i] = (rotations, count)
                        remove_shape(grid, coords, start_r, start_c)

    grid[er][ec] = 'B'
    
    if solve(grid, pieces_to_place):
        return True
        
    grid[er][ec] = '.'
    return False

def count_valid_region(shape_map, dimension_map):
    all_rotations = {}
    for idx, shape in shape_map.items():
        all_rotations[idx] = get_all_rotations(shape)
    
    valid_count = 0
    
    for dimension, piece_lists in dimension_map.items():
        width, height = map(int, dimension.split('x'))
        
        for piece_list in piece_lists:
            # Grid yaratish eng katta vaqqtni oladi bu
            grid = [['.' for _ in range(width)] for _ in range(height)]
            
            pieces_to_place = []
            for shape_idx, count in enumerate(piece_list):
                if count > 0:
                    pieces_to_place.append((all_rotations[shape_idx], count))
            
            pieces_to_place.sort(key=lambda x: -len(get_shape_coords(x[0][0])))

            if solve(grid, pieces_to_place):
                valid_count += 1
            else:
                pass
    
    return valid_count

if __name__ == "__main__":
    try:
        shape_map, dimension_map = read_data('input.txt')
        
        print("Shape Map:")
        for k, v in shape_map.items():
            print(f"{k}: {v}")
        
        print("\nDimension Map:")
        for k, v in dimension_map.items():
            print(f"{k}: {v}")
        # calculate time
        start_time = time.time()
        result = count_valid_region(shape_map, dimension_map)
        end_time = time.time()
        print(f"\nNumber of valid regions: {result}")
        print(f"Execution time: {end_time - start_time:.4f} seconds")
    except FileNotFoundError:
        print("Xatolik: 'input.txt' fayli topilmadi.")
