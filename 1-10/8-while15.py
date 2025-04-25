starter = int(input("Boshlangich summani kiriting: "))
p = int(input("Foizni kiriting: "))

current = starter
month = 0

while current < 2 * starter:
    current += current * (p / 100)
    month += 1

print(f"{month} oydan keyin {current} ga teng bo'ladi")    