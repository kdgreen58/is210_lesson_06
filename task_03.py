#!usr/bin/env python
# -*- coding: utf-8 -*-
"""In a bubbly sort of mood...Bubble Sorting """

import data
LIST = data.TASK_O1

def bubble_sort(mylist):
    """Sorts list of numbers into ascending order.

        Args:
            mylist (list): list of numeric values

        Returns:
            A list of values listed in ascending order.

        Examples:
            >>>bubble_sort([5, 2, 7, 1], LENLIST)
            [1, 2, 5, 7]
    """
    length = len(mylist)
    for num in range(length):
        for num1 in range(length-1):
            if mylist[num1] > mylist[num1+1]:
                mylist[num1], mylist[num1+1] = mylist[num1+1], mylist[num1]
    return mylist


RESULT = bubble_sort(LIST)
print RESULT
    
