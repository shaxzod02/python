n = int(input("Nechta son kiritasiz: "))

first_number = int(input("1-sonni kiriting: "))

max = first_number
min = first_number

max_pos = 1
min_pos = 1

for i in range(2, n + 1):
    current_number = int(input("{i}Sonni kiriting: "))
    
    if current_number > max:
        max = current_number
        max_pos = i
    if current_number < min:
        min = current_number
        min_pos = i

if max_pos == min_pos:
    print(f"Eng katta va eng kichik sonlar bir xil: {min_pos}")
else:
    print(f"Eng katta son: {max}, {max_pos}-o'rinda")
    