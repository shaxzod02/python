def digit_count(K):

    count = 0

    while K > 0:
        K = K // 10
        count += 1

    return count

number = int(input("sonni kiriting"))
print(digit_count(number))    