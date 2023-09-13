#!/usr/bin/python3
"""Defines class-checking Function."""


def is_same_class(obj, a_class):
    """Check if Object is exactly an instance Of given class.

    Args:
        obj (any): Object to check.
        a_class (type): Class to Match the type of obj to.
    Returns:
        If obj Is Exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
