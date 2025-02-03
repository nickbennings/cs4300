def favorite_books():
    books = [
        ("1984", "George Orwell"),
        ("To Kill a Mockingbird", "Harper Lee"),
        ("The Great Gatsby", "F. Scott Fitzgerald"),
        ("Pride and Prejudice", "Jane Austen"),
        ("Moby-Dick", "Herman Melville")
    ]
    return books

def first_three_books():
    return favorite_books()[:3]

def student_database():
    students = {
        "Alice": 1001,
        "Bob": 1002,
        "Charlie": 1003,
        "David": 1004,
        "Emma": 1005
    }
    return students

