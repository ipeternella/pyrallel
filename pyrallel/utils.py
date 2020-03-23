"""
Module with Utility functions.
"""
from typing import List
from typing import Tuple


def split_list_into_chunks(xs: List, chunks_size: int) -> List:
    """
    Creates a new list with sub lists (chunks) from the original xs list.
    """
    list_with_chunks = [xs[i : i + chunks_size] for i in range(0, len(xs), chunks_size)]

    return list_with_chunks
