#!/usr/bin/python3
"""Defines Rectangle Subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent Square."""

    def __init__(self, size):
        """Initialize New square.

        Args:
            size (int): Size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

