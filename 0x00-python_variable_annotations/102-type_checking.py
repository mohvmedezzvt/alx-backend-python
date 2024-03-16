#!/usr/bin/env python3
"""
This module provides a function to zoom in an array by a given factor.
"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms in on the elements of the input list by
    repeating each element a certain number of times.

    Args:
        lst (Tuple): The input list to zoom in on.
        factor (int, optional): The number of times to repeat each element.
        Defaults to 2.

    Returns:
        List: The zoomed-in list.

    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
