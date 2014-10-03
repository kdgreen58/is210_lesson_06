#!/usr/bin/env python -tt
# -*- coding: utf-8 -*-
"""
Task 01 Even and Odds Function
Created on Mon Sep 29 18:01:46 2014
"""
import data

def evens_and_odds(numbers, show_even=True):
    """Specifications

    Create a file named task_01.py
    Import the data.py file. You will use the TASK_01 list object a
    s your data source.
    Within, task_01.py, define a function named evens_and_odds()
    evens_and_odds() will accept numbers as a list object
    and show_even as a boolean value of True or False
    Takes 2 arguments:
    The first argument should be named numbers
    The second argument should be named show_even
    and have a default value of True
    Uses a condition to determine if a number value is even or odd
    Uses a condition to return either even or odd values
    Returns a new list objec
    """
    
    return_it = []
    for x in numbers:
        if show_even and (x%2 == 0):
            return_it.append(x)
        elif not show_even and (x%2 == 1):
            return_it.append(x)
    return return_it
