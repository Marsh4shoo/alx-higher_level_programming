#!/usr/bin/python3
"""Defines Class MyInt that Inherits from int."""


class MyInt(int):
    """Invert int Operators == and !=."""

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value

