#!/usr/bin/env python3

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Return the value linked to key in dct if it exists,
    otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
