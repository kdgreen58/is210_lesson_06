#!/usr/bin/env python -tt
# -*- coding: utf-8 -*-
""" task_03 bubble sort
 The function accepts a list
'http://interactivepython.org/
courselib/static/pythonds/SortSearch/TheBubbleSort.html'
"""
import data


def bubble_sort(blob):
    """ task_03 bubble
    The function accepts a list(blob) and then evaluates
    each element to see if it is less than the previous number
    it has already evaluated. If it is, the function will need
    to swap the values and continue looping through
    the rest of the list. The mutability of blob objects using
    the index of the blob items is important.

    argument:
    'blob' is a list
    returns
    'blob' list in sorted order.

    Example
    >>> test = [8,4,6,7,8,9,234,67,-9,0,78,-4556]
    >>> bubble_sort(test)
    [-4556, -9, 0, 4, 6, 7, 8, 8, 9, 67, 78, 234]
    """
    for index in range(len(blob)-1, 0, -1):
        for i in range(index):
            if blob[i] > blob[i+1]:
                swap = blob[i]
                blob[i] = blob[i+1]
                blob[i+1] = swap
    return blob
print bubble_sort(data.TASK_O1)
