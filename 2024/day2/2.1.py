def reports(file_name):
    count = 0
    try:
        with open(file_name, "r") as file:
            for line in file:
                numbers = list(map(int, line.split()))
                n = len(numbers)
                if n < 2:
                    continue
                count += is_safe(numbers)
    except FileNotFoundError:
        print("Fayl topilmadi.")
        return None
    return count

def is_safe(nums):
    inc = nums[1] > nums[0]
    if inc:
        for i in range(1, len(nums)):
            dif = nums[i] - nums[i - 1]
            if not (1 <= dif <= 3):
                return False
        return True
    else:
        for i in range(1, len(nums)):
            dif = nums[i - 1] - nums[i]
            if not (1 <= dif <= 3):
                return False
        return True

file_name = "input.txt"

result = reports(file_name)
if result is not None:
    print(f"Shartga mos keluvchi qatorlar soni: {result}")


