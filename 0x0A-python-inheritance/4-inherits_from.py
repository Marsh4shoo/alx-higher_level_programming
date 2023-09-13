#!/usr/bin/python3
"""Defines Inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if Object is Inherited instance of a class.

    Args:
        obj (any): The object To check.
        a_class (type): Class to match the type of obj to.
    Returns:
        If obj is Inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
