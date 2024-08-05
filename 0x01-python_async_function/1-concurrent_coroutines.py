#!/usr/bin/env python3
import asyncio
from 0-basic_async_syntax import wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> list[float]:
    delays: list[float] = []
    tasks: List = []

    for _ in range(n):
        tasks.append(wait_random(max_delay))

    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)

    return delays
