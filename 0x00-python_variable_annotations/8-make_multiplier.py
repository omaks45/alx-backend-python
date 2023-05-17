#!/usr/bin/env python3
"""
type-annotated function make_multiplier that takes a float
multiplier as argument and returns a
function that multiplies a float by multiplier.
"""


import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """
    returns a float by multiplier
    """
    def multiply_float(n: float) -> float:
        return multiplier * n
    return multiply_float
