#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Computes averages, including broken down by even and odd values"""

import task_01
import data
import decimal
def get_average(nums):
    total = 0.00000000000000000000
    count = 0.00000000000000000000
    for i in nums:
        total += i
        count += 1
    return total / count

TOTAL_AVG = get_average(data.TASK_O1)
EVEN_AVG = get_average(task_01.evens_and_odds(data.TASK_O1))
ODD_AVG = get_average(task_01.evens_and_odds(data.TASK_O1, show_even = False))

import decimal
print "Task 02 Report\n------------------------\n\
Total AVG: {0}\nEven AVG: {1}\n\
Odd AVG: {2}".format(TOTAL_AVG, \
                     EVEN_AVG, ODD_AVG)
