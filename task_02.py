#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_02 Assignment 6"""

import data
import task_01
from decimal import *


def get_average(integerlist):
    """Produces the average of a list of integers

    Args:
    integerlist (list): list of integers

    Returns:
    float: the average of a list of integers

    """
    sumlist = 0
    for n in integerlist:
        sumlist = float(n + sumlist)
    lengthlist = len(integerlist)
    averagelist = float(sumlist / lengthlist)
    return float(averagelist)


TOTAL_AVERAGE = get_average(data.TASK_O1)
EVEN_AVERAGE = get_average(task_01.evens_and_odds(data.TASK_O1, show_even=True))
ODD_AVERAGE = get_average(task_01.evens_and_odds(data.TASK_O1, show_even=False))
print TOTAL_AVERAGE