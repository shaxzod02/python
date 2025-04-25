n = int(input("nechta son kiritasiz: "))
first_number = int(input("1-sonni kiriting: "))

max_value = None
max_pos = -1

if first_number % 2 != 0:
    max_value = first_number
    max_pos = 1

for i in range(2, n + 1):
    current_number = int(input(f"{i}-sonni kiriting: "))
    
    if current_number % 2 != 0:
        if max_value is None or current_number > max_value:
            max_value = current_number
            max_pos = i
if max_value is None:
    print(0)
else:
    print(max_value)
    print(max_pos)


