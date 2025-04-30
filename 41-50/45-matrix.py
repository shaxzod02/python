
def transform_matrix(m):
    elemets = list(range(1, m*m+1))
    matrix = [elemets[i*m: (i+1)*m] for i in range(m)]

    print("Orginal matrix")

    for row in matrix:
        print(row)

        new_list = []
        used_elements = set()

        for i in range(m):
            row = []

            for elem in matrix[i]:
                if elem not in used_elements:
                    row.append(elem)
                    used_elements.add(elem)

            for j in range(i+1, m):
                column_elem = matrix[j][m - 1 - i]
                if column_elem not in used_elements:
                    row.append(column_elem)
                    used_elements.add(column_elem)

            new_list.append(row)

        return new_list

tranformed3 = transform_matrix(3)

for row in tranformed3:
    print(row)
tranformed4 = transform_matrix(4)

for row in tranformed4:
    print(row)
