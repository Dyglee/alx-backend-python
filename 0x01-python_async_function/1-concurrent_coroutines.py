#!/usr/bin/env python3
import asyncio
from 0-basic_async_syntax import wait_random


async def wait_n(n, max_delay):
    delays = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
