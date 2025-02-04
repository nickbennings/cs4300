"""
test_task5.py - Tests functions in task5.py that handle lists and dictionaries.
Ensures favorite books and student database functions return expected values.
"""

import task5

def test_favorite_books():
    """Tests if favorite_books() returns a list of books with at least 5 entries."""
    books = task5.favorite_books()
    assert isinstance(books, list)
    assert len(books) >= 5
    assert books[0] == ("1984", "George Orwell")  # Ensures first book is correct

def test_first_three_books():
    """Tests if first_three_books() correctly returns the first 3 books."""
    first_three = task5.first_three_books()
    assert len(first_three) == 3  # Must return exactly 3 books
    assert first_three == [
        ("1984", "George Orwell"),
        ("To Kill a Mockingbird", "Harper Lee"),
        ("The Great Gatsby", "F. Scott Fitzgerald")
    ]

def test_student_database():
    """Tests if student_database() returns a valid dictionary with correct student IDs."""
    students = task5.student_database()
    assert isinstance(students, dict)  # Should be a dictionary
    assert "Alice" in students  # Alice must be a key in the dictionary
    assert students["Alice"] == 1001  # Alice's student ID should be 1001
    assert len(students) == 5  # Ensures there are exactly 5 students
