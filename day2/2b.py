
# Using readlines()
file1 = open('data.txt', 'r')
Lines = file1.readlines()

cube_map = {"red": 12, "green": 13, "blue": 14}

total_count = 0

games = 3
game_total = 0

for line in Lines:
    min_colour_map = {}
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
                
                if cube_colour in min_colour_map:
                    if int(cube_count) > min_colour_map[cube_colour]:
                        min_colour_map[cube_colour] = int(cube_count)
                else:
                    min_colour_map[cube_colour] = int(cube_count)

        sub_game_line_count += 1
    if game_valid:
        power_cube = 1
        for a, b in min_colour_map.items():
            power_cube *= b
        game_total += power_cube
print(f"total is {game_total}")

