#!/usr/bin/python3

"""Defines a squre based on 0-square.py"""


class Square:

    """Private instance attribute: size"""
    def __init__(self, size):
        """Defines size as a private instance

        Args:
            size (int): size of latest square.
        """
        self.__size = size
