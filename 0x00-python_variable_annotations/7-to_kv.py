#!/usr/bin/env python3
"""
Complex types - string and int/float to tuple
mandatory
"""


import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """
    calculates the square of the v and
    returns a tuple
    """
    return(k, float(v * v))
