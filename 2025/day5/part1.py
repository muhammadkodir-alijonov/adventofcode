def read_two_lists(file_path):
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    list1 = []
    list2 = []
    for line in lines:
        if '-' in line:
            list1.append(line)
        else:
            list2.append(line)
    return list1, list2

"""
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

def calculate_valid_num_of_diapasons(l1, l2):
    for i in range(len(l1)):
        l1[i] = list(map(int, l1[i].split('-')))
    valid_count = 0
    for num_str in l2:
        num = int(num_str)
        for diapason in l1:
            if diapason[0] <= num <= diapason[1]:
                valid_count += 1
                break
    return valid_count

if __name__ == "__main__":
    l1, l2 = read_two_lists('input.txt')
    valid_count = calculate_valid_num_of_diapasons(l1, l2)
    print("List 1:", l1)
    print("List 2:", l2)
    print("Valid count:", valid_count)