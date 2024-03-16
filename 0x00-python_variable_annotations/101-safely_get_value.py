#!/usr/bin/env python3
"""
This module contains a function for safely getting a value from a dictionary.
"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Return the value linked to key in dct if it exists,
    otherwise the default value.

    Args:
        dct (Mapping): The dictionary to search for the key.
        key (Any): The key to search for in the dictionary.
        default (Union[T, None], optional): The default value to return if the
        key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value linked to the key if it exists,
        otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
