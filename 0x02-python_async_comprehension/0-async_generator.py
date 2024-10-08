#!/usr/bin/env python3
"""
This module contains a coroutine that generates random numbers asynchronously.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Loops 10 times, each time asynchronously waits for 1 second,
    then yields a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
