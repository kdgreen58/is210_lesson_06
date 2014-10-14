#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""My task 04 code."""

import data

SALT = 'monosodium-glutamate'


def test_passwords(listobj):
    """Tests and cracks a password.

    Args:
        listobj(char list): accepts a list

    Returns:
        list: returns

    Example:

        >>>evens_and_odds(data.task_O1)
        [250, 728, 752]
    """
    cracked = []
    for account in listobj:
        aparts = account.split(':')
        passwd = crack_it(aparts[1])
        if passwd:
            cracked.append((aparts[4], passwd))

    return cracked


def crack_it(pwdhash):
    """Finds even or odd values in a list and displays one or the other.

    Args:
        numbers(num): A numeric type that reads in number(s).
        show_even(bool, optional): Defaults to showing even values.

    Returns:
        list: returns all even or odd values in a list

    Example:

        >>>evens_and_odds(data.task_O1)
        [250, 728, 752]

        >>>evens_and_odds(data.task_O1, False)
        [603, 753, 745]

    """
    for word in data.WORDS:
        crypted = data.crypt(word, SALT)
        if pwdhash == crypted:
            retval = word
            break
        
    return retval

def report(listtup):
    """Finds even or odd values in a list and displays one or the other.

    Args:
        numbers(num): A numeric type that reads in number(s).
        show_even(bool, optional): Defaults to showing even values.

    Returns:
        list: returns all even or odd values in a list

    Example:

        >>>evens_and_odds(data.task_O1)
        [250, 728, 752]

        >>>evens_and_odds(data.task_O1, False)
        [603, 753, 745]

    """
    report = 'Cracked passwords\n' + ('-' * 50) + '\n'
    userline='{0} {1}\n'
    for user in listtup:
        report += userline.format(user[0], user[1])

    return report

print report(test_passwords(data.PASSWD))
