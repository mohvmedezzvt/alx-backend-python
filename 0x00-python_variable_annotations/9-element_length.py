#!/usr/bin/env python3
"""
Type-annotated function element_length that takes a sequence
and returns a list of tuples.
"""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples containing the length of each element in lst.

    Args:
        lst (Sequence[Sequence]): A sequence of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
        an element from lst and its corresponding length.

    Example:
        >>> element_length([[1, 2, 3], [4, 5], [6, 7, 8, 9]])
        [([1, 2, 3], 3), ([4, 5], 2), ([6, 7, 8, 9], 4)]
    """
    return [(i, len(i)) for i in lst]
