def is_prime(n):

    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


k = int(input("nechta son kiritmoqchsiz (k>0)"))


prime_count = 0

for i in range(1, k+1):
    n = int(input(f"{i}-sonni kiriting"))

    if is_prime(n):
        prime_count += 1

print(prime_count)