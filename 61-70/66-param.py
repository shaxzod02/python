
def invert(a,n):
    start = 0
    end = n - 1
    while start < end:
        a[start], a[end] = a[end], a[start]
        start += 1
        end -=1

    return a


a = [1,2,3,4,5,6]
n = len(a)

print(invert(a,n))