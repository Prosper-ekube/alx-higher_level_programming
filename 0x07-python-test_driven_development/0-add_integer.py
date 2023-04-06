#!/usr/bin/python3
"""This module defines a function that returns the sum of two integers"""


def add_integer(a, b=98):
    """Returns the sum of two integers"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float) or isinstance(b, float):
        return (int(a) + int(b))
    else:
        return a + b
