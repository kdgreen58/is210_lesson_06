#!/usr/bin/env python -tt
# -*- coding: utf-8 -*-
"""
Task 02 Average of a List

Task 02: Average of a List

This task builds on the work done for task_01.
Now you will need to import your task_01
and use the evens_and_odds() function
to further analyze the data.
Create an additional function named get_average()
that returns the average value of a list of positive integers.
"""
import task_01
import data
THEDATA = data.TASK_O1

TOTAL_AVG = 0.0
EVEN_AVG = 0.0
ODD_AVG = 0.0


def get_average(numbers):
    """Specifications: return the average of list

    Import the data.py file

    The function get_average()
    accepts a list object of integers as its only parameter.
    Use a loop to total the sum of the individual list values
    return the average as a float object. The display is
    formatted representations with commas separating thousands
    and only two decimals of accuracy.

    Example:
    >>> test = [1,2,3,4,5,6,7,8,9,10]
    >>> get_average(test)
    5.5
    return float(sum(numbers)/float(len(numbers)))
    http://stackoverflow.com/questions/9039961/
    finding-the-average-of-a-list
    http://stackoverflow.com/questions/10291619/
    calculating-average-in-python-using-while-loop
    """
    total = 0.0
    for number in numbers:
        total = total + number
    return float(total) / float(len(numbers))

TOTAL_AVG = get_average(THEDATA)
EVEN_AVG = get_average(task_01.evens_and_odds(THEDATA))
ODD_AVG = get_average(task_01.evens_and_odds(THEDATA, False))
print 'Task 02 Report' + '\n' + ('-' * 40)
print 'TOTAL AVG:    ' + '{0:,.2f}'.format(TOTAL_AVG)
print 'EVEN AVG:     ' + '{0:,.2f}'.format(EVEN_AVG)
print 'ODD AVG:      ' + '{0:,.2f}'.format(ODD_AVG)
