"""
Module with settings of the project.
"""
import os

PROJECT_ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

GRAPH_SETTINGS = {"fonts": {"title": {"size": 25, "weight": "bold"}, "x_axis": {"size": 20}, "y_axis": {"size": 20}}}

THREADS_SETTINGS = {"number_of_threads": 3}
