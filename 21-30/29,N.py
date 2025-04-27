

def EKUB(a,b):
    while b!= 0:
        a, b = b, a % b

    return a


def EKUB_list(numbers):
    current_ekub = numbers[0]

    for number in numbers[1:]:
        current_ekub = EKUB(current_ekub, number)

    return current_ekub

n = int(input("nechta son kiritmoqchisiz"))

numbers = []

for i in range(1, n+1):
    current_number = int(input(f"{i}-sonni kiriting"))
    numbers.append(current_number)

print(EKUB_list(numbers))