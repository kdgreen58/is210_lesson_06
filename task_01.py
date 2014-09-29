#!/usr/bin/env python -tt
# -*- coding: utf-8 -*-
"""
Task 01 Even and Odds Function
Created on Mon Sep 29 18:01:46 2014

@author: ghhoward
"""
#import data

numbers = [0,1,2,3,4,5,6,7,8,9]

def evens_and_odds(numbers, show_even=True):
    """ 
    return_x
    """
    x = 0
    return_x = []
    for x in numbers:
        if show_even and (x%2 == 0):        
            return_x.append(x)
        else:
            return_x.append(x)
   
print evens_and_odds(numbers)
print evens_and_odds(numbers, False)