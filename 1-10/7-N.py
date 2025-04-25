N = int(input("N kiring: "))

def sum_of_divisor(num):
    total = 0

    for i in range(1, num):
        if num % i == 0:
            total += i

    return total

amicable_pair = []

for a in range(1, N + 1):
    b = sum_of_divisor(a)
    if a != b and a == sum_of_divisor(b):
        amicable_pair.append((a, b))

for pair in amicable_pair:
    print(pair[0], pair[1])
