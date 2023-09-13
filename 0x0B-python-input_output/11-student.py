#!/usr/bin/python3
"""Defines class Student."""


class Student:
    """Represent Student."""

    def __init__(self, first_name, last_name, age):
        """Initialize New Student.

        Args:
            first_name (str): First Name of Student.
            last_name (str): Last Name of Student.
            age (int): Age of Student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get Rictionary Representation of Student.

        If attrs is List of Strings, represents Only those attributes
        included in the list.

        Args:
            attrs (list): (Optional) The Attributes To Represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all Attributes Of the Student.

        Args:
            json (dict): Key/value pairs To replace Atributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
