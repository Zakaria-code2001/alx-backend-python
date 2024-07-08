#!/usr/bin/env python3
"""The basics of async"""
from random import uniform
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    max_delay, with a default value of 10,
    wait_random that waits for a random delay between 0 and max_delay
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
