#!/usr/bin/python3
"""JSON representation that writes object to text file"""
import json


def save_to_json_file(my_obj, filename):
    """Write object to a text file using JSON representation"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
