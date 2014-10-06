#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_02 Assignment 6"""

import data
import crypt

SALT = "monosodium-glutamate"


def test_passwords(inputlist):
    """

    Args:
    inputlist (list): list if user data, strings seperated with :
                Example: 'jlawrence:dK6XC5q3p0CiTu38lRZAQHZSYdU=:1:1:Jill Lawrence:/home/jlawrence'

    Returns:
    tuple: tuple of usernames and hashed passwords
    """
    hashedpwds = []
    username = []
    for i in inputlist:
        hashedpwds.append(i.split(":")[1])
        username.append(i.split(":")[4])
    return username, hashedpwds


def crack_it(pwds=test_passwords(data.PASSWD)):
    """Finds passwords that were cracked from a list
    Args:
    pwds (tuple): tuple of usernames and hashed passwords

    Returns (list): At the moment returns a
                    list of matched passwords

    """
    crackedpwds = []
    username = []
    crack = test_passwords(data.PASSWD)
    words = data.WORDS
    for w in words:
        crypted = data.crypt(w, SALT)
        for c in crack[1]:
            if c == crypted:
                crackedpwds.append(w)
                return crackedpwds
test = crack_it()
print test