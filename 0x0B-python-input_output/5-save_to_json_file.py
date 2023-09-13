#!/usr/bin/python3
"""Defines JSON file-writing Function."""
import json


def save_to_json_file(my_obj, filename):
    """Write Object To text File using JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
