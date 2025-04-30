
def find_ser(arr):
    B = []
    C = []

    n = len(arr)
    current_value = arr[0]
    count = 1

    for i in range(1, n + 1):
        if i < n and arr[i] == current_value:
            count += 1
        else:
            B.append(count)
            C.append(current_value)
            current_value = arr[i]
            count = 1
    return B, C

resultB1, resultC1 = find_ser([1,1,1,2,2,3,4,5,5,5])

print(resultB1)
print(resultC1)