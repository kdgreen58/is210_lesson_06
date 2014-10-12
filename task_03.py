#!usr/bin/env python#
# -*- coding: utf-8 -*-
"""Even and Odds Function."""


import data

def bubble_sort(x):
     
    """Returns lists of intergers sorted.

    Args:
    numbers(numeric).

    Returns:
    Number: Returns a sorted list.

    Examples:
    
    """
    blist = []
    c = 0
    for a in range(len(x)- 1):
        if x[c] < x[c + 1]:
            blist.append(x[c])
            x.pop(c)
        c += 1               
        
    return blist, x
 
            

