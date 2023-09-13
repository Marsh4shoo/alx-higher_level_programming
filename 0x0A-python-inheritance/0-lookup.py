#!/usr/bin/python3
"""Defines object Attribute lookup function."""


def lookup(obj):
    """Return a list Of Object's available attributes."""
    return (dir(obj))
