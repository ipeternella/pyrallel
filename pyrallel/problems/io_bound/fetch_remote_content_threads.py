"""
Module with IO-bound problems, e.g.: requests.
"""
import logging
import threading
from concurrent.futures import ThreadPoolExecutor
from threading import current_thread
from typing import List
from typing import Tuple

import numpy as np
import requests
from pyrallel.decorators import how_much_time
from pyrallel.graphs.plotting import plot_task_duration_graph

logger = logging.getLogger(__name__)


individual_thread_variables_repository = threading.local()


@how_much_time
def fetch_remote_content_session_safe(url) -> str:
    """
    Executes a GET request to an URL using requests session.
    """
    requests_session = getattr(individual_thread_variables_repository, "requests_session", None)

    if requests_session is None:
        new_session = requests.Session()
        individual_thread_variables_repository.requests_session = new_session

        requests_session = new_session

    response = requests_session.get(url)
    return current_thread().name


def fetch_remote_content_many_times_with_threads(
    target_url: str, number_of_threads: int, amount_of_requests: int = 15
) -> List[Tuple[float, float, str]]:
    """
    Executes a GET requests to an URL many times according to the amount_of_requests param.
    Returns the duration of these requests in List of Tuples in the form: [(start, end), (start, end)..]
    """
    sites = [target_url] * amount_of_requests
    durations = []  # type: List

    with ThreadPoolExecutor(max_workers=number_of_threads) as executor:
        result_futures = executor.map(fetch_remote_content_session_safe, sites)  # fn, iterable

    for thread_id, start, end in result_futures:
        durations.append((start, end, thread_id))  # start, end, thread_id

    return durations


def io_bound_multi_threaded_algorithm():
    """
    Multi-threaded algorithm for the I/O bound problem.
    """
    task_durations = fetch_remote_content_many_times_with_threads(
        target_url="https://www.python.org", amount_of_requests=15, number_of_threads=3
    )
    tasks_thread_0 = [
        (duration[0], duration[1]) for duration in task_durations if duration[2] == "ThreadPoolExecutor-0_0"
    ]
    tasks_thread_1 = [
        (duration[0], duration[1]) for duration in task_durations if duration[2] == "ThreadPoolExecutor-0_1"
    ]
    tasks_thread_2 = [
        (duration[0], duration[1]) for duration in task_durations if duration[2] == "ThreadPoolExecutor-0_2"
    ]
    plot_task_duration_graph(
        task_durations=np.array(tasks_thread_0, dtype="float64"),
        task_ids=np.full(shape=(len(tasks_thread_0),), fill_value=0, dtype="int64"),
        graph_title="Task durations (Threads)",
        x_axis_title="Time (s)",
        y_axis_title="Task ID",
    )
