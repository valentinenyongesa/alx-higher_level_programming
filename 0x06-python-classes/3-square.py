#!/usr/bin/python

"""Define a class square"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Private instance attribute: size

        Args:
            size (int): size of new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return current area of square"""
        return (self.__size * self.__size)
