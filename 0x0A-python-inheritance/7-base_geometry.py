#!/usr/bin/python3
"""Defines class BaseGeometry"""


class BaseGeometry:
    """class BaseGeometry"""

    def area(self):
        """If not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate parameter as integer

        Args:
            name (str): name of parameter
            value (int) : parameter value to validate
        Raises:
            TypeError: if value is not integer
            ValueError: parameter to validate
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
