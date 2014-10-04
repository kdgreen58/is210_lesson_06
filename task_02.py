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
the_average = data.TASK_O1

TOTAL_AVG = 0.0
EVEN_AVG = 0.0
ODD_AVG = 0.0

def get_average(numbers):
    """Specifications

    Open task_02.py
    Import your task_01.py file
    Import the data.py file
    Create a function named get_average()
    that accepts a list object of integers as its only parameter.
    Use a loop to total the sum of the individual list values
    return the average as a float object
    Assign the returned value get_average(data.TASK_01)
    to a variable named TOTAL_AVG
    Assign EVEN_AVG the average of only the even numbers
    using your task_01.events_and_odds() function
    Assign ODD_AVG the average of only the odd numbers
    using your task_01.events_and_odds() function
    Produce a report of the data. Display formatted
    representations with commas separating thousands
    and only two decimals of accuracy.
    Example Report Output

    http://stackoverflow.com/questions/9039961/
    finding-the-average-of-a-list
    http://stackoverflow.com/questions/10291619/
    calculating-average-in-python-using-while-loop
    """
    total = 0.0
    for number in numbers:
        total = total + number
    return float(total) / float(len(numbers))
    """return float(sum(numbers)/float(len(numbers)))"""
TOTAL_AVG = get_average(the_average)
EVEN_AVG = get_average(task_01.evens_and_odds(the_average))
ODD_AVG = get_average(task_01.evens_and_odds(the_average, False))
print TOTAL_AVG
print EVEN_AVG
print ODD_AVG
