"""
Module with code to select the appropriate algorithm for the asked problem.
"""
from typing import Callable

from pyrallel.problems.io_bound.fetch_remote_content_sync import io_bound_sync_algorithm
from pyrallel.problems.io_bound.fetch_remote_content_threads import io_bound_multi_threaded_algorithm


def algorithm_selector(problem_type: str, algorithm_type: str) -> Callable:
    """
    Executes the required algorithm for the given problem type.
    """
    executor_config = {
        "io-bound": {"sync": io_bound_sync_algorithm, "async-threads": io_bound_multi_threaded_algorithm},
        "cpu-bound": {},
    }

    chosen_algorithm = executor_config[problem_type][algorithm_type]
    return chosen_algorithm
