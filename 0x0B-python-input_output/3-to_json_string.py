#!/usr/bin/python3
"""Defines a function that returns JSON representation of object"""
import json


def to_json_string(my_obj):
    """Returns JSON representation of an object string"""
    return json.dumps(my_obj)
