
def find_mult(m,n):
    elements = list(range(1, m * n + 1))

    matrix = [elements[i * n: (i+1*n)] for i in range(m)]

    for row in matrix:
        print(row)

    column_products = [1] * n

    for col in range(n):
        for row in range(m):
            column_products[col] *= matrix[row][col]

    print(column_products)
    print(max(column_products))

    find_mult(3,3)