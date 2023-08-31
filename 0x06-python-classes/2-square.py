#!/usr/bin/python3

"""Defines a squre based on 0-square.py"""


class Square:
    """Private instance attribute: size"""

    def __init__(self, size=0):
        """initialize new square

        Args:
            size (int): size of new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
