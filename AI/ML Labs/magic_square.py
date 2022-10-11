import numpy as np


def make_magic_square(size):
    if size % 2 == 0 or size < 0 or not isinstance(size, int):
        raise Exception("Size should be a postive odd int.")
    magic_square = np.zeros((size, size), int)
    current = get_top_middle(size)

    magic_square[current[0], [current[1]]] = 1
    for i in range(2, size ** 2 + 1):
        current = get_next(current, magic_square)
        magic_square[current[0], current[1]] = i
    check_magic_square(magic_square)
    return magic_square


def get_next(current, square):
    up_right = get_up_right(current, len(square))
    if is_empty(up_right, square):
        return up_right

    down = get_down(current, len(square))
    if is_empty(down, square):
        return down
    raise Exception("down was not empty idk what to do here bruh")


def is_empty(position, square):
    if square[position[0], position[1]] == 0:
        return True
    else:
        return False


def get_top_middle(size):
    return [0, int(size / 2)]


def get_up_right(current, size):
    i = current[0]
    j = current[1]
    if i >= size or j >= size:
        raise Exception("i or j out of bounds.")
    if i - 1 >= 0:
        new_i = i - 1
    else:
        new_i = size - 1

    if j + 1 < size:
        new_j = j + 1
    else:
        new_j = 0
    return [new_i, new_j]


def get_down(current, size):
    i = current[0]
    j = current[1]
    if i + 1 < size:
        new_i = i + 1
    else:
        new_i = 0
    return new_i, j


def check_magic_square(square):
    rows_check(square) and cols_check(square) and diags_check(square)


def rows_check(square):
    expected = int((len(square) ** 2) * ((len(square) ** 2) + 1) / 2 / len(square))
    sums = np.sum(square, axis=0)
    assert all(s == expected for s in sums)


def cols_check(square):
    expected = int((len(square) ** 2) * ((len(square) ** 2) + 1) / 2 / len(square))
    sums = np.sum(square, axis=1)
    assert all(s == expected for s in sums)


def diags_check(square):
    expected = int((len(square) ** 2) * ((len(square) ** 2) + 1) / 2 / len(square))
    sums = np.zeros(2, int)
    for i in range(len(square)):
        sums[0] += square[i, i]
        sums[1] += square[i, len(square) - i - 1]
    assert all(s == expected for s in sums)


print(make_magic_square(3))
