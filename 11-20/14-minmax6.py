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

print(f"{max_pos}-son eng katta son")
print(f"Eng katta son: {max}")
print(f"{min_pos}-son eng kichik son")
print(f"Eng kichik son: {min}")