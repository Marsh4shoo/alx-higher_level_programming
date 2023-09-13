#!/usr/bin/python3
"""Defines Text file-reading Function."""


def read_file(filename=""):
    """Print Contents Of UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
