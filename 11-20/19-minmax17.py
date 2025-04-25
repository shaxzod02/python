n = int(input("Nechta son kiritasiz: "))
first_number = int(input("1-sonni kiriting: "))
max_value = first_number
max_pos = 1

for i in range(2, n + 1):
    current_number = int(input(f"{i}-sonni kiriting: "))
    
    if current_number >= max_value:
        max_value = current_number
        max_pos = i


next_element_count = n - max_pos

print(max_value, next_element_count)