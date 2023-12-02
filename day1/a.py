
# Using readlines()
file1 = open('file1.txt', 'r')
Lines = file1.readlines()

total_count = 0

for line in Lines:
    first_number_counter = 0
  
    line = line.strip()
    for x in line:
        if x.isnumeric():
            if first_number_counter == 0:
                first_number = x
                first_number_counter = 1
            last_number = x
    
    value = str(first_number)+str(last_number)
    
    total_count = total_count + int(value)

print(f"total is {total_count}")

