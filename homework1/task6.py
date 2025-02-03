import os

def count_words_in_file(filename):
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"File '{filename}' not found.")

    with open(filename, "r") as file:
        content = file.read()
        words = content.split()
        print(f"DEBUG: Word count for {filename} = {len(words)}")  # Debug output
        return len(words)
