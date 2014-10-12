#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_02 Assignment 6"""

import data
import task_01


def get_average(integerlist):
    """Produces the average of a list of integers

    Args:
    integerlist (list): list of integers

    Returns:
    float: the average of a list of integers

    """
    sumlist = 0
    for element in integerlist:
        sumlist = float(element + sumlist)
    lengthlist = len(integerlist)
    averagelist = float(sumlist / lengthlist)
    return float(averagelist)


TOTAL_AVERAGE = get_average(data.TASK_O1).__format__("0,.2f")
EVEN_AVERAGE = get_average(task_01.evens_and_odds
                           (data.TASK_O1, show_even=True)).__format__("0,.2f")
ODD_AVERAGE = get_average(task_01.evens_and_odds
                          (data.TASK_O1, show_even=False)).__format__("0,.2f")
