
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

number = int(input("sonni kiriting "))

print(fact(number))