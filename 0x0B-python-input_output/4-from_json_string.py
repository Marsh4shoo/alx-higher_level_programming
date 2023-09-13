#!/usr/bin/python3
# 6-from_json_string.py
"""Defines JSON-to-object Function."""
import json


def from_json_string(my_str):
    """Return Python Object representation Of JSON string."""
    return json.loads(my_str)

