def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

print(selection_sort([4,6,2,1,7]))
print(selection_sort([10,2,9,3,1,8,7,3,4,5]))