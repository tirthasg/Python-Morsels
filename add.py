def add(*matrices):
    matrix_shapes = {tuple(len(row) for row in matrix) for matrix in matrices}
    if len(matrix_shapes) > 1:
        raise ValueError("Given matrices are not the same size.")

    return [[sum(values) for values in zip(*rows)] for rows in zip(*matrices)]


matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]
print(add(matrix1, matrix2))

matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
print(add(matrix1, matrix2))

matrix1 = [[1, 9], [7, 3]]
matrix2 = [[5, -4], [3, 3]]
matrix3 = [[2, 3], [-3, 1]]
print(add(matrix1, matrix2, matrix3))

print(add([[1, 9], [7, 3]], [[1, 2], [3]]))
