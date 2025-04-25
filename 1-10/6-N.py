N = int(input("N kiring: "))
perfect_numbers = []

for number in range(2, N + 1):

    is_perfect = True

    for i in range(1, number):
        if number % i == 0:
            is_perfect = False
    
    if is_perfect:
        perfect_numbers.append(number)

print(*perfect_numbers)        