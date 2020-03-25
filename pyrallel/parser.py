"""
Module with the command-line parser logic.
"""
import argparse
from typing import Tuple


def get_command_line_parameters() -> Tuple[str, str]:
    """
    Extracts the command line parameters.
    """
    parser = argparse.ArgumentParser(description="Pyrallel: a way to explore Python concurrency/parallelism!.")

    parser.add_argument(
        "--problem-type",
        type=str,
        choices=["io-bound", "cpu-bound"],
        help="Problem type: 'io-bound' or 'cpu-bound'",
        required=True,
    )

    parser.add_argument(
        "--algorithm-type", type=str, default="sync", help="Algorithm type: 'sync' or 'async-threads' ",
    )

    program_args = parser.parse_args()

    return program_args.problem_type, program_args.algorithm_type
