#!/usr/bin/python3
"""
This module defines the MagicClass, which represents a circle.
"""

import math

class MagicClass:
    """
    Represents a circle with radius and related calculations.
    """

    def __init__(self, radius=0):
        """
        Initialize a MagicClass.

        Args:
            radius (float or int): The radius of the MagicClass circle.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculate and return the area of the MagicClass circle.
        """
        return math.pi * self.__radius ** 2

    def circumference(self):
        """
        Calculate and return the circumference of the MagicClass circle.
        """
        return 2 * math.pi * self.__radius
