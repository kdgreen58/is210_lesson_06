#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 Code Looking at Evens and Odds"""


def evens_and_odds(numbers, show_even=True):
    """Finds even or odd values in a list and displays one or the other.

    Args:
        numbers(num): A numeric type that reads in number(s).
        show_even(bool, optional): Defaults to showing even values.

    Returns:
        list: returns all even or odd values in a list

    Example:

        >>>evens_and_odds(data.task_O1)
        [250, 728, 752]

        >>>evens_and_odds(data.task_O1, False)
        [603, 753, 745]

    """
    elist = []
    olist = []

    for val in numbers:
        if val % 2:
            olist.append(val)
        else:
            elist.append(val)

    if show_even:
        rlist = elist
    else:
        rlist = olist

    return rlist
