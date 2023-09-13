#!/usr/bin/python3
"""Defines a text file (UTF8) reading function"""


def read_file(filename=""):
    """Print content of a UTFtect file to stdout"""
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end="")
