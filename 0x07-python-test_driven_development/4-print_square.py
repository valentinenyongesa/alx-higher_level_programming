#!/usr/bin/python3

"""Square printing wit '#' """


def print_square(size):
    """Print a square

    Args:
        size(int): size length of square
    Raises:
        TypeError: If size not integer
        ValueError: If size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
