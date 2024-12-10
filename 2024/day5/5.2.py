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
        if indeg.get(a) == 0:
            indeg[a] = 0

    # result =  dict(sorted(indeg.items(), key=lambda item: item[1]))
    result = []
    # for item, value in indeg.items():
    #     result.append(item)
    # 32: 9, 62: 7, 56: 6, 15: 4, 87: 8, 98: 10, 59: 5, 89: 3, 69: 2, 72: 1
    # print(indeg)    # print('Result ', result)
    # result = []
    templates = indeg.copy()
    while len(result) < len(update):
        # update = [75,47,61,53,29 ]
        # result = [47 ]
        for x in update:
            if x not in result and indeg[x] == 0:
                result.append(x)
                for a, b in rules:
                    if a == x:
                        indeg[b] -= 1
    return result, templates


def find_middle(update):
    return update[len(update) // 2]


def sort_update2(update, rules):
    indeg = defaultdict(int)
    for a, b in rules:
        if a in update and b in update:
            indeg[b] += 1
        # if indeg.get(a) == 0:
        #     indeg[a] = 0

    result =  dict(sorted(indeg.items(), key=lambda item: item[1]))
    result = []
    for item, value in indeg.items():
        result.append(item)
        
    res_, ind = sort_update(update, rules)
    if res_ != result:
        print("Result ", indeg)
        print("Res_", ind, )
        print(res_, )
        print(result)
        print()
    # 32: 9, 62: 7, 56: 6, 15: 4, 87: 8, 98: 10, 59: 5, 89: 3, 69: 2, 72: 1
    # result = []

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

        # sorted_update = sort_update(update, ordering_rules)
        sorted_update = sort_update2(update, ordering_rules)

        middle_page = find_middle(sorted_update)
        middle_pages_sum += middle_page

    print(middle_pages_sum)


if __name__ == "__main__":
    main()
