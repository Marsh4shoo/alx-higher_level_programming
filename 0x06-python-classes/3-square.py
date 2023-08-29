#!/usr/bin/env python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

# Example usage
if __name__ == "__main__":
    try:
        size_input = int(input("Enter the size of the square: "))
        square = Square(size_input)
        print("Area of the square:", square.area())
    except ValueError:
        print("Invalid input. Size must be a non-negative integer.")

