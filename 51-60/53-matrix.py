
def reomove_min_row(matrix):
    min_value = float("inf")
    min_row = 0

    m = len(matrix)
    n = len(matrix[0])

    for row in range(m):
        for col in range(n):
            if matrix[row][col] < min_value:
                min_value = matrix[row][col]
                min_row = row

    new_matrix = [matrix[row] for row in range(m) if row != min_row]

    return new_matrix

matrix1 = [[1,2,3], [4,5,6,],[7,8,9]]
matrix2 = [[9,2,8], [4,1,6], [7,5,3]]

result1 = reomove_min_row(matrix1)
result2 = reomove_min_row(matrix2)

for row in result1:
    print(row)

for row in result2:
    print(row)