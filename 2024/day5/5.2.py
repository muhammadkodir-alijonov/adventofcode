from collections import defaultdict

def read_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        ordering_rules = []
        updates = []
        empty_line_found = False

        for line in lines:
            if line.strip() == "":
                empty_line_found = True
                continue

            if not empty_line_found:
                # Read ordering rules
                numbers = list(map(int, line.strip().split("|")))
                ordering_rules.append(numbers)
            else:
                # Read updates
                updates.append(list(map(int, line.strip().split(","))))
        return ordering_rules, updates


def follows_rules(update, rules):
    idx = {num: i for i, num in enumerate(update)}
    for a, b in rules:
        if a in idx and b in idx and idx[a] > idx[b]:
            return False  # If the order is incorrect
    return True


def sort_update(update, rules):
    indeg = defaultdict(int)
    for a, b in rules:
        if a in update and b in update:
            indeg[b] += 1

    result = []
    while len(result) < len(update):
        for x in update:
            if x not in result and indeg[x] == 0:
                result.append(x)
                for a, b in rules:
                    if a == x:
                        indeg[b] -= 1
    return result


def find_middle(update):
    return update[len(update) // 2]


def main():
    middle_pages_sum = 0
    file_path = 'input.txt'
    ordering_rules, updates = read_file(file_path)

    for update in updates:
        if follows_rules(update, ordering_rules):
            continue

        sorted_update = sort_update(update, ordering_rules)

        middle_page = find_middle(sorted_update)
        middle_pages_sum += middle_page

    print(middle_pages_sum)


if __name__ == "__main__":
    main()
