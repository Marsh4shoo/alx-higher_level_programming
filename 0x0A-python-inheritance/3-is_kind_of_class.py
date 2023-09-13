#!/usr/bin/python3
"""Defines class and Inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if Object is an Instance or inherited instance of a class.

    Args:
        obj (any): Object to check.
        a_class (type): CLass to match the type of obj to.
    Returns:
        If obj is Instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
