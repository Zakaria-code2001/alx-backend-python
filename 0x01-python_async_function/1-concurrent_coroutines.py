#!/usr/bin/env python3
"""
Let's execute multiple coroutines
at the same time with async
"""
from random import uniform
import asyncio
import importlib.util

module_name = "0-basic_async_syntax"
module_path = "0-basic_async_syntax.py"

spec = importlib.util.spec_from_file_location(module_name, module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

wait_random = module.wait_random


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
