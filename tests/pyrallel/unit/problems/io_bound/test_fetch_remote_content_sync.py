"""
Module with tests for the fetch remote content SYNC module.
"""
from unittest.mock import MagicMock
from unittest.mock import patch

from pyrallel.problems.io_bound.fetch_remote_content_sync import fetch_remote_content_many_times
from requests_mock import Mocker


@patch("pyrallel.decorators.time")
def test_should_make_three_requests(mocked_time: MagicMock, requests_mock: Mocker):
    # test scenario
    test_url = "http://test-url.com/"
    amount_of_requests = 3

    # mocks
    mocked_time.side_effect = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0]  # 3x starts, ends

    requests_mock.get(test_url)
    requests_mock.get(test_url)
    requests_mock.get(test_url)

    # function invocation
    durations = fetch_remote_content_many_times(target_url=test_url, amount_of_requests=amount_of_requests)

    # durations assertion
    expected_durations = [(0.5, 0.6), (0.7, 0.8), (0.9, 1.0)]
    assert durations == expected_durations

    # requests history assertion
    requests_history = requests_mock.request_history

    assert requests_history[0].method == "GET"
    assert requests_history[0].url == test_url

    assert requests_history[1].method == "GET"
    assert requests_history[1].url == test_url

    assert requests_history[1].method == "GET"
    assert requests_history[1].url == test_url
