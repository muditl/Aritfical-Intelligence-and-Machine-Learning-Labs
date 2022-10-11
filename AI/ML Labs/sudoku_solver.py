import numpy as np


def row_is_valid(grid, row, col, num):
    for x in range(9):
        if grid[row, x] == num:
            return False
    return True


def col_is_valid(grid, row, col, num):
    for y in range(9):
        if grid[y, col] == num:
            return False
    return True


def box_is_valid(grid, row, col, num):
    box_x_and_y = get_box_x_and_y(row, col)
    for x in box_x_and_y[0]:
        for y in box_x_and_y[1]:
            if grid[x, y] == num:
                return False
    return True


def get_box_x_and_y(row, col):
    if row < 3 and col < 3:
        return [[0, 1, 2], [0, 1, 2]]
    if row < 3 and 2 < col < 6:
        return [[0, 1, 2], [3, 4, 5]]
    if row < 3 and 5 < col < 9:
        return [[0, 1, 2], [6, 7, 8]]
    if 2 < row < 6 and col < 3:
        return [[3, 4, 5], [0, 1, 2]]
    if 2 < row < 6 and 2 < col < 6:
        return [[3, 4, 5], [3, 4, 5]]
    if 2 < row < 6 and 5 < col < 9:
        return [[3, 4, 5], [6, 7, 8]]
    if 5 < row < 9 and col < 3:
        return [[6, 7, 8], [0, 1, 2]]
    if 5 < row < 9 and 2 < col < 6:
        return [[6, 7, 8], [3, 4, 5]]
    if 5 < row < 9 and 5 < col < 9:
        return [[6, 7, 8], [6, 7, 8]]


def is_valid(grid, row, col, num):
    return row_is_valid(grid, row, col, num) and col_is_valid(grid, row, col, num) and box_is_valid(grid, row, col, num)


def solve_sudoku(grid, row, col):
    # end of sudoku
    if row == len(grid) - 1 and col == len(grid):
        return True

    # column overflow into next row
    if col == len(grid):
        row += 1
        col = 0

    # if already filled, go to next col
    if grid[row][col] > 0:
        return solve_sudoku(grid, row, col + 1)
    for num in range(1, 10, 1):
        # if valid, place and recursive call for next col
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid, row, col + 1):
                return True
        # if not valid put zero and try next num
        grid[row][col] = 0
    return False


def make_grid_from_string(sudoku_str):
    sudoku = np.zeros((9, 9), dtype=int)
    if len(sudoku_str) != 81:
        raise ValueError("Expected 81 characters, got {}.".format(str(len(sudoku_str))))
    for i in range(81):
        sudoku[int(i / 9), i % 9] = sudoku_str[i]
    return sudoku


unsolved_str_1 = '050000190000000042910027568345001906700340000890206003008700210160008004000100685'  # easy
unsolved_str_2 = '000940000008070100069020005450600008036805020082000000004280003010000057000001980'  # medium
unsolved_str_3 = '600500100800004360300900000100080200000000000050400600070200400010009002000000093'  # hard

sudoku_grid = make_grid_from_string(unsolved_str_3)
solve_sudoku(sudoku_grid, 0, 0)
print(sudoku_grid)
