
def fact2(n):
    if n == 1 or n == 2:
        return n
    else:
        return n * fact2(n - 2)

number = int(input("sonni kiriting"))
print(fact2(number))    