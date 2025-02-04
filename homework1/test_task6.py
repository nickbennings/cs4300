"""
test_task6.py - Tests the count_words_in_file function from task6.py.
Uses metaprogramming by dynamically generating test functions.
"""

import pytest
import task6

def generate_test_function(filename, expected_word_count):
    """
    Generates a test function that verifies word count for a given file.

    Parameters:
    - filename (str): The name of the file to test.
    - expected_word_count (int): The expected word count for the file.

    Returns:
    - function: A dynamically created test function.
    """
    def test_function():
        assert task6.count_words_in_file(filename) == expected_word_count
    return test_function

# Dynamically create a test function for 'task6_read_me.txt'
test_task6_read_me = generate_test_function("task6_read_me.txt", 104)


