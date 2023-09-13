#!/usr/bin/python3
"""Defines Text file Insertion Function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert Text After each line Containing Given string in a file.

    Args:
        filename (str): The name Of the file.
        search_string (str): String To Search For within the file.
        new_string (str): String To insert.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
