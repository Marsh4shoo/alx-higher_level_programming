#!/usr/bin/python3
"""Defines File-appending Function."""


def append_write(filename="", text=""):
    """Appends String To the End of UTF8 Text file.

    Args:
        filename (str): Name of The File to Append to.
        text (str): String to Append to The file.
    Returns:
        Number of Characters Appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

