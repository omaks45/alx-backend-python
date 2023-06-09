#!/usr/bin/env python3
"""
type function that sums a list of floats
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    returns the sum of the floats
    """
    return float(sum(input_list))
