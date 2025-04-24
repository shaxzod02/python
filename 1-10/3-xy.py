x = int(input("1-sonni kiring(x): "))
y = int(input("2-sonni kiring(y): "))

min = (x + y) / 2
max = (x * y) * 2

if x > y:
    x, y = max, min
elif x < y:
    x, y = min, max


print(f"X: {x}, Y: {y}")
# Compare this snippet from 1-10/2-if28.py:    