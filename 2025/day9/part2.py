def read_data(file_path):
    with open(file_path, 'r') as f:
        result = []
        for line in f:
            line = line.strip()
            if line:
                parts = line.split(',')
                if len(parts) == 2:
                    result.append(tuple(map(int, parts)))
        return result

def is_point_inside(x, y, polygon):
    """Ray casting: Nuqta polygon ichidami?"""
    inside = False
    n = len(polygon)
    j = n - 1
    for i in range(n):
        xi, yi = polygon[i]
        xj, yj = polygon[j]
        
        # Qirra bilan kesishishni tekshirish
        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi):
            inside = not inside
        j = i
    return inside

def solve(data):
    if not data:
        return 0
    
    n = len(data)
    # Polygon qirralarini tayyorlab olamiz
    edges = []
    for i in range(n):
        p1 = data[i]
        p2 = data[(i + 1) % n]
        edges.append((p1, p2))

    max_area = 0
    
    # Har bir juftlikni tekshiramiz
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = data[i]
            x2, y2 = data[j]
            
            # To'rtburchak chegaralari
            min_x, max_x = min(x1, x2), max(x1, x2)
            min_y, max_y = min(y1, y2), max(y1, y2)
            
            # Hozirgi yuza
            current_area = (max_x - min_x + 1) * (max_y - min_y + 1)
            
            # Optimallashtirish: Agar bu yuza topilgan max dan kichik bo'lsa, tekshirib o'tirmaymiz
            if current_area <= max_area:
                continue

            # 1-SHART: Markaz polygon ichidami?
            mid_x = (min_x + max_x) / 2
            mid_y = (min_y + max_y) / 2
            if not is_point_inside(mid_x, mid_y, data):
                continue

            # 2-SHART: Polygonning birorta qirrasi to'rtburchakni kesib o'tadimi?
            # Bizga faqat to'rtburchakning ICHIDAN o'tadigan qirralar xalaqit beradi.
            is_valid = True
            for (ex1, ey1), (ex2, ey2) in edges:
                # Qirra chegaralari
                e_min_x, e_max_x = min(ex1, ex2), max(ex1, ex2)
                e_min_y, e_max_y = min(ey1, ey2), max(ey1, ey2)

                if ex1 == ex2: # Vertikal qirra
                    # Agar qirra to'rtburchakning X oralig'ida bo'lsa (qat'iy ichida)
                    if min_x < ex1 < max_x:
                        # Va Y oralig'i kesishsa
                        if max(min_y, e_min_y) < min(max_y, e_max_y):
                            is_valid = False
                            break
                else: # Gorizontal qirra
                    # Agar qirra to'rtburchakning Y oralig'ida bo'lsa (qat'iy ichida)
                    if min_y < ey1 < max_y:
                        # Va X oralig'i kesishsa
                        if max(min_x, e_min_x) < min(max_x, e_max_x):
                            is_valid = False
                            break
            
            if is_valid:
                max_area = current_area

    return max_area

if __name__ == "__main__":
    data = read_data('input.txt')
    print(f"Nuqtalar soni: {len(data)}")
    print('ans:', solve(data))