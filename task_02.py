#!/usr/bin/env python
# -*- coding: utf-8 -*-

import task_01
import data
def get_average(nums):
    total = 0
    count = 0
    for i in nums:
        total += i
        count += 1
    return float(total / count)

TOTAL_AVG = get_average(data.TASK_O1)
EVEN_AVG = get_average(task_01.evens_and_odds(data.TASK_O1))
ODD_AVG = get_average(task_01.evens_and_odds(data.TASK_O1, show_even = False))

import decimal
print "Task 02 Report\n------------------------\n\
Total AVG: {0}\nEven AVG: {1}\n\
Odd AVG: {2}".format(decimal.Decimal(TOTAL_AVG), \
                     decimal.Decimal(EVEN_AVG), decimal.Decimal(ODD_AVG))
