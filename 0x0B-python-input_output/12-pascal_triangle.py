#!/usr/bin/python3
"""Defines Pascal's Triangle Function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle Of Size n.

    Returns List Of lists of Integers Representing the Triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
