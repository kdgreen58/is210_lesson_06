#!/usr/bin/env python -tt
# -*- coding: utf-8 -*-
""" task_04 Cracking Passwords
Specifications

Create a file named task_04.py

Import the data.py file.
Instantiate a variable named SALT and
assign it a value of 'monosodium-glutamate'.
Uses a function named test_passwords()
that accepts a list object parameter 'account'.
Print a user and password list

"""
import data

SALT = 'monosodium-glutamate'


def test_passwords(account):
    """ accepts a list object parameter 'accou.nt'
    using the known account format 'test_password'
    calls 'crack_it' finds passwords
    'test_passwords' build a tuple list and
    calls 'report' to user and password list"""
    user_id = []
    pass_hash = []
    hash_word = ''
    rep_tuple = []

    for user_id in account:
        pass_hash = user_id.split(':')
        hash_word = crack_it(pass_hash[1])
        rep_tuple += (pass_hash[4], hash_word)

    report(rep_tuple)


def crack_it(hash_w):
    """ Calls the data.crypt() function with each word and
    the SALT variable.
    Compare the result of the string returned by data.crypt() with
    that passed as the input parameter.
    Return the word in 'crack' if if a match is found."""
    for crack in data.WORDS:
        if hash_w == data.crypt(crack, SALT):
            return crack


def report(this_tuple):
    """ Report prints "this_tuple list created
    by 'test_password'
    http://stackoverflow.com/questions/2990121/
    how-do-i-loop-through-a-python-list-by-twos"""
    print 'Cracked Passwords' + '\n' + ('-' * 40)
    for index in range(0, len(this_tuple)-1, 2):
        print "{0:<20} {1:<30}".format(this_tuple[index], this_tuple[index + 1])

test_passwords(data.PASSWD)
