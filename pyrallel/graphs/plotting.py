"""
Module with plotting features.
"""
from typing import Dict

import matplotlib.pyplot as plt
import numpy
from pyrallel.settings import GRAPH_SETTINGS


def _write_graphic_to_screen_buffer():
    """
    Writes the graphic to the video memory (screen buffer) so that it can be displayed.
    """
    plt.show()


def _apply_aesthetics_configs(graph_title: str, x_axis_title: str, y_axis_title: str, settings: Dict):
    """
    Applies graph titles, x/y axis titles and set aesthetic configurations to the graph.
    """
    title_font_size = settings["fonts"]["title"]["size"]
    title_weight = settings["fonts"]["title"]["weight"]
    x_axis_font_size = settings["fonts"]["x_axis"]["size"]
    y_axis_font_size = settings["fonts"]["y_axis"]["size"]

    plt.title(graph_title, weight=title_weight).set_fontsize(title_font_size)
    plt.xlabel(x_axis_title).set_fontsize(x_axis_font_size)
    plt.ylabel(y_axis_title).set_fontsize(y_axis_font_size)


def plot_task_duration_graph(
    task_durations: numpy.ndarray, task_ids: numpy.ndarray, graph_title: str, x_axis_title: str, y_axis_title: str,
):
    """
    Plots a graph on the screen.
    """
    # tasks data for plotting
    task_end_times = task_durations[:, 1]  # second element (end_time) of every task
    task_start_times = task_durations[:, 0]  # first element (start_time) of every task
    task_delta_times = task_end_times - task_start_times

    # graph plotting
    plt.barh(y=task_ids, width=task_delta_times, left=task_start_times)

    # aesthetics configuration
    _apply_aesthetics_configs(graph_title, x_axis_title, y_axis_title, GRAPH_SETTINGS)

    # plots the graphic
    _write_graphic_to_screen_buffer()
