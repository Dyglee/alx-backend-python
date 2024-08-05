#!/usr/bin/env python3

import time
import asyncio
from 1-concurrent_coroutines import wait_n


async def measure_time(n, max_delay):
    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n
