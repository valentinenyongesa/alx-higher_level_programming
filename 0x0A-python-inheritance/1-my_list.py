#!/usr/bin/python3
"""Defines a class MyList inherited from list"""


class MyList(list):
    """Implements sorted printingfor the built in list class"""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
