#!/usr/bin/env python3
"""
Measure the runtime
"""
from random import uniform
import asyncio
from typing import List
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay)
    and return the average time per call.
    """
    start_time = time.monotonic()
    await wait_n(n, max_delay)
    end_time = time.monotonic()
    total_time = end_time - start_time
    return total_time / n
