number = int(input("sonni kiring: "))

digit_count = 0
digit_sum = 0

while number > 0:
    digit_sum += number % 10
    number = number // 10

    digit_count += 1

print(f"Raqamlar soni: {digit_count}")    