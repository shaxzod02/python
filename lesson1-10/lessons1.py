a = int(input("1-sonni kiriting: "))
b = int(input("2-sonni kiriting: "))
c = int(input("3-sonni kiriting: "))

if a < b and a < c:
    print(a)
elif b < a and b < c:
    print(b)
else:
    print(c)