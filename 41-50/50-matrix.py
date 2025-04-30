
def find_max_column(matrix):

    m = len(matrix)
    n = len(matrix[0])

    columns = []

    for col in range(n):
        column = []

        for row in range(m):
            column.append(matrix[row][col])

        print(max(column))
        columns.append(max(column))

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1,2,3,], [4,5,6], [7,8,9]]

find_max_column(matrix1)
find_max_column(matrix2)        
        