#!/usr/bin/python3
"""Aclass checking function"""


def inherits_from(obj, a_class):
    """Check if an object is an inherited instance of a given class

    Args:
        obj: object to check
        a_class: class to match the type of object to
    Returns:
        True if the object is an inherited instance of a class
        Otherwisw False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
