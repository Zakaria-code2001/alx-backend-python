#!/usr/bin/env python3
"""multiple coroutines with async"""
from random import uniform
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> list:
    """
    Spawn wait_random n times with the specified max_delay.
    Returns the list of all delays in ascending order.
    """
    tasks = []
    for task in range(n):
        tasks.append(wait_random(max_delay))
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
