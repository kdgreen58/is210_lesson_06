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
    """ accepts a list object parameter 'account'
    using the known account format 'test_password'
    calls 'crack_it' finds passwords
    'test_passwords' build a tuple list and
    calls 'report' to user and password list

    Arguement:
    Takes list with data.PASSWD format

    Returns:
    Tuple list with user and password pairs.

    Example
    >>> import data
    >>> account = ['root:SKzYTp7qhvTMCti4RBYXmxuh9tM=:0:0:root:/home/root',
    'jlawrence:dK6XC5q3p0CiTu38lRZAQHZSYdU=:1:1:Jill Lawrence:/home/jlawrence']
    >>> print test_passwords(account)
     ('root', 'satellites', 'Jill Lawrence', 'retinas')
    >>>
    """
    user_id = []
    pass_hash = []
    hash_word = ''
    rep_tuple = []
    temptup = ()

    for user_id in account:
        pass_hash = user_id.split(':')
        hash_word = crack_it(pass_hash[1])
        temptup = (pass_hash[4], hash_word)
        rep_tuple.append(tuple(temptup))
    return rep_tuple


def crack_it(hash_w):
    """ Calls the data.crypt() function with each word and
    the SALT variable.
    Compare the result of the string returned by data.crypt() with
    that passed as the input parameter.

    Arguement:
    User hash string for password

    Return:
    Password as string
    the word in 'crack' if if a match is found.

    Example:
    from PASSWD = [
    'root:SKzYTp7qhvTMCti4RBYXmxuh9tM=:0:0:root:/home/root',
    >>> import data
    >>> crack_it('SKzYTp7qhvTMCti4RBYXmxuh9tM=')
     'satellites'
    >>>
    """
    for crack in data.WORDS:
        if hash_w == data.crypt(crack, SALT):
            return crack


def report(this_tuple):
    """ Report prints "this_tuple" list
    Prints a User name and password list

    Arguement:
    Takes a tuple or list in User, password pair order

    Returns:
    return empty or None

    Example:
    >>> this_tuple = [('root', 'satellites'), ('Jill Lawrence', 'retinas')]
    >>> report(this_tuple)
    Cracked Passwords
    ----------------------------------------
    root                satellites
    Jill Lawrence       retinas
    >>>
    http://stackoverflow.com/questions/2990121/
    how-do-i-loop-through-a-python-list-by-twos"""

    print 'Cracked Passwords' + '\n' + ('-' * 40)
    for usernam in this_tuple:
        print "{0:<20}{1}".format(usernam[0], usernam[1])
    return


report(test_passwords(data.PASSWD))
