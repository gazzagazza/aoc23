
# Using readlines()
file1 = open('data.txt', 'r')
Lines = file1.readlines()

cube_map = {"red": 12, "green": 13, "blue": 14}

total_count = 0

games = 3
game_total = 0

for line in Lines:
    game_info = line.split(":")[0]
    game_number = game_info.split()[1]

    game_line = line.split(":")[1]
    sub_game_line = game_line.split(";")

    sub_game_line_count = 0
    game_valid = True
    while sub_game_line_count < games:    
        for x in sub_game_line:

            colour_sub_game_line = x.split(",")
            for y in colour_sub_game_line:
                cube_count = y.split()[0]
                cube_colour = y.split()[1]
                if int(cube_count) > cube_map[cube_colour]:
                    game_valid = False
        sub_game_line_count += 1
    if game_valid:
        game_total += int(game_number)
        
print(f"total is {game_total}")

