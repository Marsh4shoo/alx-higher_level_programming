#!/usr/bin/python3
"""Defines Python Class-to-JSON Function."""


def class_to_json(obj):
    """Return Dictionary represntation Of Simple Data structure."""
    return obj.__dict__
