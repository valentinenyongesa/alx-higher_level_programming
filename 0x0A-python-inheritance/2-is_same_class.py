#!/usr/bin/python3
"""Defines a class checking function"""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of a given class


    Args:
        obj : object tocheck
        a_class : class to check for the object
    Returns:
        True if object is an instance
        False if object not instance
    """
    if type(obj) == a_class:
        return True
    return False
