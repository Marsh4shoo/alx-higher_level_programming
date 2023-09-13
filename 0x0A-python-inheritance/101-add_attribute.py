#!/usr/bin/python3
"""Defines Function that adds Attributes to objects."""


def add_attribute(obj, att, value):
    """Add New attribute to an object if possible.

    Args:
        obj (any): The Object To add an attribute to.
        att (str): The name Of the Attribute to add to obj.
        value (any): The value Of att.
    Raises:
        TypeError: If Attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)

