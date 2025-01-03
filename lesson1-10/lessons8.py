
setarter = int(input("Boshlang'ich summani kiriting"))
p = int(input("foizni kiriting"))

current = setarter
month = 0


while current <= 2 * setarter:
    current += current * p / 100
    month += 1

print(f"{month} oyda {current} so'm")    