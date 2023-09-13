#!/usr/bin/python3
"""Define Object (Python data structure) represented by a JSON string"""
import json


def from_json_string(my_str):
    """Returns object (Python data structure) represented by JSON string"""
    return json.loads(my_str)
