#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 code."""

import task_01
import data


def get_average(numbers):
    """Finds the average of a list.

    Args:
        numbers(num): A numeric type that reads in number(s).

    Returns:
        numeric (float): returns the average of a list

    Example:

        >>>get_average(data.task_O1)
        2,833,713.08
    """
    total = 0.0
    for num in numbers:
        total += num

    return total / len(numbers)

TOTAL_AVG = get_average(data.TASK_O1)
EVEN_AVG = get_average(task_01.evens_and_odds(data.TASK_O1))
ODD_AVG = get_average(task_01.evens_and_odds(data.TASK_O1, False))

REPORT = '''Task 02 Report
---------------------------------
Total AVG: {0:,.2f}
Even AVG:  {1:,.2f}
Odd AVG:   {2:,.2f}'''

print REPORT.format(TOTAL_AVG, EVEN_AVG, ODD_AVG)
