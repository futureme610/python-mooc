def sudoku_grid_correct(sudoku: list):
    checked_row = []
    row_no = 0
    column_no = 0
  
    for i in range(0,len(sudoku)):          # i takes the value 0,1,2...8 (each row)
        row = sudoku[i]                     # grab the current row as a list
        for square in row:                  # go through each value in that row
            if square != 0:                 # skip empty squares
                if square in checked_row:   # have we seen this number before?
                    return False            # yes - duplicate found
                else:
                    checked_row.append(square)  # no - add it to the seen list
        checked_row =[]                     # finished this row, reset for the next row
    


    for j in range(0, len(sudoku)):         # j takes the values 0,1,2...8 (each column)
        checked_column = []                 # reset at the start of each new column
        for i in range(0, len(sudoku)):     # i take the value 0,1,2...8 (each row)
            square = sudoku[i][j]           # grab the square at row i, column j
            if square != 0:                 # skip empty squares
                if square in checked_column:# have we seen this number in this column?
                    return False            # yes - duplicate found
                else:
                    checked_column.append(square)   # no - add it to the seen list


    #Check the 3x3 grids
    while row_no <= 6: 
        while column_no <= 6:
            for i in range(row_no, row_no +3):
                row = sudoku[i]
                for j in range(column_no, column_no +3):
                        square = row[j]
                        if square != 0:
                            if square in checked_row:
                                return False
                            else:
                                checked_row.append(square)
            checked_row = []
            column_no += 3
        column_no = 0
        row_no += 3

    return True

if __name__ == "__main__":
    sudoku1 = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))