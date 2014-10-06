#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Cracking passwords!"""

import data
SALT = 'monosodium-glutamate'

def test_passwords(listobj):
    """FIX DOCSTRING"""
    tup = ()
    listsplit = ()
    for i in listobj:
        listsplit = i.split(':')[1]
        listsplit.append([('somepass','someusername'),('otherpass','otherusername')])
        return listsplit
#    listsplit = [i.split(':')[1] for i in listobj]
#    testing = crack_it(listsplit)

def crack_it(strobj):
    """FIX DOCSTRING"""
    for words in data.WORDS:
        cryptic = data.crypt(words, SALT)
        if cryptic == strobj:
            results = words
            return results

def report(tuplist):
    for pword in tuplist:
        report = """
        Cracked Passwords
        ____________________________"""
        tuplist
