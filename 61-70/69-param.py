
def sort_index(a,n):
    index_a = list(enumerate(a))

    sorted_a = sorted(index_a, key = lambda x: x[1])
    index_result = [index for index, value in sorted_a]

    return index_result

n = int(input("Nechta son kiritmoqchisiz:"))
a = list(map(int, input("Sonlarni kirting: ").split()))

print(sort_index(a,n))