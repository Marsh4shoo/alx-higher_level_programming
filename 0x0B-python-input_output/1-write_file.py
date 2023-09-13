#!/usr/bin/python3
"""Defines File-writing Function."""


def write_file(filename="", text=""):
    """Write String To UTF8 Text file.

    Args:
        filename (str): Name of The File to Write.
        text (str): Text to Write to The File.
    Returns:
        The Number of Characters W`:written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
