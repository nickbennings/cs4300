import pytest
import task6

def generate_test_function(filename, expected_word_count):
    def test_function():
        assert task6.count_words_in_file(filename) == expected_word_count
    return test_function

test_task6_read_me = generate_test_function("task6_read_me.txt", 104)
