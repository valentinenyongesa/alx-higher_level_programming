#!/usr/bin/python3
"""Defines a a class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a class square"""

    def __init__(self, size):
        """Initialize new square

        Args:
            size (int): Size of new Square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
