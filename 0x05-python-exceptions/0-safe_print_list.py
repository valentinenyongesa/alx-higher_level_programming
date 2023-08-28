#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list and
    Returns the real number of elements printed"""
    no_elements = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end=" ")
            no_elements += 1
        except indexError:
            break
    print(" ")
    return(no_elements)
