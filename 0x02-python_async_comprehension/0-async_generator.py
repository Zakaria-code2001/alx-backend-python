#!/usr/bin/env python3
"""
Write a coroutine called async_generator
that takes no arguments.
The coroutine will loop 10 times
each time asynchronously wait 1 second
then yield a random number between 0 and 10.
Use the random module.
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random delay between 0 and max_delay"""
    random_number = random.uniform(0, max_delay)
    await asyncio.sleep(random_number)
    return random_number
