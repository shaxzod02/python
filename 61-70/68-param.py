
def doubleX(a,n,x):
    res = []
    for element in a:
        res.append(element)
        if element == x:
            res.append(element)

    new_length = len(res)
    return res, new_length

n = int(input("Qancha son kiritasiz: "))
a = [int(x) for x in input().split()]
x = int(input("X: "))

a, n = doubleX(a, n, x)

print(*a)