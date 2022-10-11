import pytest
import numpy as np

from labs_1.magic_square import *


@pytest.mark.parametrize("size",
                         [-4, 4, 2, 5.5])
def test_throws_exception(size):
    with pytest.raises(Exception):
        assert make_magic_square(size)


@pytest.mark.parametrize("current, size, expected",
                         [([2, 4], 5, [1, 0]), ([2, 3], 7, [1, 4]), ([0, 0], 5, [4, 1])])
def test_up_right(current, size, expected):
    np.testing.assert_array_equal(get_up_right(current, size), expected)


@pytest.mark.parametrize("current, size, expected",
                         [([2, 4], 5, [3, 4]), ([2, 3], 7, [3, 3]), ([4, 0], 5, [0, 0]), ([1, 0], 3, [2, 0])])
def test_down(current, size, expected):
    np.testing.assert_array_equal(get_down(current, size), expected)


@pytest.mark.parametrize("size, expected",
                         [(5, [0, 2]), (7, [0, 3]), (3, [0, 1])])
def test_get_top_middle(size, expected):
    np.testing.assert_array_equal(get_top_middle(size), expected)


@pytest.mark.parametrize("current, square, expected",
                         [([0, 2], np.array([[0, 1, 6], [3, 5, 0], [4, 0, 2]]), [1, 2]), ([2, 0],
                                                                                          np.array(
                                                                                              [[0, 1, 0], [3, 0, 0],
                                                                                               [4, 0, 2]]), [1, 1])])
def test_get_next(current, square, expected):
    np.testing.assert_array_equal(get_next(current, square), expected)
