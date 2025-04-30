

def spiral_matrix(m,n):
    elements = list(range(1, m * n + 1))

    matrix = [elements[i * n: (i+1)*n] for i in range(m)]

    for row in matrix:
        sumofrow = sum(row)

        print(f"{row}=>{sumofrow}")

spiral_matrix(3,3)        