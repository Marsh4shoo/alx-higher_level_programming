#!/usr/bin/python3
"""Defines Class Student."""


class Student:
    """Represent Student."""

    def __init__(self, first_name, last_name, age):
        """Initialize New Student.

        Args:
            first_name (str): First Name Of The Student.
            last_name (str): Last Name Of the Student.
            age (int): Age Of the Student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get Dictionary representation Of The Student.

        If attrs is a List Of strings, represents Only those attributes
        included in the list.

        Args:
            attrs (list): (Optional) The attributes To represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
