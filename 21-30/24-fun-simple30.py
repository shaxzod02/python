def digit_n (k, n):

    str_k = str(k)

    if len(str_k) < n:
        return -1
    else:
        return str_k[n - 1]
    
number = int(input("Sonni kiriting"))
order = int(input("Tartib raqamni kiriting"))

print(digit_n(number, order))