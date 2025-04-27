
def is_polydrome(n):
    str_n = str(n)
    return str_n == str_n[::-1]

def count_ploy(number):
    count = 0

    for number in number:
        if is_polydrome(number):
            count += 1
    return count


print(count_ploy([12321, 123, 456]))
print(count_ploy([121, 23332, 1591]))
print(count_ploy([101, 121, 131]))