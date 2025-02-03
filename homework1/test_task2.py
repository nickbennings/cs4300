import task2

def test_get_data_types():
    integer_value, float_value, string_value, boolean_value = task2.get_data_types()

    assert isinstance(integer_value, int)
    assert isinstance(float_value, float)
    assert isinstance(string_value, str)
    assert isinstance(boolean_value, bool)

    assert integer_value == 42
    assert float_value == 3.14
    assert string_value == "Hello, Python!"
    assert boolean_value is True
