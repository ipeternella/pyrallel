"""
Module with tests for the decorators module.
"""
from unittest.mock import MagicMock
from unittest.mock import patch

from pyrallel.decorators import how_much_time


@patch("pyrallel.decorators.time")
def test_should_wrap_function_and_return_its_execution_time(mocked_time: MagicMock):
    # mocks
    mocked_time.side_effect = [0.5000, 0.7000]  # 0.2 seconds execution time

    # dummy test function
    @how_much_time
    def double(x: int) -> int:
        return 2 * x

    expected_rslt, expected_start_time, expected_end_time = 4, 0.5000, 0.7000

    rslt, start_time, end_time = double(2)

    assert rslt == expected_rslt
    assert start_time == expected_start_time
    assert end_time == expected_end_time
