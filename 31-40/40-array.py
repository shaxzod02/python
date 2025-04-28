
def bubble_sort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(n - 1 - i):
            if arr[j]> arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


    return arr



print(bubble_sort([4,2,7,3,1,10,6]))
print(bubble_sort([4,6,2,1,7]))