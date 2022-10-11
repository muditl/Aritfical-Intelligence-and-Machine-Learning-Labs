import datetime
import numpy as np


def recursive_knight(board, cur, cur_i, cur_j):
    # if finished
    if cur >= len(board) ** 2:
        return True
    # iterate over all possible moves
    moves = possible_moves(cur_i, cur_j, len(board))
    for move in moves:
        # if square not occupied
        if board[move[0], move[1]] == 0:
            # try occupying it, increment count
            cur = cur + 1
            board[move[0], move[1]] = cur
            # recursvice call; if solved: return
            if recursive_knight(board, cur, move[0], move[1]):
                return True
            # if not solved, backtrack
            else:
                cur = cur - 1
                board[move[0], move[1]] = 0


def possible_moves(cur_i, cur_j, board_size):
    # ordered to imporve performance
    possibilities = [(-2, -1), (1, 2), (-2, 1), (2, 1), (1, -2), (-1, 2), (-1, -2), (2, -1)]
    moves = []
    for move in possibilities:
        # add if move is inside the board
        if 0 <= cur_i + move[0] < board_size and 0 <= cur_j + move[1] < board_size:
            moves.append((move[0] + cur_i, move[1] + cur_j))
    return moves


# size of board
size = 5
print("size taken: " + str(size))

# make board
chessboard = np.zeros((size, size), int)
chessboard[0][0] = 1

# measure time taken
start = datetime.datetime.now()
recursive_knight(chessboard, 1, 0, 0)
end = datetime.datetime.now()

# calcuate time and print result
time_taken = end - start
print(chessboard)
print("time taken:" + time_taken.__str__())
