#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Listing even and odd numbers"""

import data
from data import TASK_O1

def evens_and_odds(numbers, show_even=True):
    """Creates a list of even numbers and a list of odd numbers.

        Args:
            numbers (list): list of numbers
            show_even (bool): determines whether the function returns list
            of even or odd values; default set to True

        Returns:
            A list of either odd or even values from numbers list.

        Examples:
            >>> evens_and_odds([1,2,3,4,5],show_even=False)
            [1, 3, 5]
            >>> evens_and_odds([1,2,3,4,5])
            [2, 4]
    """
    even = [x for x in numbers if x % 2 is 0]
    odd = [x for x in numbers if x % 2 is not 0]

    if show_even is False:
        return odd
    else:
        return even
