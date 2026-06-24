def row_correct(sudoku: list, row_no: int):
    checked = []
    for square in sudoku[row_no]:
        if square != 0:
            if square in checked:
                return False
            checked.append(square)
    return True

if __name__ == "__main__":
    print(row_correct(sudoku, 0))
    print(row_correct(sudoku, 1))   