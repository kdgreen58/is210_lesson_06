#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""My task 03 code."""


def bubble_sort(numbers):
    """Puts a list of numbers in order.

    Args:
        numbers(num): A numeric type that reads in numbers.

    Returns:
        list: returns a list in numerical order

    Example:

        >>>bubble_sort([3, 2, 1])
        [1, 2, 3]
    """
    length = len(numbers)
    for value in range(length - 1, 0, -1):
        for i in range(0, value):
            if numbers[i] > numbers[i + 1]:
                value = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = value

    return numbers
