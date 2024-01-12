#!/usr/bin/env python3
""" Basic annotations - elements length """
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Return list of tuples of sequence and int """
    return [(i, len(i)) for i in lst]
