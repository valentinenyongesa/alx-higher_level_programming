#!/usr/bin/python3
"""Aclass checking function"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a given class

    Args:
        obj: object to check
        a_class: class to match the type of object to
    Returns:
        True if the object is an instance of a class
        Otherwisw False
    """
    if type(obj) == a_class:
        return True
    return False
