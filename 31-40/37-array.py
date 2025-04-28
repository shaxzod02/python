def find_clos(arr, r):
    min_diff = float('inf')
    closest_element = None

    for element in arr:
        diff = abs(element - r)
        if diff < min_diff:
            min_diff = diff
            closest_element = element

    return closest_element

print(find_clos([1, 3, 2, 4, 6, 5, 9, 1], 5))
print(find_clos([1, 11, 2, 4, 6, 7, 9, 1], 5))