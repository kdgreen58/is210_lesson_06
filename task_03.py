#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_02 Assignment 6"""

import data


def bubble_sort(bubblelist):
    """accepts a list of integers and orders
    in ascending order

    Args
    bubblelist (list) : list of integers to be
        returned in ascending order

    Returns:
    list: list of integers in ascending order
    """
    listlength = len(bubblelist)
    for i in range(0, listlength):
        moved = False
        for value in range(0, listlength-i-1):
            if bubblelist[value] > bubblelist[value + 1]:
                holder = bubblelist[value + 1]
                bubblelist[value + 1] = bubblelist[value]
                bubblelist[value] = holder
                moved = True
        if not moved:
            break

    return bubblelist
