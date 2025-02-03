import task7

def test_calculate_array_mean():
    assert task7.calculate_array_mean([1, 2, 3, 4, 5]) == 3.0
    assert task7.calculate_array_mean([10, 20, 30]) == 20.0
    assert task7.calculate_array_mean([5, 10, 15]) == 10.0
