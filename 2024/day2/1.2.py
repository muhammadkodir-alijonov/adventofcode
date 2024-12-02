from collections import Counter

def calculate_total_distance_from_file(file_name):
    left_list = []
    right_list = []

    try:
        with open(file_name, "r") as file:
            for line in file:
                numbers = line.split()
                if len(numbers) == 2:
                    left_list.append(int(numbers[0]))
                    right_list.append(int(numbers[1]))

        return calculate_similarity_score(left_list, right_list)

    except FileNotFoundError:
        print("Fayl topilmadi.")
        return None
    except ValueError:
        print("Faylda noto'g'ri formatdagi ma'lumot bor.")
        return None

def calculate_similarity_score(left_list, right_list):
    right_count = Counter(right_list)

    total_similarity_score = 0

    for num in left_list:
        total_similarity_score += num * right_count[num]

    return total_similarity_score

file_name = "input.txt"

result = calculate_total_distance_from_file(file_name)
if result is not None:
    print(f"Umumiy masofa: {result}")
