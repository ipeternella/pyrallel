"""
Module with IO-bound problems, e.g.: requests.
"""
import logging
from typing import List
from typing import Tuple

import numpy as np
import requests
from pyrallel.decorators import how_much_time
from pyrallel.graphs.plotting import plot_task_duration_graph
from requests import Response

logger = logging.getLogger(__name__)


@how_much_time
def fetch_remote_content(url: str) -> Response:
    """
    Executes a GET request to an URL.
    """
    response = requests.get(url)  # automatically generates a Session object.
    return response


def fetch_remote_content_many_times(target_url: str, amount_of_requests: int = 15) -> List[Tuple[float, float]]:
    """
    Executes a GET requests to an URL many times according to the amount_of_requests param.
    Returns the duration of these requests in List of Tuples in the form: [(start, end), (start, end)..]
    """
    sites = [target_url] * amount_of_requests
    durations = []

    for url in sites:
        response, start, end = fetch_remote_content(url)
        durations.append((start, end))

    return durations


def io_bound_sync_algorithm():
    """
    Sync algorithm for the I/O bound problem.
    """
    task_durations = fetch_remote_content_many_times(target_url="https://www.python.org", amount_of_requests=15)
    task_durations_array = np.array(task_durations, dtype="float64")
    task_ids_array = np.arange(1, len(task_durations_array) + 1, dtype="int64")  # int ids for every task starting at 1

    plot_task_duration_graph(
        task_durations=task_durations_array,
        task_ids=task_ids_array,
        graph_title="Task durations (Sync)",
        x_axis_title="Time (s)",
        y_axis_title="Request Number",
    )
