def read_matrix():
    matrix = []
    with open("matrix.txt") as file:
        for line in file:
            row = [int(value) for value in line.strip().split(",")]
            matrix.append(row)
    return matrix

def matrix_sum():
    matrix = read_matrix()
    total = 0
    for row in matrix:
        total += sum(row)
    return total

def matrix_max():
    matrix = read_matrix()
    maximum = matrix[0][0]
    for row in matrix:
        for value in row:
            if value > maximum:
                maximum = value
    return maximum

def row_sums():
    matrix = read_matrix()
    return [sum(row) for row in matrix]