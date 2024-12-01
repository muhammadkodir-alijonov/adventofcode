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

        left_list.sort()
        right_list.sort()

        total_distance = 0
        for left, right in zip(left_list, right_list):
            total_distance += abs(left - right)

        return total_distance

    except FileNotFoundError:
        print("Fayl topilmadi.")
        return None
    except ValueError:
        print("Faylda noto'g'ri formatdagi ma'lumot bor.")
        return None

file_name = "input.txt"

result = calculate_total_distance_from_file(file_name)
if result is not None:
    print(f"Umumiy masofa: {result}")
