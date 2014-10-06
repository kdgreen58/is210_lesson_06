#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_02 Assignment 6"""

import data
import crypt

SALT = "monosodium-glutamate"


def test_passwords(inputlist):
    """
    """
    hashedpwds = []
    username = []
    for i in inputlist:
        hashedpwds.append(i.split(":")[1])
        username.append(i.split(":")[4])
    return username, hashedpwds


def crack_it(pwds=test_passwords(data.PASSWD)):
    crackedpwds = []
    username = []
    crack = test_passwords(data.PASSWD)
    words = data.WORDS
    for w in words:
        crypted = data.crypt(w, SALT)
        for n in crack[1]:
            if n == crypted:
                crackedpwds.append(w)
                return crackedpwds
test = crack_it()
print test