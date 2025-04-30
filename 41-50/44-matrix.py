
def spiral_matrix(m,n):
    elements = list(range(1, m * n + 1))

    matrix = [elements[i * n: (i+1)*n] for i in range(m)]

    for i in range(m):
        if i % 2 == 0:
            matrix[i] = matrix[i]
        else:
            matrix[i] = matrix[i][::-1]

    print(elements)

spiral_matrix(3,3)
