

def EKUB(a,b):
    while b!= 0:
        a, b = b, a % b

    return a


a = int(input("1-sonni kiriting"))
b = int(input("2-sonni kiriting"))

print(EKUB(a, b))