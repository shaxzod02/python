a = int(input("1-sonni kiring: "))
b = int(input("2-sonni kiring: "))
c = int(input("3-sonni kiring: "))

if a < b and a < c:
    print(a)
elif b < a and b < c:
    print(b)
else:
    print(c)