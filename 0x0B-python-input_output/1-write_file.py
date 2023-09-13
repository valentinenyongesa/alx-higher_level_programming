#!/usr/bin/python3
"""Defines a file writing function"""


def write_file(filename="", text=""):
    """Writes string to text file and returns number of characters
    
    Args:
        filename (str): name of file to write
        text (str): text to write to the file
    Returns:
        Number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)

