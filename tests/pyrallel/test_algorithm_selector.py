"""
Module with tests for the algorithm selector.
"""
from unittest.mock import patch

from pyrallel.algorithm_selector import algorithm_selector


@patch("pyrallel.algorithm_selector.io_bound_multi_threaded_algorithm")
@patch("pyrallel.algorithm_selector.io_bound_sync_algorithm")
def test_should_return_sync_algorithm(mocked_io_bound_sync_algorithm, mocked_io_bound_multi_threaded_algorithm):
    problem_type = "io-bound"
    algorithm_type = "sync"

    algorithm = algorithm_selector(problem_type, algorithm_type)
    expected_algorithm = mocked_io_bound_sync_algorithm

    assert algorithm == expected_algorithm


@patch("pyrallel.algorithm_selector.io_bound_multi_threaded_algorithm")
@patch("pyrallel.algorithm_selector.io_bound_sync_algorithm")
def test_should_return_threaded_algorithm(mocked_io_bound_sync_algorithm, mocked_io_bound_multi_threaded_algorithm):
    problem_type = "io-bound"
    algorithm_type = "async-threads"

    algorithm = algorithm_selector(problem_type, algorithm_type)
    expected_algorithm = mocked_io_bound_multi_threaded_algorithm

    assert algorithm == expected_algorithm
