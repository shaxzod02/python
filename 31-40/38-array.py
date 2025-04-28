

def find_number_frequency(arr):
    numbers = []
    frequency = []

    for element in arr:
        if element in numbers:
            index = numbers.index(element)
            frequency[index] += 1
        else:
            numbers.append(element)
            frequency.append(1)

    for i in range(len(numbers)):
        print(f"{numbers[i]} soni {frequency[i]} ta")

    print(f"number: {numbers}")
    print(f"frequency: {frequency}")


print(find_number_frequency([1, 3, 2, 4, 2, 1, 9, 1]))    
