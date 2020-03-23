"""
Module with decorators for the app.
"""
from functools import wraps
from time import time
from typing import Callable


def how_much_time(fn: Callable) -> Callable:
    """
    Wraps a function result with the time it took to process it.
    """

    @wraps(fn)
    def wrapper(*args, **kwargs):
        """
        Time wrapper for the function.
        """
        start_time = time()

        # actual function invocation
        result = fn(*args, **kwargs)

        end_time = time()

        return result, start_time, end_time

    return wrapper
