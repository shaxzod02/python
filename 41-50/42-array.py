
def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        currenr_value = arr[i]
        postion = i - 1

        while postion >= 0 and arr[postion] > currenr_value:
            arr[postion + 1] = arr[postion]
            postion -= 1

        arr[postion + 1] = currenr_value

    return arr

print(insertion_sort([4,6,2,1,7]))