n = int(input("nechta son kiritasiz: "))
first_number = int(input("1-sonni kiriting: "))

min_value = float("inf")

if first_number > 0:
    min_value = first_number

for i in range(2, n + 1):
    current_number = int(input(f"{i}-sonni kiriting: "))
    
    if 0 < current_number < min_value:
        min_value = current_number
if min_value == float("inf"):
    print(0)
else:
    print(min_value)      