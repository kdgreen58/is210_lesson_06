#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_01 Assignment 6"""


def evens_and_odds(numbers, show_even=True):
    """ return evens and odds from a list
    Args:
    numbers (list): list of integers
    show_even (bool): if True return evens from
        numbers, if false return odds from list

    Returns:
    list: list of even integers if show_even is
                True
        or list of odd integers if show_even
                is odd

    """
    evenlist = [even for even in range(len(numbers)) if even % 2 == 0]
    oddlist = [odd for odd in range(len(numbers)) if odd % 2 == 1]
    if show_even is True:
        returnlist = evenlist
    else:
        returnlist = oddlist
    return returnlist