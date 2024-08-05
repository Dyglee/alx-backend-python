#!/usr/bin/env python3


import asyncio
from 3-tasks import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list:
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
