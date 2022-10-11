import numpy as np


# check if the square is not attacked already
# we go column by column, so only the left side needs to be checked
# and column can be ignored, since each column should have 1 queen
def square_is_safe(board, row, col):
    # row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # diagonal 1
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # diagonal 2
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


# recursive function to solve n queens
def recursive_solve_n_queens(board, col):
    n = len(board)
    # end of program
    if col >= len(board):
        return True

    # iterate over rows
    for row in range(n):
        # place queen if safe
        if square_is_safe(board, row, col):
            board[row][col] = 1

            # recursive call, if solved, return true
            if recursive_solve_n_queens(board, col + 1):
                return True
            # if not solved, remove queen and go to next row (next iteration of i)
            board[row][col] = 0
    return False


# function to make board and call recursive function
def solve_n_queens(size):
    board = np.zeros((size, size), dtype=int)
    if not recursive_solve_n_queens(board, 0):
        print("Solution does not exist")
        return
    print(board)


solve_n_queens(6)
