def read_file(file_path):
    with open(file_path, 'r') as file:
        # Har bir qatorni ro'yxatga olamiz va ortiqcha bo'shliqlarni olib tashlaymiz
        return [line.strip() for line in file if line.strip()]

def calculate_cubes(data):
    # Maksimal ruxsat etilgan kublar soni
    max_cubes = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    
    possible_games_sum = 0

    for line in data:
        # "Game 1: 3 blue, 4 red; ..." -> ["Game 1", "3 blue, 4 red; ..."]
        game_part, rounds_part = line.split(":")
        
        # O'yin ID raqamini ajratib olamiz: "Game 1" -> 1
        game_id = int(game_part.split()[1])
        
        # Raundlarni ajratamiz: "3 blue, 4 red; 1 red, 2 green" -> ["3 blue, 4 red", "1 red, 2 green"]
        rounds = rounds_part.split(";")
        
        game_is_possible = True
        
        for round_data in rounds:
            # Har bir raunddagi kublarni ajratamiz: "3 blue, 4 red" -> ["3 blue", "4 red"]
            cubes = round_data.split(",")
            
            for cube in cubes:
                # " 3 blue" -> count = 3, color = "blue"
                count, color = cube.strip().split()
                count = int(count)
                
                # Agar o'yindagi kublar soni ruxsat etilgandan ko'p bo'lsa, o'yin imkonsiz
                if count > max_cubes[color]:
                    game_is_possible = False
                    break # Ichki sikldan chiqish
            
            if not game_is_possible:
                break # Agar o'yin imkonsiz bo'lsa, keyingi raundlarni tekshirish shart emas
                
        # Agar o'yin barcha shartlarga javob bersa, uning ID sini summasiga qo'shamiz
        if game_is_possible:
            possible_games_sum += game_id

    return possible_games_sum

if __name__ == '__main__':
    # Fayl yo'li
    file_path = 'input.txt'
    
    # Ma'lumotni o'qish
    data = read_file(file_path)
    
    # Natijani hisoblash
    result = calculate_cubes(data)
    print(f"Possible games ID sum: {result}")