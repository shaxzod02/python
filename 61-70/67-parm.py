
def removeX(a,n,x):
    res = [element for element in a if element != x]
    new_length = len(res)

    return res, new_length

n = int(input("N: "))
a = [int(x) for x in input().split()]
x = int(input("X: "))

a, n = removeX(a, n, x)

print(*a)