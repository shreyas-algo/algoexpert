def transposeMatrix(matrix):
    columns = len(matrix)
    rows = len(matrix[0])
    transpose = [[0] * columns for _ in range(rows)]
    for row in range(rows):
        for col in range(columns):
            transpose[row][col] = matrix[col][row]
    return transpose
