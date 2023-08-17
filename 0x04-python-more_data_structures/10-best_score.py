#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns a Key with the largest integr val"""
    if not a_dictionary:
        return (None)

    return (max(a_dictionary, key = a_dictionary.get))
