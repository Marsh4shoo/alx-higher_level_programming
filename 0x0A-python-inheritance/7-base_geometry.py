#!/usr/bin/python3
"""Defines Base geometry class BaseGeometry."""


class BaseGeometry:
    """Reprsent Base geometry."""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate Parameter As integer.

        Args:
            name (str): The name Of parameter.
            value (int): The parameter To validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must Be integer".format(name))
        if value <= 0:
            raise ValueError("{} must Be greater than 0".format(name))
