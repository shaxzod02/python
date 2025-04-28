
def find_small_local_maxima(arr):

    n = len(arr)
    local_maximas = []

    for i in range(1, n - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            local_maximas.append(arr[i])

    if local_maximas:
        return min(local_maximas)
    else:
        return None
    

print(find_small_local_maxima([1, 3, 2, 4, 6, 5, 9, 1]))
print(find_small_local_maxima([1, 11, 2, 4, 6, 5, 9, 1]))
    
    