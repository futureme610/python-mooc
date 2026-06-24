def transpose(matrix: list):
    #flip the matrix over its diagonal:
    #columns become rows and rows become columns

    new_matrix = []
    matrix_row = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix_row.append(matrix[j][i])
        new_matrix.append(matrix_row)
        matrix_row = []
    for i in range(len(matrix)):
        matrix[i] = new_matrix[i]

if __name__ == "__main__":    
    matrix = [
            [1 ,2 ,3],
            [4, 5, 6],
            [7, 8, 9]
        ]

    print(transpose(matrix))