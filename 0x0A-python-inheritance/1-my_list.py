#!/usr/bin/python3
"""Defines Inherited list class MyList."""


class MyList(list):
    """Implements Sorted printing for built-in list class."""

    def print_sorted(self):
        """Print a list In Sorted ascending order."""
        print(sorted(self))
