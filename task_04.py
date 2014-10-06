#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Cracking passwords!"""

import data
SALT = 'monosodium-glutamate'

def test_passwords(listobj):
    """FIX DOCSTRING"""
    tup = ()
    listsplit = [i.split(':')[1] for i in listobj]
    testing = crack_it(listsplit)

def crack_it(strobj):
    """FIX DOCSTRING"""
    for words in data.WORDS:
        print words
        cryptic = data.crypt(words, SALT)
        if cryptic == strobj:
            return strobj

def report(tuplist):
    for pword in tuplist:
        report = """
        Cracked Passwords
        ____________________________"""
        tuplist
