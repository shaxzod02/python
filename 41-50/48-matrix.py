
def compare_row(matrix):
    for row_index, row in enumerate(matrix):

        count_positive = sum(1 for num in row if num > 0)
        count_negative = sum(1 for num in row if num < 0)

        if count_positive == count_negative:
            return row_index + 1

    return "Bunday qator yoq"

matrix1 = [[1, -2, 3], [4, -5, 6], [7, -8, 9]]
matrix2 = [[-1, 2, -3], [4, -5, 6], [7, -8, 9]]

print(compare_row(matrix1))
print(compare_row(matrix2))

        

