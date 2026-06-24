def block_correct(sudoku: list, row_no: int, column_no: int):
    checked = []
    for i in range(row_no, row_no + 3):
        for j in range(column_no, column_no + 3):
            square = sudoku[i][j]
            if square != 0:
                if square in checked:
                    return False
                checked.append(square)
    return True

if __name__ == "__main__":
    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))