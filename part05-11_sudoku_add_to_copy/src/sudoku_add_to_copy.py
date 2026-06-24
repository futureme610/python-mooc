def print_sudoku(sudoku: list):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                sudoku[i][j] = "_"
            print(sudoku[i][j], end=" ")
            if j == 2 or j == 5:
                print(" ", end ="")
        print()
        if i == 2 or i == 5:
            print()

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku_copy = []
    copy_row = []
    for i in range(9):
        for j in range(9):
            copy_row.append(sudoku[i][j])
        sudoku_copy.append(copy_row)
        copy_row = []
    sudoku_copy[row_no][column_no] = number
    return sudoku_copy



if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
