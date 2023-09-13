#!/usr/bin/python3
"""Defines Class Student."""

class Student:
    """Represent Student."""

    def __init__(self, first_name, last_name, age):
        """Initialize New Student.

        Args:
            first_name (str): First name of Student.
            last_name (str): Last name of Student.
            age (int): Age of Student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get Dictionary representation Of Student."""
        return self.__dict__

