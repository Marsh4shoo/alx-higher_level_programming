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
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of Rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation Of Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string

