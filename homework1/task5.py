"""
task5.py - Shows the use of lists and dictionaries in Python.
Includes functions to return a list of favorite books and a student database.
"""

def favorite_books():
    """
    Returns a list of favorite books.
    
    Each book is represented as a tuple (title, author).
    """
    books = [
        ("1984", "George Orwell"),
        ("To Kill a Mockingbird", "Harper Lee"),
        ("The Great Gatsby", "F. Scott Fitzgerald"),
        ("Pride and Prejudice", "Jane Austen"),
        ("Moby-Dick", "Herman Melville")
    ]
    return books

def first_three_books():
    """
    Returns the first three books from the favorite books list.
    
    Demonstrates list slicing.
    """
    return favorite_books()[:3]  # Using slicing to return first three books

def student_database():
    """
    Returns a dictionary representing a simple student database.
    
    The dictionary maps student names to student ID numbers.
    """
    students = {
        "Alice": 1001,
        "Bob": 1002,
        "Charlie": 1003,
        "David": 1004,
        "Emma": 1005
    }
    return students

