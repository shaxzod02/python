n = int(input("nechta son kirtmoqchisiz"))

first_number = int(input("1-sonni kiriting"))
second_number = int(input("2-sonni kiriting"))

max_sum = first_number + second_number
prev_number = second_number

for i in range(3, n + 1):
    current_number = int(input(f"{i}-sonni kiriting"))

    current_sum = prev_number + current_number

    current_sum = prev_number + current_number

    if current_sum > max_sum:
        max_sum = current_sum

    prev_number = current_number


print(max_sum)        