
x = int(input("1-sonni kiriting(x): "))
y = int(input("2-sonni kiriting(y): "))

min = (x + y) / 2
max = 2 * x * y

if x > y:
    x, y = max, min
elif x < y:
    x, y = min, max

print(f"{x}  {y}")    