def array_pattern(arr):

    n = len(arr)

    left = 0
    right = n - 1
    result = []


    while left<=right:
        if left<=right:

             result.append(arr[left])
             left += 1

        if left <= right:
            result.append(arr[right])
            right -= 1
        

    return result 


print(array_pattern([1,2,3,4,5]))    
print(array_pattern([1,2,3,4,5,6]))    
 
