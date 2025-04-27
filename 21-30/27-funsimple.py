


def EKUB(a,b):
    while b!= 0:
        a, b = b, a % b

    return a


def EKUB(a,b):
    ekub = a * b / EKUB(a,b)
    return ekub

a = int(input("1-sonni kiriting"))
b = int(input("2-sonni kiriting"))

print(EKUB(a, b))