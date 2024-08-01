#!/usr/bin/env python3
"""
a function that returns a tuple with a string and the square of a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns:
    A tuple containing the string and the square of the number.
    """
    return (k, float(v ** 2))
