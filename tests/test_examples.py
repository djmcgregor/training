""" Tests for the examples submodule """
import numpy as np
from numpy.testing import assert_allclose

from learning import examples


def test_add():
    """ Test add function """
    assert examples.add(2, 4) == 6      # test ints
    assert examples.add(2.5, 6) == 8.5  # test floats

    # test numpy arrays
    np_case = examples.add(np.array([[2, 4.5], [4, 1]]), np.array([[-2, 0.1], [8, 1]]))
    assert_allclose(np_case, np.array([[0, 4.6], [12, 2]]))


def test_needs_formatting():
    """ Example of successful test """
    assert examples.needs_formatting(1, 2, 3, 4) == 21
