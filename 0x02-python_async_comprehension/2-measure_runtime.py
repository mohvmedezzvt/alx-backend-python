#!/usr/bin/env python3
"""
This module contains a function to measure the runtime of the
async_comprehension function executed 4 times in parallel.
"""

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the runtime of the async_comprehension function executed 4 times
    in parallel.

    Returns:
        The runtime of the async_comprehension function in seconds.
    """
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = asyncio.get_event_loop().time()
    return end_time - start_time
