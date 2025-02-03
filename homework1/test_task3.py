import task3

def test_check_number():
    assert task3.check_number(10) == "Positive"
    assert task3.check_number(-5) == "Negative"
    assert task3.check_number(0) == "Zero"

def test_first_n_primes():
    assert task3.first_n_primes(5) == [2, 3, 5, 7, 11]
    assert task3.first_n_primes(10) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def test_sum_numbers_upto_100():
    assert task3.sum_numbers_upto_100() == 5050

