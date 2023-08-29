#!/usr/bin/env python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, side_length):
        """Initialize the Square instance with the given side length."""
        self.side_length = side_length

    def area(self):
        """Calculate the area of the square."""
        return self.side_length ** 2

    def perimeter(self):
        """Calculate the perimeter of the square."""
        return 4 * self.side_length


# Example usage
if __name__ == "__main__":
    side = float(input("Enter the side length of the square: "))
    square_instance = Square(side)
    
    print("Area:", square_instance.area())
    print("Perimeter:", square_instance.perimeter())

