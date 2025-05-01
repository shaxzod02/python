
def find_min_index(matrix):
    min_value = float("inf")
    min_index = (0,0)

    m = len(matrix)
    n = len(matrix[0])

    for row in range(m):
        for col in range(n):
            if matrix[row][col] < min_value:
                min_value = matrix[row][col]
                min_index = (row, col)

    return min_index


matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]

print(find_min_index(matrix1))
print(find_min_index(matrix2))
