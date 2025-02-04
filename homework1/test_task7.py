"""
test_task7.py - Tests the calculate_array_mean function from task7.py.
Makes sure that the function correctly computes the mean of a list using NumPy.
"""

import task7

def test_calculate_array_mean():
    """Tests if calculate_array_mean correctly computes the mean of number lists."""
    assert task7.calculate_array_mean([1, 2, 3, 4, 5]) == 3.0
    assert task7.calculate_array_mean([10, 20, 30]) == 20.0
    assert task7.calculate_array_mean([5, 10, 15]) == 10.0
