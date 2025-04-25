n = int(input("N:"))
m = int(input("M:"))

butun = 0

while n >= m:
    n -= m
    butun += 1

qoldiq = n
print(f"qoldiq: {qoldiq} Butun :, {butun}")    