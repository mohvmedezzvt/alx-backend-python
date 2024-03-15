#!/usr/bin/env python3
"""
This module contains a function to_kv that takes a string and a number as
arguments and returns a tuple containing the string and the square
of the number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple containing the first argument and the square
    of the second argument.

    Args:
        k (str): A string.
        v (Union[int, float]): An integer or a float.

    Returns:
        Tuple[str, float]: A tuple containing the first argument and the
        square of the second argument.

    Examples:
        >>> to_kv('eggs', 3)
        ('eggs', 9.0)
        >>> to_kv('school', 0.02)
        ('school', 0.0004)
    """
    return (k, v * v)
