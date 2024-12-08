def read_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        first = []
        second = []
        empty_line_found = False

        for line in lines:
            if line.strip() == "":
                empty_line_found = True
                continue

            if not empty_line_found:
                numbers = list(map(int, line.strip().split("|")))
                first.append(numbers)
            else:
                second.append(list(map(int, line.strip().split(","))))
        print(first)
        print(second)
        return first, second


def is_correct_order(update, ordering_rules):
    page_index = {page: idx for idx, page in enumerate(update)}

    for rule in ordering_rules:
        first, second = rule
        if first in page_index and second in page_index:
            if page_index[first] > page_index[second]:
                return False

    return True
def is_raely_correct_order(update, ordering_rules):
    page_index = {page: idx for idx, page in enumerate(update)}

    for rule in ordering_rules:
        first, second = rule
        if first in page_index and second in page_index:
            if page_index[first] > page_index[second]:
                return False

    return True

def find_middle(update):
    return update[len(update) // 2]


def main():
    total_sum = 0
    file_path = 'input.txt'
    ordering_rules, updates = read_file(file_path)

    for update in updates:
        if not is_correct_order(update, ordering_rules):
            middle_page = find_middle(update)
            total_sum += middle_page

    print(total_sum)


if __name__ == "__main__":
    main()
