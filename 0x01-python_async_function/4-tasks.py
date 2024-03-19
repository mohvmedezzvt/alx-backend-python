#!/usr/bin/env python3
"""This module implements the task_wait_n coroutine."""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Waits for a random delay multiple times
    and returns a list of the delays.

    Args:
        n (int): The number of times to wait.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: A list of the delays in seconds.
    """
    tasks: List[asyncio.Task] = [task_wait_random(max_delay) for i in range(n)]
    delays: List[float] = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
