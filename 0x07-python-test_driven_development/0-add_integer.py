#!/usr/bin/python3

"""Adds two integers"""


def add_integer(a, b=98):
    """Returns addition of two integers a and b

    Raises:
        TypeError: if a and b is a non integer and nonfloat
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
