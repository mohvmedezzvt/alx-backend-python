#!/usr/bin/env python3
"""
Module that takes a list input_list of integers and floats
and returns their sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and floats.

    Returns:
        float: The sum of the input list.

    Examples:
        >>> sum_mixed_list([5, 4, 3.14, 666, 0.99])
        678.13
        >>> sum_mixed_list([])
        0.0
    """
    return sum(mxd_lst)
