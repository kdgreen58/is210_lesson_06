#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Executes a bubble sort function"""

def bubble_sort(nums):
    """Bubble sorts"""
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                sorted = False
                hold = nums[i + 1]
                nums[i + 1] = nums[i]
                nums[i] = hold
    return nums
