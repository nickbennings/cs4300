import pytest
import task4

def test_calculate_discount():
    assert task4.calculate_discount(100, 10) == 90.00
    assert task4.calculate_discount(200, 25) == 150.00
    assert task4.calculate_discount(50.5, 10) == 45.45
    assert task4.calculate_discount(100.75, 15) == 85.64

def test_calculate_discount_invalid_input():
    with pytest.raises(ValueError):
        task4.calculate_discount("100", 10)

    with pytest.raises(ValueError):
        task4.calculate_discount(100, "10")

    with pytest.raises(ValueError):
        task4.calculate_discount(100, -5)

    with pytest.raises(ValueError):
        task4.calculate_discount(100, 105)

