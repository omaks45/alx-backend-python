#!/usr/bin/env python3
"""
type function of a mixed type
"""


from typing import List
from typing import Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    returns their sum as a float
    """
    return float(sum(mxd_list))
