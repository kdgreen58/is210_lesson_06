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

TOTAL_AVG = get_average(data.TASK_01)
EVEN_AVG = get_average(task_01.evens_and_odds(data.TASK_01))
ODD_AVG = get_average(task_01.evens_and_odds(data.TASK_01, show_even = False))

print "Task 02 Report\n------------------------\n\
Total AVG: {0}\nEven AVG: {1}\n\
Odd AVG: {2}".format(TOTAL_AVG, EVEN_AVG, ODD_AVG)
