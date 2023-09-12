#!/usr/bin/python3
"""Defines a Rectangle subclass square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents square"""

    def __init__(self, size):
        """Initialize new square

        Args:
            size (int): size of new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
