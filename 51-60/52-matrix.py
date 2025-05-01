
def remove_min_column(matrix):
    min_value = float("inf")
    min_col = 0

    m = len(matrix)
    n = len(matrix[0])

    for row in range(m):
        for col in range(n):
            if matrix[row][col] < min_value:
                min_value = matrix[row][col]
                min_col = col

    new_matrix = []

    for row in matrix:
        new_row = [row[j] for j in range(len(row)) if j != min_col]
        new_matrix.append(new_row)

    return new_matrix


matrix1 = [[1,2,3,], [4,5,6], [7,8,9]]
matrix2 = [[9,2,8], [4,1,6], [7,5,3]]

result1 = remove_min_column(matrix1)
result2 = remove_min_column(matrix2)

for row in result1:
    print(row)

for row in result2:
    print(row)