#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Prints integer with "{:d}".format().

    If a value error message is incorrectly printed
    prints in stderr the error

    Args:
        value(int): integer to print
    Returns:
        if error occurs - False
        otherwise - True"""
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception:{}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
