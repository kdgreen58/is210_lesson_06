#!usr/bin/env python
# -*- coding: utf-8 -*-
"""No one likes being 'average'...finding averages."""

import task_01
import data


def get_average(listobj):
    """Determines the average of a list object of integers.

        Args:
            listobj (list): list of integers

        Returns:
            an average (mean) of the integers in a list

        Examples:
            >>> get_average([1,2,3,4,5])
            3.0
    """
    total = 0
    for x in listobj:
        total = float(total+x)
    AVG = float(total/len(listobj))
    return AVG

TOTAL_AVG = "{0:,}".format(float("%.2f" % get_average(data.TASK_O1)))
EVEN_AVG = "{0:,}".format(float("%.2f" % get_average(
    task_01.evens_and_odds(data.TASK_O1))))
ODD_AVG = "{0:,}".format(float("%.2f" % get_average(
    task_01.evens_and_odds(data.TASK_O1, show_even=False))))

REPORT =  """
Task 02 Report
_________________________
Total AVG: {0}
Even AVG:  {1}
Odd AVG:   {2}"""

print REPORT.format(TOTAL_AVG, EVEN_AVG, ODD_AVG)
