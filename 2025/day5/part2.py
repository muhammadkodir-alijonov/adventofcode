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

"""
Now, the second section of the database (the available ingredient IDs) is irrelevant. Here are the fresh ingredient ID ranges from the above example:

3-5
10-14
16-20
12-18
The ingredient IDs that these ranges consider to be fresh are 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, and 20. So, in this example, the fresh ingredient ID ranges consider a total of 14 ingredient IDs to be fresh.

Process the database file again. How many ingredient IDs are considered to be fresh according to the fresh ingredient ID ranges?
"""

def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort()
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))
    return merged

def calculate_valid_num_of_diapasons(ranges_list):
    intervals = []
    for rng in ranges_list:
        left, right = map(int, rng.split('-'))
        intervals.append((left, right))
    merged = merge_intervals(intervals)
    total = sum(end - start + 1 for start, end in merged)
    return total


if __name__ == "__main__":
    l1, l2 = read_two_lists('input.txt')
    valid_count = calculate_valid_num_of_diapasons(l1)
    print("List 1:", l1)
    print("List 2:", l2)
    print("Valid count:", valid_count)