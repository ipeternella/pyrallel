"""
Module with IO-bound problems, e.g.: requests.
"""
import logging
from typing import List
from typing import Tuple

import requests
from pyrallel.decorators import how_much_time
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
