#!/usr/bin/env python3
"""
Annotate the below function’s parameters and
return values with the appropriate types
def element_length(lst):
    return [(i, len(i)) for i in lst]
"""


import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> \
        typing.List[typing.Tuple[typing.Sequence, int]]:
    """
    returns values with the appropriate types
    """
    return [(i, len(i)) for i in lst]
