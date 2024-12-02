def reports(file_name):
    count = 0
    i = 0
    try:
        with open(file_name, "r") as file:
            for line in file:
                numbers = list(map(int, line.split()))
                n = len(numbers)
                if n < 2:
                    continue
                is_incresing = all(1<= numbers[i] - numbers[i + 1]<=3 for i in range(n - 1))
                is_decresing = all(1<= numbers[i+1] - numbers[i]<=3 for i in range(n - 1))
                if is_incresing or is_decresing:
                    count += 1
    except FileNotFoundError:
        print("Fayl topilmadi.")
        return None
    return count

file_name = "input.txt"

result = reports(file_name)
if result is not None:
    print(f"Shartga mos keluvchi qatorlar soni: {result}")
