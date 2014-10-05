#!/usr/bin/env python
# -*- coding: utf-8 -*-

import data
def evens_and_odds(numbers, show_even = True):
    odds = []
    evens = []
    for i in numbers:
        if (i % 2 == 1):
            odds.append(i)
        else:
            evens.append(i)
    if show_even is True:
        return evens
    else:
        return odds
