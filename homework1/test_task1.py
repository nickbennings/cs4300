"""
test_task1.py - Tests if task1.py correctly returns 'Hello, World!'.
"""

from task1 import hello_world

def test_hello_world():
    """Checks if hello_world() returns 'Hello, World!'."""
    assert hello_world() == "Hello, World!"

