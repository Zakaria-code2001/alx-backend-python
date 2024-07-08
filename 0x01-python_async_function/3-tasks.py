#!/usr/bin/env python3
"""Tasks"""
import asyncio
import time
wait_random = __import__('0-basic_async_syntax').wait_random


def ask_wait_random(max_delay: int):
    """
    function task_wait_random that takes an integer
    returns a asyncio.Task
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
