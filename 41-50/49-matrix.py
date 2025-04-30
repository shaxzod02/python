
def find_max_row(matrix):
    for row in matrix:
        print(f"{row} => {max(row)}")

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
find_max_row(matrix1)
find_max_row(matrix2)