

def EKUB(a,b):
    while b!= 0:
        a, b = b, a % b

    return a


a = int(input("1-sonni kiriting"))
b = int(input("2-sonni kiriting"))
c = int(input("3-sonni kiriting"))

def EKUB3(a,b,c):
    ekub_ab = EKUB(a,b)
    ekub3 = EKUB3(ekub_ab, c)
    return ekub3



print(EKUB3(a, b, c))