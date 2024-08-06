#!/usr/bin/env python3
"""
Collects random numbers using async comprehensions.
"""

from typing import List
import importlib
async_generator = importlib.import_module('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Returns:
        A list of 10 random numbers.
    """
    return [i async for i in async_generator()]
