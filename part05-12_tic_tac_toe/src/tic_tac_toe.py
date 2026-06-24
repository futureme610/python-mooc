def play_turn(game_board: list, x: int, y: int, piece: int):
    #place the given symbol at the given coordinates of the board
    #column x first, row y second

    if x in range(3) and y in range(3) and game_board[y][x] == "" :
        game_board[y][x] = piece
        return True
    return False

    #Function should return True if the square was empty and symbol
    #successfully placed on the game board
    #Function should return False if the square was occupied or coordinates
    #were not valid    

if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "X"))
    print(game_board)