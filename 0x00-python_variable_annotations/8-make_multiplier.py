#!/usr/bin/env python3
""" Complex types - make multiplier functions """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Return function that multiplies float by multiplier """
    def multiply(n: float) -> float:
        """ Return product of multiplier and n """
        return n * multiplier
    return multiply
