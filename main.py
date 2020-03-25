"""
Pyrallel's project entry-point.
"""
from pyrallel.algorithm_selector import algorithm_selector
from pyrallel.parser import get_command_line_parameters


def main():
    """
    Entry-point of the application.
    """
    problem_type, algorithm_type = get_command_line_parameters()
    algorithm = algorithm_selector(problem_type, algorithm_type)
    algorithm()


if __name__ == "__main__":
    main()
