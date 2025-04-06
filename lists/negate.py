def negate(matrix):
    return [[-num for num in row] for row in matrix]


matrix = [[1, -2], [-3, 4]]
print(negate(matrix))

matrix = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
print(negate(matrix))

