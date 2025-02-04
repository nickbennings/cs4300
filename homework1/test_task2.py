"""
test_task2.py - Tests the get_data_types function from task2.py.
Ensures the returned values are of the correct types and expected values.
"""

import task2

def test_get_data_types():
    """Tests if get_data_types() returns correct data types and values."""
    integer_value, float_value, string_value, boolean_value = task2.get_data_types()

    # Check data types
    assert isinstance(integer_value, int)
    assert isinstance(float_value, float)
    assert isinstance(string_value, str)
    assert isinstance(boolean_value, bool)

    # Check expected values
    assert integer_value == 42
    assert float_value == 3.14
    assert string_value == "Hello, Python!"
    assert boolean_value is True
