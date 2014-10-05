#!usr/bin/env python#
# -*- coding: utf-8 -*-
"""Even and Odds Function."""


import data
import task_01

def get_average(D):

    """Returns Average of a list.

    Args:
    numbers(numeric).

    Returns:
    Number: Returns average as a float.

    Examples:
   
    """
    ENUMS = []
    TOTAL_AVG = 0
    L = len(D)
    A= 0
    for x in D:
        A = A + x
      
    TOTAL_AVG = float(A / L)
    #ENUMS = task_01.evens_and_odds(D)
    #EVEN_AVG = get_average(ENUMS)
    #EVEN_AVG = get_average(D)
    #ODD_AVG = task_01.evens_and_odds(D, show_evens = False) 
    
    REPORT = '''    Task 02 Report
    -----------------------------
    Total AVG:      {T:,.2f} '''.format(T=TOTAL_AVG, E=EVEN_AVG)
    #EVEN_AVG:       {E:,.2f} 
   # ODD_AVG:        {O:,.2f}'''
    
    return REPORT
