n = int(input("Nechta son kiritasiz: "))

first_number = int(input("1-sonni kiriting: "))


min = first_number
index = 1

for i in range(2, n + 1):
    current_number = int(input("{i}Sonni kiriting: "))
    
    if current_number < min:
        min = current_number
        index = i
print(f"{index}-son eng kichik son")
print(f"Eng kichik son: {min}")