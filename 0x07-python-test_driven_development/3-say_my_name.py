#!/usr/bin/python3

"""printd first and last name"""


def say_my_name(first_name, last_name=""):
    """Print a name

    Args:
        first_name(str): First name to print
        last_name(str): Last name to print
    Raises:
        TypeError: If either first or last name not string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
