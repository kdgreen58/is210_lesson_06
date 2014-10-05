#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_02 Assignment 6"""

import data


def bubble_sort(bubblelist):
    listlength = len(bubblelist)
    for i in range(0,listlength):
        moved = False
        for value in range(0, listlength-i-1):
            if bubblelist[value] > bubblelist[value + 1]:
                holder = bubblelist[value + 1]
                bubblelist[value + 1] = bubblelist[value]
                bubblelist[value] = holder
                swapped = True
        if not moved: break

    return bubblelist
