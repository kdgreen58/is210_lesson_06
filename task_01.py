#!/usr/bin/env python -tt
# -*- coding: utf-8 -*-
"""
Task 01 - Defines an "Even and Odds Function"
Imports the "data.py" file for the assignment.
"""
import data


def evens_and_odds(numbers, show_even=True):
    """Specifications - evens_and_odds()

    function - evens_and_odds()

    Takes two arguments:
    The first argument named "numbers"
    accept a number argument as (tuple) or list object
    The second argument should be named show_even
    "show_even" as a boolean type
     with a default value of True

    Uses a condition to determine if a number value is even or odd
    Returns either even or odd values as a new list object

    Examples:
    >>> print evens_and_odds((1, 2, 3))
    [2]
    >>> print evens_and_odds([1, 2,3, 4, 5, 6, 7, 8, 9, 0], False)
    [1, 3, 5, 7, 9]
    >>> A_List = [42, 66, 23, 999, 123, 29]
    >>> print evens_and_odds(A_List, False)
    [23, 999, 123, 29]
    >>>
    >>> print evens_and_odds(A_List)
    [42, 66]
    >>> print evens_and_odds(A_List, True)
    [42, 66]
    """
    return_it = []
    for its in numbers:
        if show_even and ((its % 2) == 0):
            return_it.append(its)
        elif not show_even and ((its % 2) == 1):
            return_it.append(its)
    return return_it
