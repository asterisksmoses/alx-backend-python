import asyncio
import random

"""This code is an asynchronous coroutine that takes
in an integer argument."""

async def wait_random(max_delay: int = 10) -> float:
    """This function defines an asynchronous coroutine
    that takes in an integer argument."""
    delay = random.uniform(0, max_delay)

    await asyncio.sleep(delay)

    return delay
