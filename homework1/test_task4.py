"""
test_task4.py - Tests the calculate_discount function from task4.py.
Ensures correct discount calculation and raises errors for invalid inputs.
"""

import pytest
import task4

def test_calculate_discount():
    """Tests valid discount calculations with different input values."""
    assert task4.calculate_discount(100, 10) == 90.00
    assert task4.calculate_discount(200, 25) == 150.00
    assert task4.calculate_discount(50.5, 10) == 45.45
    assert task4.calculate_discount(100.75, 15) == 85.64

def test_calculate_discount_invalid_input():
    """Tests if calculate_discount raises ValueError for invalid inputs."""
    # Non-numeric inputs
    with pytest.raises(ValueError):
        task4.calculate_discount("100", 10)

    with pytest.raises(ValueError):
        task4.calculate_discount(100, "10")

    # Invalid discount values
    with pytest.raises(ValueError):
        task4.calculate_discount(100, -5)

    with pytest.raises(ValueError):
        task4.calculate_discount(100, 105)
