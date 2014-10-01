#!/usr/bin/env python -tt
# -*- coding: utf-8 -*-
"""
Task 02 Average of a List
Created on Tuesday Sep 30 2014

@author: ghhoward

Task 02: Average of a List

This task builds on the work done for task_01. Now you will need to import your task_01 and use the evens_and_odds() function to further analyze the data. Create an additional function named get_average() that returns the average value of a list of positive integers.

Specifications

Open task_02.py
Import your task_01.py file
Import the data.py file
Create a function named get_average() that accepts a list object of integers as its only parameter.
Use a loop to total the sum of the individual list values
return the average as a float object
Assign the returned value get_average(data.TASK_01) to a variable named TOTAL_AVG
Assign EVEN_AVG the average of only the even numbers using your task_01.events_and_odds() function
Assign ODD_AVG the average of only the odd numbers using your task_01.events_and_odds() function
Produce a report of the data. Display formatted representations with commas separating thousands and only two decimals of accuracy.
Example Report Output

Task 02 Report
-------------------------------
Total AVG: 2,833,713.08
Even AVG:  966,486.12
Odd AVG:   4,715,937.84
"""
import data

def get_average()
