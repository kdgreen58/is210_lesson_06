#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_02 Assignment 6"""

import data


SALT = "monosodium-glutamate"


def test_passwords(inputlist):
    """

    Args:
    inputlist (list): list if user data, strings seperated with :
                Example: 'jlawrence:dK6XC5q3p0CiTu38lRZAQHZSYdU=:
                            1:1:Jill Lawrence:/home/jlawrence'

    Returns:
    tuple: tuple of usernames and hashed passwords
    """
    hashedpwds = []
    username = []
    for i in inputlist:
        hashedpwds.append(i.split(":")[1])
        username.append(i.split(":")[4])
    return username, hashedpwds


def crack_it(crack=test_passwords(data.PASSWD)):
    """Finds passwords that were cracked from a list
    Args:
    pwds (tuple): tuple of usernames and hashed passwords

    Returns (list): At the moment returns a
                    list of matched passwords

    """
    crackedpwds = []
    crack = test_passwords(data.PASSWD)
    words = data.WORDS
    for word in words:
        crypted = data.crypt(word, SALT)
        for cpwd in crack[1]:
            if cpwd == crypted:
                crackedpwds.append(word)
                return crackedpwds