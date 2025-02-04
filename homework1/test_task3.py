"""
test_task3.py - Tests functions in task3.py that check numbers, generate prime numbers, and sum numbers.
"""

import task3

def test_check_number():
    """Tests check_number() function to classify numbers as Positive, Negative, or Zero."""
    assert task3.check_number(10) == "Positive"
    assert task3.check_number(-5) == "Negative"
    assert task3.check_number(0) == "Zero"

def test_first_n_primes():
    """Tests first_n_primes() function to ensure correct generation of prime numbers."""
    assert task3.first_n_primes(5) == [2, 3, 5, 7, 11]
    assert task3.first_n_primes(10) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def test_sum_numbers_upto_100():
    """Tests sum_numbers_upto_100() function to verify correct sum calculation."""
    assert task3.sum_numbers_upto_100() == 5050

