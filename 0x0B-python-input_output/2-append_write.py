#!/usr/bin/python3
"""Functoin that appends a string at the end of text file"""


def append_write(filename="", text=""):
    """Appends a string at end of a text file

    Args:
        filename (str) : name of file to append to
        text (str): string to append to file
    Returns:
        Number of charactres appended
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
