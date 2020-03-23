"""
Pyrallel's project entry-point.
"""
import numpy as np
from pyrallel.graphs.plotting import plot_task_duration_graph
from pyrallel.problems.io_bound.fetch_remote_content_sync import fetch_remote_content_many_times
from pyrallel.problems.io_bound.fetch_remote_content_threads import fetch_remote_content_many_times_with_threads


def main():
    """
    Entry-point of the application.
    """
    task_durations = fetch_remote_content_many_times(target_url="https://www.python.org", amount_of_requests=15)
    task_durations_array = np.array(task_durations, dtype="float64")
    task_ids_array = np.arange(1, len(task_durations_array) + 1, dtype="int64")  # int ids for every task starting at 1

    plot_task_duration_graph(
        task_durations=task_durations_array,
        task_ids=task_ids_array,
        graph_title="Task durations (Sync)",
        x_axis_title="Time (s)",
        y_axis_title="Task ID",
    )


if __name__ == "__main__":
    main()
