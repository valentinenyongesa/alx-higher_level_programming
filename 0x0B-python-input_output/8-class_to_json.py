#!/usr/bin/python3
"""Defines Python class-to-JSON function"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure"""
    return obj.__dict__
