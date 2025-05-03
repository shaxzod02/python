
def min_element(a, n):
    min_element = a[0]
    for i in range(1, n):
        if a[i] < min_element:
            min_element = a[i]
    return min_element


print(min_element([1,2,3,4,5], 5))