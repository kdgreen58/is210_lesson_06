#!/usr/bin/env python -tt
# -*- coding: utf-8 -*-
"""
Task 01 Even and Odds Function
Created on Mon Sep 29 18:01:46 2014

@author: ghhoward
"""

from data import numbers

def evens_and_odds(num, show_even=True):
    """ 
    
    """
    for x in num:
        if x%2 == 0:
            even_num.append(x)
        else:
            odd_num.append(x)
            
        if show_even:
            return even_num[0:]
        else:
            return odd_num[0:]   

print evens_and_odds(numbers)
print evens_and_odds(numbers, False)