
# Using readlines()
file1 = open('file1.txt', 'r')
Lines = file1.readlines()

num_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
num_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

total_count = 0

for line in Lines:
    first_number_counter = 0
    line_length_counter = 1

    line_length = len(line)
 
    while line_length_counter <= line_length: 
        # print(line[0])
        if line[0].isnumeric():
            if first_number_counter == 0:
                first_number = line[0]
                first_number_counter = 1
            last_number = line[0]
        else:
            for y in num_list:
                if line.startswith(y):
                    if first_number_counter == 0:
                        first_number_str = y
                        first_number = num_dict[first_number_str]
                        first_number_counter = 1
                    else:
                        last_number = num_dict[y]

        line = line[1:]  
        line_length_counter += 1  

    value = str(first_number)+str(last_number)

    total_count = total_count + int(value)

print(f"total is {total_count}")

