#!/usr/bin/env python3
"""Module that defines a function which takes a list of floats
and returns their sum."""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floats.

    Args:
        input_list (List[float]): A list of floats.

    Returns:
        float: The sum of the input list.

    Raises:
        TypeError: If the input is not a list of floats.

    Examples:
        >>> sum_list([1.5, 2.5, 3.5])
        7.5
        >>> sum_list([])
        0.0
    """
    return sum(input_list)
