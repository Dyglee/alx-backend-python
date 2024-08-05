#!/usr/bin/env python3
import random
import asyncio

""" basic async """


async def wait_random(max_delay: int = 10) -> float:
    """ retuns randum sleep time """
    random_delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
