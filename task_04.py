#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""My task 04 code."""

import data

SALT = 'monosodium-glutamate'


def test_passwords(listobj):
    """Tests and splits a password.

    Args:
        listobj(char list): accepts a list

    Returns:
        list: returns a full name and the password

    Example:

        >>>test_passwords(data.PASSWD)
        [(Jill Lawrence', 'retinas')]
    """
    cracked = []
    for account in listobj:
        aparts = account.split(':')
        passwd = crack_it(aparts[1])
        if passwd:
            cracked.append((aparts[4], passwd))

    return cracked


def crack_it(pwdhash):
    """Cracks a password.

    Args:
        pwdhash(string): A string that reads in a crypted string. 

    Returns:
        string: returns a string of the uncrypted password if found. 

    Example:

        >>>crack_it(data)
        [retinas]
    """
    for word in data.WORDS:
        crypted = data.crypt(word, SALT)
        if pwdhash == crypted:
            retval = word
            break
        
    return retval

def report(listtup):
    """Creates a report of matched passwords to full names. 

    Args:
        listup(tuples): A list of tuples

    Returns:
        list: returns a list of full names and weak passwords

    Example:

        >>>report(data.PASSWD)
        "Cracked passwords\n------------\nroot sate..."
    """
    report = 'Cracked passwords\n' + ('-' * 65) + '\n'
    userline='{0} {1}\n'
    for user in listtup:
        report += userline.format(user[0], user[1])

    return report

print report(test_passwords(data.PASSWD))
