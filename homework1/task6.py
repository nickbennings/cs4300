"""
task6.py - Reads a text file and counts the number of words in it.
Shows file handling in Python and includes error handling for missing files.
"""

import os

def count_words_in_file(filename):
    """
    Reads a file and counts the number of words.

    Parameters:
    - filename (str): The name of the file to read.

    Returns:
    - int: The number of words in the file.

    Raises:
    - FileNotFoundError: If the file does not exist.
    """
    
    # Check if the file exists before trying to open it
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"File '{filename}' not found.")

    # Open the file, read its content, and count the words
    with open(filename, "r") as file:
        content = file.read()
        words = content.split()  # Split content into words based on whitespace
        print(f"DEBUG: Word count for {filename} = {len(words)}")  # Debug output
        return len(words)
