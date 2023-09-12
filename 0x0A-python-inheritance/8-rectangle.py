#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rep[resents a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Initialize ne Rectangle

        Args:
            width (int): width of new rectangle
            height (int): height of new rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
