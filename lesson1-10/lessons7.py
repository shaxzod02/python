
N = int(input("N kiriting" ))

def sum_of_devisor(number):
    total = 0

    for i in range(1, number):
        if number % i == 0:
            total += i

    return total

amicable_pairs = []

for a in range(1, N+1):
    b = sum_of_devisor(a)

    if a < b <= N and a == sum_of_devisor(b):
        amicable_pairs.append((a, b))

for pari in amicable_pairs:
    print(f"{pari[0]} - {pari[1]}")        
