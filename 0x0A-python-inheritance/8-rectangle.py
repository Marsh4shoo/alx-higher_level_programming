#!/usr/bin/python3
"""Defines Class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent Rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize New Rectangle.

        Args:
            width (int): The width of New Rectangle.
            height (int): The height of New Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

