def column_correct(sudoku: list, column_no: int):
    checked = []
    for i in range(len(sudoku)):
        square = sudoku[i][column_no]
        if square != 0:
            if square in checked:
                return False
            checked.append(square)
    return True
if __name__ == "__main__":
    print(column_correct(sudoku, 0))
    print(column_correct(sudoku, 1))