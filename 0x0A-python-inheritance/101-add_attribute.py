#!/usr/bin/python3
"""Define function that adds a new attribute to an object"""


def add_attribute(obj, att, value):
    """Add new attribute to object if possible

    Args:
        obj (any): object to add an attribute to
        att (str): attribute to add to the object
        value (any): value of attribute
    Raises:
        TypeErro: If attribute cannot be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
