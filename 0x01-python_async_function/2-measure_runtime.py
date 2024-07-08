#!/usr/bin/env python3
"""
Measure the runtime
"""
from typing import List
import time

wait_n_module = __import__('1-concurrent_coroutines', fromlist=['wait_n'])
wait_n = wait_n_module.wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay)
    and return the average time per call.
    """
    start_time = time.perf_counter()
    await wait_n(n, max_delay)
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time / n
