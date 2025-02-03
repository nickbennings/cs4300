import task5

def test_favorite_books():
    books = task5.favorite_books()
    assert isinstance(books, list)
    assert len(books) >= 5
    assert books[0] == ("1984", "George Orwell")

def test_first_three_books():
    first_three = task5.first_three_books()
    assert len(first_three) == 3
    assert first_three == [
        ("1984", "George Orwell"),
        ("To Kill a Mockingbird", "Harper Lee"),
        ("The Great Gatsby", "F. Scott Fitzgerald")
    ]

def test_student_database():
    students = task5.student_database()
    assert isinstance(students, dict)
    assert "Alice" in students
    assert students["Alice"] == 1001
    assert len(students) == 5

