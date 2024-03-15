#!/usr/bin/env python3
"""Type-annotated function make_multiplier."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier."""
    def multiply(x: float) -> float:
        """Return x multiplied by multiplier."""
        return x * multiplier
    return multiply
