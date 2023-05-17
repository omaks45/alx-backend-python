#!/usr/bin/env python3
"""
type function that sums a list of floats
"""


def sum_list(input_list: float) -> float:
    """
    returns the sum of the floats
    """
    return sum((num) for num in input_list)
